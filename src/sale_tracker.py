import requests
from bs4 import BeautifulSoup

URL = "https://www.logitechg.com/en-ca/gaming-sale.html"


def main() -> None:
    """Fetch the sale page and print any gaming mice found."""
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:  # pragma: no cover - network errors
        print(f"Error fetching page: {exc}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    for text in soup.stripped_strings:
        if "Gaming Mouse" in text:
            print(text)


if __name__ == "__main__":
    main()

