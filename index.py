## System Imports
import os


## Application Imports


## Library Imports
import json


def get_categories():
	categories = []
	
	dir_list = os.listdir()
	
	for i in dir_list:
		if os.path.isdir(i):
			if '.' not in i:
				categories.append(i)
	
	return categories


def generate_index():
	categories = get_categories()
	
	packages_categories = {cat: [] for cat in categories}
	
	for category in categories:
		packages = []
		
		dir_list = os.listdir(category)
		
		for i in dir_list:
			if os.path.isdir(f'{category}/{i}'):
				if '.' not in i:
					packages.append(i)
		
		for package in packages:
			packages_categories[category].append(package)
	
	return packages_categories


def generate_json_file():
	packages_index = generate_index()
	
	return json.dumps(packages_index, indent=4)


if __name__ == '__main__':
	
	print('Generating Packages Index')
	packages_index_file = generate_json_file()
	
	with open('packages_index.json', 'w') as f:
		f.write(packages_index_file)
