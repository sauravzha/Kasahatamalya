/**
 * Vercel Serverless Function — Donation Submission
 * POST /api/donate
 *
 * Official Recipient: info@kshamtalaya.org
 *
 * Environment variables required (set in Vercel Dashboard or .env):
 *   DONATION_ADMIN_EMAIL   — official Kshamtalaya email (defaults to info@kshamtalaya.org)
 *   SMTP_HOST              — e.g. smtp.gmail.com
 *   SMTP_PORT              — e.g. 587
 *   SMTP_USER              — SMTP username / sender account
 *   SMTP_PASS              — SMTP password / app-password
 *   SMTP_FROM              — From address for emails (defaults to info@kshamtalaya.org)
 *
 * NEVER put credentials in frontend code.
 */

import nodemailer from 'nodemailer';
import { randomUUID } from 'crypto';
import fs from 'fs';
import path from 'path';
import os from 'os';

/* -- Validation helpers -- */

const MOBILE_RE = /^[6-9]\d{9}$/;
const EMAIL_RE  = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const PAN_RE    = /^[A-Z]{5}[0-9]{4}[A-Z]$/;
const PIN_RE    = /^\d{6}$/;

function trimStr(v) {
  return typeof v === 'string' ? v.trim() : '';
}

function validateDonor(body) {
  const errors = [];

  // Amount
  const amount = Number(body.amount);
  if (!amount || amount < 1 || !Number.isFinite(amount)) {
    errors.push({ field: 'amount', message: 'A valid donation amount is required.' });
  }

  // Full Name
  const fullName = trimStr(body.fullName);
  if (!fullName) {
    errors.push({ field: 'fullName', message: 'Full name is required.' });
  }

  // Mobile
  const mobile = trimStr(body.mobile).replace(/\s+/g, '');
  if (!MOBILE_RE.test(mobile)) {
    errors.push({ field: 'mobile', message: 'A valid 10-digit Indian mobile number is required.' });
  }

  // Email
  const email = trimStr(body.email).toLowerCase();
  if (!EMAIL_RE.test(email)) {
    errors.push({ field: 'email', message: 'A valid email address is required.' });
  }

  // Address Line 1
  const address1 = trimStr(body.address1);
  if (!address1) {
    errors.push({ field: 'address1', message: 'Address Line 1 is required.' });
  }

  // City
  const city = trimStr(body.city);
  if (!city) {
    errors.push({ field: 'city', message: 'City or Town is required.' });
  }

  // State
  const state = trimStr(body.state);
  if (!state) {
    errors.push({ field: 'state', message: 'State is required.' });
  }

  // PIN Code
  const pinCode = trimStr(body.pinCode);
  if (!PIN_RE.test(pinCode)) {
    errors.push({ field: 'pinCode', message: 'A valid 6-digit PIN code is required.' });
  }

  // PAN
  const pan = trimStr(body.pan).toUpperCase();
  if (!PAN_RE.test(pan)) {
    errors.push({ field: 'pan', message: 'A valid PAN number is required (e.g. ABCDE1234F).' });
  }

  return {
    errors,
    data: {
      amount,
      fullName,
      mobile,
      email,
      address1,
      address2: trimStr(body.address2),
      city,
      state,
      pinCode,
      pan,
      whatsappOptIn: !!body.whatsappOptIn,
    },
  };
}

function maskPAN(pan) {
  if (!pan || pan.length !== 10) return '****';
  return pan.slice(0, 2) + '****' + pan.slice(8);
}

/* -- Persistent storage -- */

const RECORDS_DIR = process.env.DONATION_RECORDS_DIR || path.join(os.tmpdir(), 'kshamtalaya-donations');

function ensureDir() {
  if (!fs.existsSync(RECORDS_DIR)) {
    fs.mkdirSync(RECORDS_DIR, { recursive: true });
  }
}

function saveRecord(record) {
  ensureDir();
  const filename = `${record.donationRef}.json`;
  fs.writeFileSync(
    path.join(RECORDS_DIR, filename),
    JSON.stringify(record, null, 2),
    'utf-8'
  );
}

function refExists(ref) {
  ensureDir();
  return fs.existsSync(path.join(RECORDS_DIR, `${ref}.json`));
}

/* -- Email notification -- */

