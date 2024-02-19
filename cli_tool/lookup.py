import requests
import json
import argparse
import os

def get_country_name(country_code, data):
    return data['data'].get(country_code, {}).get('name', 'Country not found')

def lookup_country_codes(country_codes, data):
    result = {}
    for code in country_codes:
        country_name = get_country_name(code, data)
        result[code] = country_name
    return result

def save_to_file(data, filename='data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def read_from_file(filename='data.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Generating the file.")
        return None

def fetch_data_and_save(filename='data.json'):
    url = 'https://www.travel-advisory.info/api'
    response = requests.get(url)
    data = response.json()
    save_to_file(data, filename)
    return data

def main():
    parser = argparse.ArgumentParser(description='Country Code Lookup CLI')
    parser.add_argument('--countryCodes', nargs='+', help='List of country codes to look up', required=True)
    parser.add_argument('--file', help='JSON file to read from or write to', default='data.json')
    args = parser.parse_args()

    data = read_from_file(args.file)

    if data is None:
        data = fetch_data_and_save(args.file)

    result = lookup_country_codes(args.countryCodes, data)
    print("Results:")
    for code, name in result.items():
        print(f"{code}: {name}")

if __name__ == '__main__':
    main()

