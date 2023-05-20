import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def get_ted_talks():
    talks = []
    page = 83

    while 82 < page < 166:
        print(f"Scraping page {page}")
        url = f"https://www.ted.com/talks?page={page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all talks on the current page
        talk_elements = soup.find_all("div", class_="media__message")

        # If there are no talks, we've reached the last page and can stop
        if not talk_elements:
            break

        # Otherwise, extract the talk title and link and add them to our list
        for talk_element in talk_elements:
            a_element = talk_element.find("a")
            title = a_element.text.strip()
            link = "https://www.ted.com" + a_element["href"] + "/c"
            talks.append((title, link))

        # Sleep for a bit before we move on to the next page, to avoid overloading the server
        time.sleep(2)

        # Increment the page number
        page += 1

    return talks

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    talks = get_ted_talks()

    # Create a DataFrame from the list of talks
    df = pd.DataFrame(talks, columns=["Title", "Link"])

    # Save the DataFrame to an Excel file
    df.to_excel("ted_talks_3.xlsx", index=False)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
