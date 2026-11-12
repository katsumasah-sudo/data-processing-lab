import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

cities = []
with open(os.path.join(__location__, "Cities.csv")) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


# --- นิยามฟังก์ชันตามโจทย์ ---
def filter_items(condition, dict_list):
    """Return a new list containing only the dictionaries that satisfy

    the given condition function.
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """Aggregate values associated with aggregation_key using the

    provided aggregation function.
    """
    values = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(values)


# --- ใช้สองฟังก์ชันนี้ทำตามโจทย์ ---

# 1. Print the average temperature of all the cities
avg_temp = aggregate(
    "temperature", lambda temps: sum(temps) / len(temps), cities
)
print("Average temperature of all cities:", avg_temp)
print()

# 2. Print all cities in Germany
germany_cities = filter_items(lambda c: c["country"] == "Germany", cities)
print("All cities in Germany:")
for city in germany_cities:
    print(city)
print()

# 3. Print all cities in Spain with a temperature above 12°C
spain_warm_cities = filter_items(
    lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12, cities
)
print("All cities in Spain with a temperature above 12°C:")
for city in spain_warm_cities:
    print(city)
print()

# 4. Count the number of unique countries
unique_countries = {c["country"] for c in cities}
print("Number of unique countries:", len(unique_countries))
print()

# 5. Print the average temperature for all the cities in Germany
ger_cities = filter_items(lambda c: c["country"] == "Germany", cities)
ger_avg_temp = aggregate(
    "temperature", lambda temps: sum(temps) / len(temps), ger_cities
)
print("Average temperature for all cities in Germany:", ger_avg_temp)
print()

# 6. Print the max temperature for all the cities in Italy
it_cities = filter_items(lambda c: c["country"] == "Italy", cities)
it_max_temp = aggregate("temperature", max, it_cities)
print("Max temperature for all cities in Italy:", it_max_temp)
print()
