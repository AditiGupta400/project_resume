import pdfplumber

def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

    return text


def extract_skills(text, skills_list):
    text = text.lower()
    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return list(set(found))