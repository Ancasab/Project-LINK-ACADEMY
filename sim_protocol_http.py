import requests

# Functie pentru a verifica starea de raspuns a unei pagini web
def check_response_status(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Pagina web este disponibila (200 OK) pentru:", url)
    elif response.status_code == 404:
        print("Pagina web nu a fost gasita (404 Not Found) pentru:", url)
    else:
        print("Stare de raspuns neasteptata:", response.status_code, "pentru:", url)


check_response_status("https://www.sheismomclub.com")