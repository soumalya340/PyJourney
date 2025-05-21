import requests
import random

# Fetch all countries from REST Countries API
def get_countries():
    url = "https://restcountries.com/v3.1/all"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Find a country by name (case-insensitive)
def find_country(countries, query):
    for country in countries:
        if country["name"]["common"].lower() == query.lower():
            return country
    return None

# Display country details
def display_country(country):
    if country:
        name = country["name"]["common"]
        capital = country["capital"][0] if country["capital"] else "N/A"
        population = country["population"]
        region = country["region"]
        print(f"🌍 Country: {name}")
        print(f"🏛️ Capital: {capital}")
        print(f"👥 Population: {population:,}")
        print(f"🌎 Region: {region}")
    else:
        print("Country not found! Try again.")

# Main function to run the service
def main():
    print("Welcome to the Country Info Service! 😊")
    countries = get_countries()  # Fetch data once
    if not countries:
        print("Sorry, couldn't load country data. Try again later!")
        return

    while True:
        query = input("\nEnter a country name (or 'random' for a random country, 'quit' to exit): ")
        if query.lower() == "quit":
            print("Thanks for using the Country Info Service! 👋")
            break
        elif query.lower() == "random":
            country = random.choice(countries)
        else:
            country = find_country(countries, query)
        display_country(country)

if __name__ == "__main__":
    main()