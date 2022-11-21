import scraper_sub
if __name__ == "__main__":
    seed_url = "http://books.toscrape.com/catalogue/page-{}.html"
    print("Initiating Web-Scraping")
    result = scraper_sub.browse_and_scrape(seed_url)
    if result == True:
        print("Web-Scraping complete!")
    else:
        print(f"Oops, That doesn't seem right! - {result}")
