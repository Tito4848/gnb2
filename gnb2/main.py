# main.py

# Importamos las bibliotecas y módulos necesarios
import pandas as pd  # Para manipular y guardar datos en un archivo CSV
from joblist import get_job_listings  # Función para obtener la lista de ofertas de trabajo
from title import extract_title  # Función para extraer el título del trabajo
from company import extract_company  # Función para extraer el nombre de la compañía
from location import extract_location  # Función para extraer la ubicación del trabajo
from description import extract_description  # Función para extraer la descripción del trabajo


# Función principal que controla el flujo de la aplicación
def main():
    url = "https://www.getonbrd.com/"
    joblist = get_job_listings(url)  # Llamamos a la función para obtener la lista de trabajos desde la URL

    jobs = []  # Lista para almacenar los datos de los trabajos
    for job in joblist:  # Iteramos a través de la lista de trabajos obtenida
        # Para cada trabajo, extraemos los datos relevantes y los guardamos en un diccionario
        job_data = {
            "Título": extract_title(job),  # Extraer el título del trabajo
            "Compañía": extract_company(job),  # Extraer la compañía que ofrece el trabajo
            "Ubicación": extract_location(job),  # Extraer la ubicación del trabajo
            "Descripción": extract_description(job)  # Extraer una breve descripción del trabajo
        }
        jobs.append(job_data)  # Añadimos el diccionario con los datos del trabajo a la lista de trabajos

    # Convertimos la lista de trabajos en un DataFrame de pandas
    df = pd.DataFrame(jobs)
    # Guardamos el DataFrame en un archivo CSV
    df.to_csv("trabajos.csv", index=False)
    print("Datos exportados a trabajos.csv")


# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()
