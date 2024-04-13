import json
from formuls import *

pict = """
MY FIRST SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)

def convert_dict(samply: dict) -> dict:
    a, b, c = samply.values()
    diag_ = diag(a, b, c)
    convert_dicts = {
        "diag": diag_,
        "volume": volume(a, b, c),
        "surface_area": surface_area(a, b, c),
        "alpha": alpha(a, diag_),
        "beta": beta(b, diag_),
        "gamma": gamma(c, diag_),
        "radius_described_sphere": radius_described_sphere(diag_),
        "volume_described_sphere": volume_described_sphere(diag_),
    }
    return convert_dicts

with open('parallelepipeds.json', 'r') as f: 
    data = json.load(f)             
                                    
dict_ = [convert_dict(data[i]) for i in data]

figures_data = {}

for i, dict_data in enumerate(dict_, start=1):
    figure_key = f"figure_{i}"
    figures_data[figure_key] = dict_data

with open('statistics.json', 'w') as file: 
    json.dump(figures_data, file, indent=4)
    
print("Данные для фигур с 1 по 100 были созданы и сохранены в characteristics.json.")
print()

with open('statistics.json', 'r') as file:
    figures_data = json.load(file)


sum_values = {
    "diag": 0,
    "volume": 0,
    "surface_area": 0,
    "alpha": 0,
    "beta": 0,
    "gamma": 0,
    "radius_described_sphere": 0,
    "volume_described_sphere": 0
}


num_figures = len(figures_data)
for figure_data in figures_data.values():
    for key, value in figure_data.items():
        sum_values[key] += float(value) 

average_values = {key: str(sum_value / num_figures) for key, sum_value in sum_values.items()}

for key, value in average_values.items():
    print(f"Среднее значение для {key}: {value}")

with open('statistics.json', 'w') as file: 
    json.dump(average_values, file, indent=4)
print()

print('---------Script END BABY------------')
