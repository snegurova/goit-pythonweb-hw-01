"""Module providing library implementation"""
from abc import ABC, abstractmethod
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Book:
    """Class implementing saving information about the book"""

    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    """Interface representing methods with books"""

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """Method adding book to a library"""

    @abstractmethod
    def remove_book(self, title: str) -> None:
        """Method removing book from a library"""

    @abstractmethod
    def get_all_books(self) -> List[Book]:
        """Method retuning library books list"""

class Library(LibraryInterface):
    """Library class implementation"""

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info("Book added: %s", book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logger.info("Book removed: %s", book)
                return
        logger.info("Book with title '%s' not found.", title)

    def get_all_books(self) -> List[Book]:
        return self.books


class LibraryManager:
    """Class implementing user library interaction"""

    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        """Method creating book and adding it to the library"""
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        """Method deleting book by name"""
        self.library.remove_book(title)

    def show_books(self) -> None:
        """Method providing library books list"""
        books = self.library.get_all_books()
        if books:
            for book in books:
                logger.info("%s", book)
        else:
            logger.info("Library is empty.")

def main() -> None:
    """Function processing CLI commands"""
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
