# extract_location.py
def extract_location(job):
    location_element = job.find("span", class_="location")
    if location_element:
        location_text = location_element.get_text(separator="\n", strip=True)
        return location_text.split('\n')[0].strip() if location_text else "Ubicación no disponible"
    return "Ubicación no disponible"
