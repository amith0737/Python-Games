import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    """Fetch and parse data from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def extract_headlines(soup):
    """Extract headlines and their links from the parsed HTML."""
    headlines = []
    for item in soup.find_all('h3'):  # Assuming headlines are in <h3> tags
        title = item.get_text(strip=True)
        link = item.find('a')['href'] if item.find('a') else None
        if title and link:
            headlines.append((title, link))
    return headlines

def display_headlines(headlines):
    """Display extracted headlines in a user-friendly format."""
    if not headlines:
        print("No headlines found.")
        return
    print("\n--- Latest Headlines ---")
    for idx, (title, link) in enumerate(headlines, start=1):
        print(f"{idx}. {title}")
        print(f"   Link: {link}\n")

def interactive_web_scraper():
    """Main interactive web scraping function."""
    print("Welcome to the Interactive Web Scraper!")
    print("Example URL: https://www.bbc.com/news")
    url = input("Enter the URL of the website to scrape: ").strip()

    if not url:
        print("URL cannot be empty.")
        return

    print("Fetching data...")
    soup = fetch_data(url)
    if not soup:
        return

    headlines = extract_headlines(soup)
    display_headlines(headlines)

# Run the program
if __name__ == "__main__":
    interactive_web_scraper()
