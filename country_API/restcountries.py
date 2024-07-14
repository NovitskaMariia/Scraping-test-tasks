import requests
from tabulate import tabulate


class CountryAPI:
    def __init__(self):
        self.base_url = "https://restcountries.com/v3.1"

    def get_country_data(self, country_name):
        try:
            response = requests.get(f"{self.base_url}/name/{country_name}")
            response.raise_for_status()
            data = response.json()
            country_info = data[0]
            name = country_info["name"]["common"]
            capital = country_info["capital"][0] if "capital" in country_info else "N/A"
            flag_url = country_info["flags"]["png"]

            return {"name": name, "capital": capital, "flag_url": flag_url}
        except requests.RequestException as e:
            print(
                f"Try to enter valid country name in English. \nError fetching data: {e}"
            )
            return None

    def display_country_data(self, country_name):
        country_data = self.get_country_data(country_name)
        if country_data:
            table = [
                [
                    country_data["name"],
                    country_data["capital"],
                    country_data["flag_url"],
                ]
            ]
            headers = ["Country Name", "Capital", "Flag URL"]
            print(tabulate(table, headers, tablefmt="grid"))


if __name__ == "__main__":
    api = CountryAPI()
    country_name = input("Enter the name of the country: ")
    api.display_country_data(country_name)
