import requests
import time
from bs4 import BeautifulSoup

def get_links():
    sitemap_url = "https://ursus-breweries.ro/wp-sitemap.xml"

    response = requests.get(sitemap_url)

    soup = BeautifulSoup(response.content, "xml")
    locations = soup.find_all("loc")

    xml_locations = [l.text for l in locations]
    print("The number of location is: ", len(xml_locations), xml_locations)

    all_xml_links =[]

    for xml in xml_locations:
        xml_response = requests.get(xml)
        xml_soup = BeautifulSoup(xml_response.content, "xml")
        xml_links = xml_soup.find_all("loc")
        inner_xml_locations = [l.text for l in xml_links]
        all_xml_links.extend(inner_xml_locations)

    return all_xml_links


if __name__ == "__main__":
    all_links = get_links()
    print("Ursus Breweries site has", len(all_links), "links")
    with open("links.txt", "w") as fwriter:
        for l in all_links:
            fwriter.write(f"{l}\n")
        