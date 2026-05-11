import json

# Initial dictionary
cities = {
    "Delhi": 32000000,
    "Mumbai": 21000000,
    "Bangalore": 13000000
}

# Save dictionary to JSON file
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

# Load and display data
print("\nCity Populations:")

with open("cities.json", "r") as file:
    data = json.load(file)

    for city, population in data.items():
        print(city, ":", population)

# Add new city
new_city = input("\nEnter new city name: ")
new_population = int(input("Enter population: "))

data[new_city] = new_population

# Update JSON file
with open("cities.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully!")
