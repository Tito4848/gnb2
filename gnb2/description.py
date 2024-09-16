# extract_description.py
from utils import get_soup, clean_text

def extract_description(job):
    details_url = job['href']
    if not details_url.startswith("http"):
        details_url = "https://www.getonbrd.com" + details_url
    
    details_soup = get_soup(details_url)
    job_body_element = details_soup.find("div", id="job-body")
    
    if job_body_element:
        description_parts = job_body_element.find_all("div", class_="gb-rich-txt")
        return "\n\n".join([clean_text(part.get_text()) for part in description_parts])
    return "Descripción no disponible"
