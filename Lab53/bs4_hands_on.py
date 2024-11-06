from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, html) -> None:
        self.soup = BeautifulSoup(html, 'html.parser')

    def get_countries_details(self):
        countries_details = []
        try:
            countries_section = self.soup.find(id="countries")
            countries_container = countries_section.find(class_="container")
            countries_divs =  countries_container.find_all(class_="row country")

            for cd in countries_divs:
                country_details = list()
                # get country name
                country_name = cd.find('h3').text.strip().lower()
                country_details.append(country_name)
                # get other details
                span_details = cd.select('.country-info span')[1:]
                other_details =[span.text for span in span_details]
                country_details.extend(other_details)
                countries_details.append(country_details)


            return countries_details
        except Exception as e:
            print(f'Error: {e}')
            exit()

    def save_to_db(self):
        # table country
        # id | Name | Capital | Population | Area

        country_details = self.get_countries_details()
        print(country_details)


if __name__=='__main__':
    with open('./index.html') as f:
        html = f.read()

    scraper = Scraper(html)
    scraper.save_to_db()