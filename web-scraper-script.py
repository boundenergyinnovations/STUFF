import requests
from bs4 import BeautifulSoup
import sys

def scrape_links(url, output_file):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all 'a' elements in the body
        body = soup.body
        links = body.find_all('a')

        # Open the output file
        with open(output_file, 'w') as f:
            # Write each link to the file
            for link in links:
                href = link.get('href')
                if href:
                    f.write(href + '\n')

        print(f"Links have been written to {output_file}")

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <output_file>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]
    scrape_links(url, output_file)
