import glob
import os

def replace_em_dash():
    folder = r"c:\Users\Saurav\Desktop\Kshamatalaya"
    html_files = glob.glob(os.path.join(folder, "*.html"))
    
    for filepath in html_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
                
        if '—' in content:
            # Replace em dash with standard hyphen
            new_content = content.replace('—', '-')
            
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
            except Exception:
                with open(filepath, 'w', encoding='latin-1') as f:
                    f.write(new_content)
            print(f"Replaced em-dash in {os.path.basename(filepath)}")

if __name__ == "__main__":
    replace_em_dash()
