import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)


class Table:

    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        """Return a new Table containing only rows that satisfy the condition."""
        filtered_data = [item for item in self.data if condition(item)]
        return Table(filtered_data)

    def aggregate(self, aggregation_key, aggregation_function):
        """Aggregate values associated with aggregation_key."""
        values = [float(item[aggregation_key]) for item in self.data]
        return aggregation_function(values)

    def __str__(self):
        return f"Table with {len(self.data)} rows"


class DataLoader:

    @staticmethod
    def load_csv(filepath):
        """Load CSV file and return a Table object."""
        data = []
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                data.append(dict(r))
        return Table(data)


# --- ใช้งานคลาสตามโจทย์ ---

# โหลดข้อมูลผ่าน DataLoader
file_path = os.path.join(__location__, "Cities.csv")
cities_table = DataLoader.load_csv(file_path)

# 1. Print the average temperature of all the cities
avg_temp = cities_table.aggregate(
    "temperature", lambda temps: sum(temps) / len(temps)
)
print("Average temperature of all cities:", avg_temp)
print()

# 2. Print all cities in Germany
germany_table = cities_table.filter(lambda c: c["country"] == "Germany")
print("All cities in Germany:")
for city in germany_table.data:
    print(city)
print()

# 3. Print all cities in Spain with a temperature above 12°C
spain_warm_table = cities_table.filter(
    lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12
)
print("All cities in Spain with a temperature above 12°C:")
for city in spain_warm_table.data:
    print(city)
print()

# 4. Count the number of unique countries
unique_countries = {c["country"] for c in cities_table.data}
print("Number of unique countries:", len(unique_countries))
print()

# 5. Print the average temperature for all the cities in Germany
ger_avg_temp = germany_table.aggregate(
    "temperature", lambda temps: sum(temps) / len(temps)
)
print("Average temperature for all cities in Germany:", ger_avg_temp)
print()

# 6. Print the max temperature for all the cities in Italy
italy_table = cities_table.filter(lambda c: c["country"] == "Italy")
it_max_temp = italy_table.aggregate("temperature", max)
print("Max temperature for all cities in Italy:", it_max_temp)
print()
