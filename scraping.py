import requests
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

os.system("clear")

print("")

print("\33[34m ██     ██ ███████ ██████      ███████  ██████ ██████   █████  ██████  ██ ███    ██  ██████   \033[0m")
print("\33[34m ██     ██ ██      ██   ██     ██      ██      ██   ██ ██   ██ ██   ██ ██ ████   ██ ██        \033[0m")
print("\33[34m ██  █  ██ █████   ██████      ███████ ██      ██████  ███████ ██████  ██ ██ ██  ██ ██   ███  \033[0m")
print("\33[34m ██ ███ ██ ██      ██   ██          ██ ██      ██   ██ ██   ██ ██      ██ ██  ██ ██ ██    ██  \033[0m")
print("\33[34m  ███ ███  ███████ ██████      ███████  ██████ ██   ██ ██   ██ ██      ██ ██   ████  ██████   \033[0m")
                                                                                                                                                                              
print("")

def menu_principal():
    while True:
        print("  [1] Metodo 1")
        print("  [2] Metodo 2")
        print("  [3] Metodo 3")
        print("  [4] Salir")
        opcion = input("\033[1m\n[+] Ingrese una opción: \033[0m")
        if opcion == "":
            print("\033[1m\n[+] Por favor ingrese una opción: \033[0m")
        elif opcion == "1":
            menu1()
        elif opcion == "2":
            menu2()
        elif opcion == "3":
            menu3()
        elif opcion == "4":
            break


def menu1():
    while True:
        url = input("\033[1m\n[+] Ingrese la URL: \033[0m")
        sesion = requests.Session()
        sesion.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        html = sesion.get(url).content
        sopa = bs(html, "html.parser")
        archivos_de_script = []
        for script in sopa.find_all("script"):
            if script.attrs.get("src"):
                url_script = urljoin(url, script.attrs.get("src"))
                archivos_de_script.append(url_script)
                archivos_de_css = []
        for css in sopa.find_all("link"):
            if css.attrs.get("href"):
                url_css = urljoin(url, css.attrs.get("href"))
                archivos_de_css.append(url_css)
                
        # Abrir y escribir archivos
        with open("javascript.txt", "w") as f:
            for archivo_js in archivos_de_script:
                print(archivo_js, file=f)
        with open("css.txt", "w") as f:
            for archivo_css in archivos_de_css:
                print(archivo_css, file=f)
                
        print("Total de archivos de script en la página:", len(archivos_de_script))
        print("Total de archivos CSS en la página:", len(archivos_de_css))


def menu2():
    while True:
        # Obtener la URL del usuario
        url = input("Ingrese la URL: ")
        try:
            # Obtener la respuesta del servidor
            response = requests.get(url)
            if response.status_code == 200:
                # Si la URL es accesible, imprimir un mensaje en pantalla
                print(f"La URL {url} está disponible.")
            else:
                # Si la URL no es accesible, imprimir un mensaje en pantalla con el código de estado HTTP
                print(f"La URL {url} no está disponible. Código de estado HTTP: {response.status_code}")
            # Obtener el título y los enlaces de la página utilizando BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            title = soup.title.text
            links = "\n[+] ".join([link.get("href") for link in soup.find_all("a")])
            # Crear el nombre del archivo utilizando la URL
            file_name = url.replace("http://", "").replace("https://", "").replace(".", "_").replace("/", "_") + ".txt"
            # Guardar el título y los enlaces en el archivo
            with open(file_name, "w+") as f:
                f.write(f"Título: {title}\n\nEnlaces:\n[+] + {links}")
            # Imprimir el título y los enlaces en pantalla
            print(f"Título: {title}")
            print("Enlaces:")
            print(links)
        except requests.exceptions.RequestException as e:
            # Si ocurre un error al intentar acceder a la URL, imprimir un mensaje de error en pantalla
            print(f"No se pudo acceder a la URL {url}: {e}")


def menu3():
    while True:
        # Definir la URL de la página a analizar
        url = input("Ingrese la URL: ")
        # Obtener el contenido HTML de la página
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Encontrar todos los elementos 'a' que contienen la etiqueta 'href'
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
            # Imprimir todos los enlaces encontrados en el archivo y en la consola
        filename = os.path.basename(url) + '.txt'
        with open(filename, 'w+') as f:
            for link in links:
                print("[+] " + link, file=f)
                print("[+] " + link)
                print("La salida se ha guardado en el archivo", filename)

menu_principal()
