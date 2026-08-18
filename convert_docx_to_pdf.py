import os
import win32com.client
import glob

def convert_to_pdf(folder_path):
    word = win32com.client.Dispatch('Word.Application')
    word.Visible = False
    
    try:
        # Find all docx files in the folder
        search_path = os.path.join(folder_path, '*.docx')
        for docx_file in glob.glob(search_path):
            if not docx_file.startswith('~'): # Ignore temporary files
                pdf_file = docx_file.rsplit('.', 1)[0] + '.pdf'
                print(f'Converting {docx_file} to {pdf_file}')
                
                doc = word.Documents.Open(os.path.abspath(docx_file))
                doc.SaveAs(os.path.abspath(pdf_file), FileFormat=17) # 17 = wdFormatPDF
                doc.Close()
                
    finally:
        word.Quit()

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    policies_dir = os.path.join(current_dir, 'Policies')
    convert_to_pdf(policies_dir)
