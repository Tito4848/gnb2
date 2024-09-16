# extract_company.py
from utils import clean_text

def extract_company(job):
    company_element = job.find("div", class_="size0").find("strong")
    return clean_text(company_element.text) if company_element else "Compañía no disponible"
