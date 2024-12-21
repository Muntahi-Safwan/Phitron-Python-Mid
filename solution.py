class Library:
    book_list = []

    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)


class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"'{self.__title}' has been borrowed.")
        else:
            print(f"'{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"'{self.__title}' has been returned.")
        else:
            print(f"'{self.__title}' is not borrowed.")

    def view_book_info(self):
        if self.__availability:
            print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Status: : Available")
        else:
            print(f"Book ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, Status: : Borrowed")
        

    def get_book_id(self):
        return self.__book_id

    def is_available(self):
        return self.__availability


def menu():
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("-----------All Books:----------")
            for book in Library.book_list:
                book.view_book_info()

        elif choice == "2":
            book_id = input("Enter the book ID to borrow: ")
            book = next((b for b in Library.book_list if b.get_book_id() == book_id), None)
            if book:
                book.borrow_book()
            else:
                print("Invalid Book ID.")

        elif choice == "3":
            book_id = input("Book ID : ")
            found = False
            for book in Library.book_list:
                if book.get_book_id == book_id:
                    found = True
            if found:
                book.return_book()
            else:
                print("Invalid Book ID.")

        elif choice == "4":
            print("Exit!")
            break

        else:
            print("Invalid Option")



