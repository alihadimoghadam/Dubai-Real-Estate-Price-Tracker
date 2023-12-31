import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import simpledialog

# Create a tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to input the URL
url = simpledialog.askstring("Input", "Enter the URL of the real estate listings page:")

# Check if the user provided a URL
if url:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract property listings
        listings = soup.find_all('div', class_='property-listing')

        # Iterate through the listings and extract property details
        for listing in listings:
            property_title = listing.find('h2').text.strip()
            property_location = listing.find('span', class_='location').text.strip()
            property_price = listing.find('span', class_='price').text.strip()

            # Print property details (you can store this data in a database)
            print(f'Title: {property_title}')
            print(f'Location: {property_location}')
            print(f'Price: {property_price}')
            print('---')
    else:
        print('Failed to retrieve the web page.')

    # Close the HTTP session
    response.close()
