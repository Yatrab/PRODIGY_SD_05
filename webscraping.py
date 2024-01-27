import requests
from bs4 import BeautifulSoup
import csv

# URL of the page to scrape (replace with the Myntra URL you want)
url = 'https://www.example.com/products'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create a CSV file to store the data
    with open('product_data.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Find and extract product information
        product_elements = soup.find_all('div', class_='product')
        for product in product_elements:
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            rating = product.find('span', class_='product-rating').text.strip()

            # Write the data to the CSV file
            writer.writerow({'Name': name, 'Price': price, 'Rating': rating})

    print("Scraping and data extraction completed. Data saved to 'product_data.csv'.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)