import json, pandas as pd, pdfplumber
from docx import Document

def load_txt(file): return file.read().decode()

def load_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

def load_docx(file): return "\n".join([p.text for p in Document(file).paragraphs])

def load_csv(file): return pd.read_csv(file).to_string(index=False)

def load_json(file): return json.dumps(json.load(file), indent=2)

def read_file(file):
    file_type = file.name.split('.')[-1].lower()
    match file_type:
        case 'txt': return load_txt(file)
        case 'pdf': return load_pdf(file)
        case 'docx': return load_docx(file)
        case 'csv': return load_csv(file)
        case 'json': return load_json(file)
        case _: return None
