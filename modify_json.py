import json

# Path to the JSON file
file_path = '/home/simon/Projects/simon/ColorPalette/color_ggsci.json'

# Load the JSON data
with open(file_path, 'r') as f:
    data = json.load(f)

# Transform each palette: convert dict values to list
for palette in data:
    if isinstance(data[palette], dict):
        data[palette] = list(data[palette].values())

# Save the modified JSON back to the file
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2)
