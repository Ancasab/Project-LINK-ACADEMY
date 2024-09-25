# Lucrarea finală la LINK Academy Software Testing and QA

Plan de testare pentru website-ul Ursus Breweries
https://ursus-breweries.ro

## Scopul testării:

Validarea funcționalității website-ului
Testarea ușurinței de utilizare (usability)

## Modalitatea de testare:

Testare funcțională: verificăm funcționalitatea fiecărei părți esențiale ale site-ului, cum ar fi navigarea, formularele și link-urile.
Testare de ușurință de utilizare (Usability): ne asigurăm că website-ul este ușor de utilizat pentru utilizatori de toate nivelurile.

Black box: Testarea va fi realizată fără a se cunoaște detaliile implementării interne a website-ului.
Automată: Testarea va fi automatizată folosind instrumente specifice cum ar fi Selenium
Manuală: Testarea manuală va fi utilizată pentru a completa testarea automată și a verifica aspecte specifice care nu pot fi automatizate.

## Instrumente de testare:

- Requests: Modul Python pentru a trimite cereri HTTP și a verifica starea paginilor.
- Selenium: Folosit pentru automatizarea acțiunilor în browser, precum navigarea sau completarea formularelor.
- Unittest și Pytest: Framework-uri de testare pentru rularea testelor automatizate.
- BeautifulSoup (bs4): Bibliotecă pentru extragerea datelor din pagini HTML, utilizată la parsearea codului HTML.
- Asyncio și Aiohttp: Permite rularea testelor asincrone pentru performanță și eficiență în testarea link-urilor.

## Mediu de testare:

Web: Testarea va fi realizată pe browser Chrome.
Desktop: Testarea va fi realizată pe sisteme de operare desktop macOS.

## Rolul testerului:

Utilizator: Testarea va fi realizată din perspectiva unui utilizator obișnuit al website-ului.

Tester / Dezvoltator: Testarea va fi realizată de către testeri/dezvoltatori pentru a identifica și remedia problemele legate de cod.

## Test case-uri:

1. Testarea protocolului HTTP:

Fisier: "test1_protocol_http_ursus.py"
Tip test: Black box, automat
Instrumente:request, selenium, pytest
Descriere: Testarea va verifica starea de raspuns a paginii principale (coduri de stare HTTP, cum ar fi 200, 404, 500).
Criterii de succes: toate cererile HTTP returnează codul de răspuns 200

2. Testarea accesarii paginii principale:

Fisier: "test2_content_title_ursus.py"
Tip test: Black box, automat
Instrumente:request, selenium, pytest
Descriere: Testarea va verifica incarcarea paginii principale prin verificarea titlului paginii

3. Testarea funcționalității de acces la continutul site-ului ( conditie de varsta > 18 ani):

Fisier: "test3_ursus_acces_unittest.py"
Tip test: Black box, automat
Instrumente:request, selenium, unittest, WebDriverWait, expected_conditions as EC
Descriere: Testarea va verifica accesul in jurul limitelor intervalului de varsta la data curenta - an, luna, zi. Testăm dacă formularul de introducere a datei de naștere validează corect datele și permite accesul doar utilizatorilor majori.

4. Testarea asincrona a funcționarii tuturor link-urilor din site:

Fisiere: "sitemap.py", "links.txt", "test4_async_links.py"
Tip test: Black box, automat
Instrumente: selenium, pytest, BeautifulSoup (bs4), asyncio, aiohttp  
Descriere: Testarea va verifica daca toate link-urile site-utlui functioneaza. Testarea decurge in 2 pasi. Pasul 1: identificarea tuturor link-urilor site-ului si salvarea lor intr-un fisier .txt. Pasul2: citirea fiecarui link si testarea starii de raspuns a fiecarei pagini web.

5. Testarea accesarii paginilor de social media (fb & in):

Fisier: "test5_socialmedia_pytest.py"
Tip test: Black box, automat
Instrumente: selenium, pytest
Descriere: Testarea va verifica lansarea paginii de facebook si respective Linkedin prin actionarea iconitelor de social media

6. Testarea formularului de "Contact":

Fisier: "test6_contact_pytest.py"
Tip test: Black box, automat
Instrumente: selenium, pytest, WebDriverWait, expected_conditions as EC
Descriere: Testarea va verifica accesarea sectiunii "Contact" si completarea formuralui on-line disponibil.
