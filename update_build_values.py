import re

# Update build_values.py
values_file = "build_values.py"
with open(values_file, "r", encoding="utf-8") as f:
    content = f.read()

new_values = '''values = [
    {
        "num": "1",
        "title": "करुणा Compassion",
        "quote": '"We recognise difficulty, treat it as universal, and act on it with care."',
        "text": "We recognise difficulty, treat it as universal, and act on it with care.",
        "color": "#08B9DB",
        "light": "rgba(8, 185, 219, 0.1)",
        "icon": "M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
    },
    {
        "num": "2",
        "title": "विश्वास Trust",
        "quote": '"We are transparent about our processes and treat mistakes as places to learn."',
        "text": "We are transparent about our processes and treat mistakes as places to learn.",
        "color": "#F2994A",
        "light": "rgba(242, 153, 74, 0.1)",
        "icon": "M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"
    },
    {
        "num": "3",
        "title": "उत्कृष्टता Excellence",
        "quote": '"We hold a high standard and improve it deliberately, year on year."',
        "text": "We hold a high standard and improve it deliberately, year on year.",
        "color": "#6DBE45",
        "light": "rgba(109, 190, 69, 0.1)",
        "icon": "M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
    },
    {
        "num": "4",
        "title": "स्वतंत्रता Freedom with responsibility",
        "quote": '"Our teams make their own decisions and own what follows."',
        "text": "Our teams make their own decisions and own what follows.",
        "color": "#FF6F59",
        "light": "rgba(255, 111, 89, 0.1)",
        "icon": "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
    },
    {
        "num": "5",
        "title": "नवाचार Innovation",
        "quote": '"We test, adapt and discard. The model came from reflection, not a plan."',
        "text": "We test, adapt and discard. The model came from reflection, not a plan.",
        "color": "#9B51E0",
        "light": "rgba(155, 81, 224, 0.1)",
        "icon": "M9 3v2m6-2v2M9 19v2m6-2v2M5 9H3m2 6H3m18-6h-2m2 6h-2M7 19h10a2 2 0 002-2V7a2 2 0 00-2-2H7a2 2 0 00-2 2v10a2 2 0 002 2z"
    }
]'''
content = re.sub(r'values = \[.*?\]\n', new_values + '\n', content, flags=re.DOTALL)
with open(values_file, "w", encoding="utf-8") as f:
    f.write(content)
print("build_values.py updated!")
