from abc import ABC, abstractmethod
from typing import Any
from json import dumps


class Scraper(ABC):
    @abstractmethod
    def run(self, product_id: str) -> dict[Any, Any]:
        raise NotImplementedError

    @abstractmethod
    def to_csv(self, data: dict[Any, Any]) -> str:
        raise NotImplementedError

    def to_json(self, data: dict[Any, Any]) -> str:
        return dumps(data)

    def send_mail(self, data: str, email: str) -> None:
        print(f"Sending\n'{data}'\nto {email}")


class AmazonScraper(Scraper):
    def run(self, product_id: str) -> dict[str, float]:
        print(f"Scraping data for product {product_id}")
        data: dict[str, float] = {"price": 10}
        return data

    def to_csv(self, data: dict[str, float]) -> str:
        print(f"Transforming {data} in CSV")
        return f"price\n{data.get('price')}"


class WalmartScraper(Scraper):
    def run(self, product_id: str) -> dict[str, dict[str, float]]:
        print(f"Scraping data for product {product_id}")
        data: dict[str, dict[str, float]] = {product_id: {"price": 12}}
        return data

    def to_csv(self, data: dict[str, dict[str, float]]) -> str:
        print(f"Transforming {data} in CSV")
        price = tuple(data.values())[0].get("price")
        return f"price\n{price}"


if __name__ == "__main__":
    amazon_scraper = AmazonScraper()
    walmart_scraper = WalmartScraper()
    amazon_data = amazon_scraper.run("123")
    csv = amazon_scraper.to_csv(amazon_data)
    amazon_scraper.send_mail(csv, "user@domain.com")
    print()
    walmart_data = walmart_scraper.run("123")
    json = walmart_scraper.to_csv(walmart_data)
    walmart_scraper.send_mail(json, "user@domain.com")
