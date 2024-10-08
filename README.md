# LINK Academy Software Testing and QA - Lucrarea finală

# Scopul testării:

- Validarea funcționalității website-ului

website-ul Ursus Breweries https://ursus-breweries.ro

# Modalitatea de testare:

## Metode de testare

- Testare funcțională: verificăm funcționalitatea fiecărei părți importante ale site-ului, cum ar fi navigarea, formularele și link-urile.

## Tipuri de testare:

- Black box: Testarea va fi realizată fără a se cunoaște detaliile implementării interne a website-ului.
- Automată: Testarea va fi automatizată folosind instrumente specifice cum ar fi Selenium

## Instrumente de testare:

- Requests: Modul Python pentru a trimite cereri HTTP și a verifica starea paginilor.
- Selenium: Instrument folosit pentru automatizarea acțiunilor în browser, precum navigarea sau completarea formularelor.
- Jupyter Notebook: mediu interactiv de programare folosit pentru a scrie și executa bucăți de cod Python (și alte limbaje) direct în celule, vizualizând rezultatele imediat.
- Unittest și Pytest: Framework-uri de testare pentru rularea testelor automatizate.
- BeautifulSoup (bs4): Bibliotecă pentru extragerea datelor din pagini HTML, utilizată la parsearea codului HTML.
- Asyncio și Aiohttp: Biblioteci ce permit rularea testelor asincrone pentru performanță și eficiență în testarea link-urilor.

## Mediu de testare:

- Web: Testarea va fi realizată pe browser Chrome.
- Desktop: Testarea va fi realizată pe sisteme de operare desktop macOS.

## Test case-uri:

### 1. Testarea protocolului HTTP:

Fisier: "test1_protocol_http_ursus.py"
Tip test: Black box, automat
Instrumente:request, selenium, pytest
Descriere: Testarea va verifica starea de raspuns a paginii principale (coduri de stare HTTP, cum ar fi 200, 404, 500).
Criteriu de succes: cererea HTTP returnează codul de răspuns 200

### 2. Testarea accesarii paginii principale:

Fisier: "test2_content_title_ursus.py"
Tip test: Black box, automat
Instrumente:request, selenium, pytest
Descriere: Testarea va verifica dacă pagina principală se încarcă corect și returnează titlul așteptat.
Criteriu de succes: cererea HTTP returnează titlul corect al paginii pricipale

### 3. Testarea validării formularului de vârstă:

Fisier: "test3_ursus_acces_unittest.py"
Tip test: Black box, automat
Instrumente:request, selenium, unittest
Descriere: Testarea verifica dacă formularul validează corect vârsta utilizatorilor și permite accesul doar celor care au peste 18 ani.
Criteriu de succes: numai utilizatorii cu o vârstă validă au acces.

### 4. Testarea asincrona a tuturor link-urilor:

Fisiere: "sitemap.py", "links.txt", "test4_async_links.py"
Tip test: Black box, automat
Instrumente: requests, selenium, pytest, BeautifulSoup (bs4), asyncio, aiohttp  
Descriere: Testarea identifică și testează toate link-urile de pe site pentru a verifica dacă răspund corect (pasul 1: identificare link-uri; pasul 2: verificare răspunsuri HTTP).
Criteriu de succes: toate cererile HTTP returnează codul de răspuns 200.

### 5. Testarea accesarii paginilor de social media:

Fisier: "test5_socialmedia_pytest.py"
Tip test: Black box, automat
Instrumente: selenium, pytest
Descriere: Testarea verifica dacă link-urile către paginile de social media (Facebook și LinkedIn) funcționează corect.
Criteriu de succes: este accesata corect pagina de login a rețelei sociale.

### 6. Testarea formularului de "Contact":

Fisier: "test6_contact_pytest.py"
Tip test: Black box, automat
Instrumente: selenium, pytest, WebDriverWait, expected_conditions as EC
Descriere: Testarea verifica completarea și trimiterea formularului de contact și afișarea mesajului de confirmare.
Criteriu de succes: Formularul este trimis cu succes și apare mesajul de confirmare.
