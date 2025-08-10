from book_class import Book
from library_system import EBook, PrintBook, Library

def main():
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813)
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 1992, 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 1951, 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    my_library.list_books()

if __name__ == "__main__":
    main()
