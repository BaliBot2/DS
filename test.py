import csv
import requests
from bs4 import BeautifulSoup

def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = soup.find_all(class_="_s30J clearfix")
        all_text = ' '.join(element.get_text(separator=' ', strip=True) for element in elements)
        return all_text
    except requests.RequestException as e:
        print(f"Failed to retrieve the webpage from {url}: {e}")
        return ""

def process_links(csv_input, csv_output):
    with open(csv_input, mode='r', newline='', encoding='utf-8') as infile, \
         open(csv_output, mode='w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=['Title', 'Date', 'Text'])
        writer.writeheader()
        
        for row in reader:
            print(f"Processing {row['Title']}...")
            text = fetch_and_parse(row['URL'])
            writer.writerow({'Title': row['Title'], 'Date': row['Date'], 'Text': text})

# Usage
input_csv = 'Farmers1.csv'
output_csv = 'test2.csv'
process_links(input_csv, output_csv)
