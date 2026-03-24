import json

# Create dictionary
cities = {
    "Delhi": 19000000,
    "Mumbai": 20000000,
    "Chennai": 11000000
}

# Save to JSON
with open("cities.json", "w") as file:
    json.dump(cities, file)

# Load and print
with open("cities.json", "r") as file:
    data = json.load(file)
    for city, population in data.items():
        print(city, ":", population)

# Add new city
new_city = input("Enter new city: ")
new_pop = int(input("Enter population: "))

data[new_city] = new_pop

# Update JSON
with open("cities.json", "w") as file:
    json.dump(data, file)
