class Book:
    """Класс для представления книги в библиотечной системе.
    
    Атрибуты:
        id_ (int): Уникальный идентификатор книги
        name (str): Название книги
        pages (int): Количество страниц в книге
    """
    
    def __init__(self, id_: int, name: str, pages: int):
        """Инициализирует экземпляр класса Book.
        
        Args:
            id_: Уникальный идентификатор книги (положительное целое число)
            name: Название книги (строка)
            pages: Количество страниц (положительное целое число)
            
        Raises:
            ValueError: Если id_ или pages не являются положительными целыми числами
            TypeError: Если name не является строкой
        """
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным целым числом")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление книги."""
        return f'Книга "{self.name}" (ID: {self.id_}, {self.pages} стр.)'

    def __repr__(self) -> str:
        """Возвращает однозначное строковое представление книги для разработчиков."""
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"
    
    def get_info(self) -> dict:
        """Возвращает информацию о книге в виде словаря.
        
        Returns:
            dict: Словарь с информацией о книге
        """
        return {
            'id': self.id_,
            'name': self.name,
            'pages': self.pages
        }


if __name__ == '__main__':
    # Тестовые данные
    BOOKS_DATABASE = [
        {
            "id": 1,
            "name": "Гарри Поттер и Философский камень",
            "pages": 400,
        },
        {
            "id": 2,
            "name": "Властелин Колец: Братство Кольца",
            "pages": 600,
        }
    ]
    
    # Создаем список книг
    library = [
        Book(id_=book["id"], name=book["name"], pages=book["pages"]) 
        for book in BOOKS_DATABASE
    ]

    # Демонстрация работы методов
    print("\nИнформация о книгах:")
    for book in library:
        print(book)  
    
    print("\nДля разработчиков:")
    print(library) 
    
    print("\nПолная информация:")
    for book in library:
        print(book.get_info())
    
    # Тест обработки ошибок
    print("\nТест обработки ошибок:")
    try:
        invalid_book = Book(id_=-1, name="Некорректная книга", pages=100)
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    try:
        invalid_book = Book(id_=3, name=123, pages=100)
    except TypeError as e:
        print(f"Ошибка: {e}")