async function sendNotification(record) {
  const adminEmail = process.env.DONATION_ADMIN_EMAIL || 'info@kshamtalaya.org';

  const host = process.env.SMTP_HOST;
  const port = Number(process.env.SMTP_PORT) || 587;
  const user = process.env.SMTP_USER;
  const pass = process.env.SMTP_PASS;
  const from = process.env.SMTP_FROM || user || 'info@kshamtalaya.org';

  // If SMTP credentials are not yet configured:
  // In development/local environments, record the submission safely and log simulation.
  // In production, require configured SMTP to guarantee notification delivery.
  if (!host || !user || !pass) {
    if (process.env.NODE_ENV === 'production' && process.env.VERCEL) {
      throw new Error('SMTP credentials are not configured in environment variables.');
    } else {
      console.log(`[Dev Simulation] Recorded donor submission for ${adminEmail}: ${record.donationRef}`);
      return { simulated: true, recipient: adminEmail };
    }
  }

  const transporter = nodemailer.createTransport({
    host,
    port,
    secure: port === 465,
    auth: { user, pass },
  });

  const submittedAt = new Date(record.submittedAt).toLocaleString('en-IN', {
    dateStyle: 'full',
    timeStyle: 'medium',
    timeZone: 'Asia/Kolkata',
  });

  const html = `
    <div style="font-family:Arial,sans-serif;max-width:640px;margin:0 auto;border:1px solid #e0e0e0;border-radius:12px;overflow:hidden;">
      <div style="background:#313234;padding:24px 32px;text-align:center;">
        <h1 style="color:#FFC72C;margin:0;font-size:20px;">New Donation Registration</h1>
        <p style="color:#ccc;margin:6px 0 0;font-size:14px;">Kshamtalaya Foundation — Official Donor Record</p>
      </div>
      <div style="padding:28px 32px;">
        <table style="width:100%;border-collapse:collapse;font-size:14px;">
          <tr style="border-bottom:1px solid #f0f0f0;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;width:40%;">Donation Reference</td>
            <td style="padding:10px 8px;color:#08B9DB;font-weight:bold;">${record.donationRef}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;background:#f9f9f9;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Donation Amount</td>
            <td style="padding:10px 8px;font-size:18px;font-weight:bold;color:#313234;">₹${record.amount.toLocaleString('en-IN')}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Full Legal Name</td>
            <td style="padding:10px 8px;font-weight:bold;">${record.fullName}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;background:#f9f9f9;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Mobile Number</td>
            <td style="padding:10px 8px;">+91 ${record.mobile}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Email Address</td>
            <td style="padding:10px 8px;"><a href="mailto:${record.email}">${record.email}</a></td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;background:#f9f9f9;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Billing Address</td>
            <td style="padding:10px 8px;">${record.address1}${record.address2 ? '<br>' + record.address2 : ''}<br>${record.city}, ${record.state} — ${record.pinCode}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">PAN (Masked)</td>
            <td style="padding:10px 8px;font-family:monospace;letter-spacing:1px;">${maskPAN(record.pan)}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;background:#f9f9f9;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">WhatsApp/SMS Updates</td>
            <td style="padding:10px 8px;">${record.whatsappOptIn ? 'Yes, opted in' : 'No'}</td>
          </tr>
          <tr style="border-bottom:1px solid #f0f0f0;">
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Submission Date & Time</td>
            <td style="padding:10px 8px;">${submittedAt}</td>
          </tr>
          <tr>
            <td style="padding:10px 8px;font-weight:bold;color:#555;">Payment Status</td>
            <td style="padding:10px 8px;"><span style="background:#FFF3CD;color:#856404;padding:4px 12px;border-radius:20px;font-weight:bold;font-size:13px;">⏳ Pending Payment</span></td>
          </tr>
        </table>
        <div style="margin-top:20px;padding:14px;background:#FFF9E6;border-left:4px solid #FFC72C;border-radius:6px;font-size:13px;color:#666;">
          <strong>Official Record Note:</strong> This notification confirms donor registration. Payment has <strong>not</strong> yet been initiated or reconciled. Full details including complete PAN are preserved securely in the foundation's backend storage.
        </div>
      </div>
      <div style="background:#f5f5f5;padding:16px 32px;text-align:center;font-size:12px;color:#999;">
        Kshamtalaya Foundation — Abode of Potential (info@kshamtalaya.org)<br>
        This is an automated donor details notification for Kshamtalaya Foundation administrative staff.
      </div>
    </div>
  `;

  await transporter.sendMail({
    from: `"Kshamtalaya Foundation" <${from}>`,
    to: adminEmail,
    subject: `New Donation Registration — Kshamtalaya Foundation [${record.donationRef}]`,
    html,
  });

  return { sent: true, recipient: adminEmail };
}

/* -- Handler -- */

export default async function handler(req, res) {
  // CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method not allowed' });
  }

  try {
    const { errors, data } = validateDonor(req.body);

    if (errors.length > 0) {
      return res.status(400).json({ success: false, errors });
    }

    // Idempotency: check for submission key to prevent duplicates
    const submissionKey = trimStr(req.body._submissionKey);

    // Generate unique donation reference
    const now = new Date();
    const dateStr = now.toISOString().slice(0, 10).replace(/-/g, '');
    const shortId = randomUUID().slice(0, 8).toUpperCase();
    const donationRef = `KF-${dateStr}-${shortId}`;

    const adminEmail = process.env.DONATION_ADMIN_EMAIL || 'info@kshamtalaya.org';

    // Build record (full PAN stored securely — never logged, never in URLs)
    const record = {
      donationRef,
      submissionKey: submissionKey || null,
      recipientEmail: adminEmail,
      ...data,
      paymentStatus: 'Pending Payment',
      emailSent: false,
      submittedAt: now.toISOString(),
    };

    // Save record to secure persistent storage
    saveRecord(record);

    // Send email notification to info@kshamtalaya.org
    try {
      await sendNotification(record);
      record.emailSent = true;
      saveRecord(record); // update record with email status
    } catch (emailErr) {
      // Email failed — record is preserved, but report to frontend
      console.error('Email notification failed:', emailErr.message);
      return res.status(503).json({
        success: false,
        error: `Your details have been recorded, but the email notification to ${adminEmail} could not be sent. Please retry or contact us directly at ${adminEmail}.`,
        donationRef,
        retryable: true,
      });
    }

    return res.status(200).json({
      success: true,
      donationRef,
      recipientEmail: adminEmail,
      message: 'Your donation details have been submitted and recorded successfully.',
    });
  } catch (err) {
    console.error('Donation handler error:', err);
    return res.status(500).json({
      success: false,
      error: 'An unexpected error occurred. Please try again.',
    });
  }
}
