# extract_title.py
from utils import clean_text

def extract_title(job):
    title_element = job.find("h4", class_="gb-results-list__title").find("strong")
    return clean_text(title_element.text) if title_element else "Título no disponible"
