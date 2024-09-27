import requests
import pytest


# verifica starea de raspuns a paginii web
def check_response_status(url):
    response = requests.get(url)
    return response.status_code

url = "https://ursus-breweries.ro/"

check_response_status(url)

def test_response():
    assert check_response_status(url) == 200



# if check_response_status(url) == 200:
#     print("Pagina web este disponibila (200 OK) pentru:", url)
# elif check_response_status(url)== 404:
#     print("Pagina web nu a fost gasita (404 Not Found) pentru:", url)
# else:
#     print("Stare de raspuns neasteptata:", response.status_code, "pentru:", url)



