
# Input list of city names
city_names = ["Zurich", "New York", "Tokyo", "Dubai", "Kuala lumpur"]

# sort list using lambda function

sorted_city_names = sorted(city_names, key=lambda x: x)

print("Sorted city names: ", sorted_city_names)
