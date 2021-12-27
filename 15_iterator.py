from typing import Iterable, Iterator


class Page:
    def __init__(self, number: int, text: str) -> None:
        self.number = number
        self.text = text


class Book(Iterable[Page]):
    def __init__(self, pages: Iterable[Page]) -> None:
        self.pages = pages

    def __iter__(self) -> Iterator[Page]:
        return iter(self.pages)


def generate_book(number_of_pages: int) -> Book:
    pages = [Page(i, "...") for i in range(number_of_pages)]
    book = Book(pages)
    return book


book = generate_book(5)

for page in book:
    print(f"Page number: {page.number}")
    print(f"Page text:\n{page.text}")
    print()
