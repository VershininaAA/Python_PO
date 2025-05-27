from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

class SocialNetwork(ABC):
    """Абстрактный базовый класс для социальных сетей."""
    
    def __init__(self, name: str, users_count: int):
        """
        Инициализирует социальную сеть.
        
        Args:
            name: Название социальной сети
            users_count: Количество пользователей
        """
        self._name = name
        self._users_count = users_count
        self._messages_sent = 0
        self._active = True

    @property
    def name(self) -> str:
        """Возвращает название социальной сети."""
        return self._name

    @property
    def users_count(self) -> int:
        """Возвращает количество пользователей."""
        return self._users_count

    @property
    def is_active(self) -> bool:
        """Проверяет, активна ли социальная сеть."""
        return self._active

    def send_message(self, recipient: str, message: str) -> bool:
        """
        Отправляет сообщение пользователю.
        
        Args:
            recipient: Получатель сообщения
            message: Текст сообщения
            
        Returns:
            bool: True если сообщение отправлено успешно
        """
        if not self._active:
            print(f"{self._name} недоступна для отправки сообщений")
            return False
            
        if recipient and message:
            self._messages_sent += 1
            print(f"[{self._name}] Сообщение для {recipient}: {message}")
            return True
        return False

    def get_messages_sent(self) -> int:
        """Возвращает количество отправленных сообщений."""
        return self._messages_sent

    @abstractmethod
    def get_features(self) -> List[str]:
        """Возвращает список особенностей социальной сети."""
        pass

    def __str__(self) -> str:
        return f"{self._name} (пользователей: {self._users_count:,})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, users_count={self._users_count})"

@dataclass
class Channel:
    """Класс для представления канала в социальной сети."""
    name: str
    subscribers: int = 0
    is_verified: bool = False

class Telegram(SocialNetwork):
    """Класс для социальной сети Telegram."""
    
    def __init__(self, users_count: int):
        super().__init__("Telegram", users_count)
        self._channels = []
        self._secret_chats_count = 0

    def create_channel(self, name: str, is_verified: bool = False) -> Optional[Channel]:
        """
        Создает новый канал.
        
        Args:
            name: Название канала
            is_verified: Верифицирован ли канал
            
        Returns:
            Channel: Созданный канал или None при ошибке
        """
        if not name:
            return None
            
        new_channel = Channel(name=name, is_verified=is_verified)
        self._channels.append(new_channel)
        print(f"Создан канал: {name} {'(верифицированный)' if is_verified else ''}")
        return new_channel

    def create_secret_chat(self) -> bool:
        """Создает секретный чат."""
        self._secret_chats_count += 1
        return True

    def send_message(self, recipient: str, message: str, is_secret: bool = False) -> bool:
        """
        Отправляет сообщение с учетом особенностей Telegram.
        
        Args:
            recipient: Получатель сообщения
            message: Текст сообщения
            is_secret: Является ли сообщение секретным
            
        Returns:
            bool: True если сообщение отправлено успешно
        """
        if not self.is_active:
            return False
            
        prefix = "🔒 Секретное сообщение" if is_secret else "Сообщение"
        if recipient and message:
            self._messages_sent += 1
            print(f"[Telegram] {prefix} для {recipient}: {message}")
            return True
        return False

    def get_features(self) -> List[str]:
        return [
            "Каналы",
            "Секретные чаты",
            "Шифрование сообщений",
            "Боты"
        ]

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, каналов: {len(self._channels)}, секретных чатов: {self._secret_chats_count}"

    def __repr__(self) -> str:
        return (f"Telegram(users_count={self.users_count}, "
                f"channels_count={len(self._channels)}, "
                f"secret_chats={self._secret_chats_count})")

class Facebook(SocialNetwork):
    """Класс для социальной сети Facebook."""
    
    def __init__(self, users_count: int):
        super().__init__("Facebook", users_count)
        self._groups_count = 0
        self._pages_count = 0

    def create_group(self, name: str) -> bool:
        """Создает новую группу."""
        if name:
            self._groups_count += 1
            return True
        return False

    def create_page(self, name: str) -> bool:
        """Создает новую страницу."""
        if name:
            self._pages_count += 1
            return True
        return False

    def get_features(self) -> List[str]:
        return [
            "Группы",
            "Страницы",
            "Маркетплейс",
            "Истории",
            "Реклама"
        ]

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, групп: {self._groups_count}, страниц: {self._pages_count}"

if __name__ == "__main__":
    print("Демонстрация работы классов социальных сетей\n")

    # Создаем экземпляры социальных сетей
    telegram = Telegram(500_000_000)
    facebook = Facebook(2_900_000_000)

    # Демонстрация Telegram
    print("\n--- Telegram ---")
    print(telegram)
    
    # Создаем канал и отправляем сообщения
    telegram.create_channel("Новости технологий", is_verified=True)
    telegram.send_message("Алексей", "Привет! Как дела?")
    telegram.send_message("Мария", "Важное сообщение", is_secret=True)
    
    print("\nОсобенности Telegram:")
    for feature in telegram.get_features():
        print(f"- {feature}")

    # Демонстрация Facebook
    print("\n--- Facebook ---")
    print(facebook)
    
    # Создаем группу и страницу
    facebook.create_group("Программисты Python")
    facebook.create_page("IT Новости")
    facebook.send_message("Друг", "Смотри что я нашел!")
    
    print("\nОсобенности Facebook:")
    for feature in facebook.get_features():
        print(f"- {feature}")

    # Тестирование методов базового класса
    print("\n--- Общие методы ---")
    networks: List[SocialNetwork] = [telegram, facebook]
    
    for network in networks:
        print(f"\n{network.name}:")
        print(f"Отправлено сообщений: {network.get_messages_sent()}")
        print(f"Активна: {'Да' if network.is_active else 'Нет'}")
