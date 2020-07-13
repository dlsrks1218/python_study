from typing import List, Any

class Book:
    def __init__(self, title: str, authors: List[str], publisher: str, isbn: str, price: float) -> None:
        self.title = title
        # 호출자가 추후 리스트를 수정할 경우를 대비해 저자 리스트를 복사
        self.authors = authors[:]
        self.publisher = publisher
        self.isbn = isbn
        self.price = price

    def num_authors(self) -> int:
        return len(self.authors)

    # 메소드의 재정의 -> 오버라이딩
    def __str__(self) -> str:
        return 'Title : {}, Authors : {}, Price : {}'.format(self.title, ''.join(self.authors), self.price)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Book) and self.isbn == other.isbn

if __name__ == '__main__':
    python_book = Book('Practical Programming', ['캠밸', '그라이스'], '종현', '978-1-6805026-8-8', 20000.0)
    # python_book1 = book.Book('Practical Programming', ['캠밸', '그라이스'], '종현', '978-1-6805026-8-8', 20000.0)
    # python_book2 = book.Book('Practical Programming', ['캠밸', '그라이스'], '종현', '978-1-6805026-8-8', 20000.0)
    
    print(python_book.num_authors())
    print(python_book.title)
    print(python_book.authors)
    print(python_book.__str__())