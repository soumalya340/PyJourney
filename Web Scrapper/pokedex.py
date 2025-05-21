import requests

pokemon_name = input("Enter a Pokemon name: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()
    print(f"Name: {pokemon_data['name'].capitalize()}")
    print(f"Height: {pokemon_data['height']} dm")
    print(f"Weight: {pokemon_data['weight']} hg")
    print("Abilities:")
    for ability in pokemon_data['abilities']:
        print(f"- {ability['ability']['name'].capitalize()}")
else:
    print(f"Pokemon '{pokemon_name}' not found.")
