class DigitalPhoto:
    """Класс для работы с цифровыми фотографиями"""
    
    def __init__(self, name: str, resolution: tuple[int, int], file_format: str):
        """
        Инициализация объекта фотографии
        
        Args:
            name: Название изображения
            resolution: Разрешение (ширина, высота) в пикселях
            file_format: Формат файла (JPEG, PNG и т.д.)
            
        Raises:
            TypeError: При неверном типе параметров
            ValueError: При некорректных значениях
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not (isinstance(resolution, tuple) and len(resolution) == 2 and
                all(isinstance(x, int) and x > 0 for x in resolution)):
            raise ValueError("Разрешение должно быть кортежем из двух положительных целых чисел")
        if not isinstance(file_format, str):
            raise TypeError("Формат должен быть строкой")

        self.name = name
        self.resolution = resolution
        self.format = file_format

    def resize(self, width: int, height: int) -> str:
        """Изменяет разрешение фотографии"""
        if not (isinstance(width, int) and width > 0):
            raise ValueError("Ширина должна быть положительным целым числом")
        if not (isinstance(height, int) and height > 0):
            raise ValueError("Высота должна быть положительным целым числом")
            
        self.resolution = (width, height)
        return f"Установлено новое разрешение: {self.resolution}"

    def convert(self, new_format: str) -> str:
        """Конвертирует в другой формат"""
        if not isinstance(new_format, str):
            raise TypeError("Формат должен быть строкой")
            
        old_format = self.format
        self.format = new_format
        return f"Конвертировано из {old_format} в {new_format}"

    def __str__(self) -> str:
        """Информация о фотографии"""
        return (f"Фотография '{self.name}'\n"
                f"Разрешение: {self.resolution[0]}x{self.resolution[1]}\n"
                f"Формат: {self.format}")
    
class VideoClip:
    """Класс для работы с видеофайлами"""
    
    def __init__(self, title: str, duration: int, codec: str):
        """
        Инициализация видеофайла
        
        Args:
            title: Название видео
            duration: Длительность в секундах
            codec: Используемый кодек (MP4, AVI и т.д.)
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not (isinstance(duration, int) and duration > 0):
            raise ValueError("Длительность должна быть положительным целым числом")
        if not isinstance(codec, str):
            raise TypeError("Кодек должен быть строкой")

        self.title = title
        self.duration = duration
        self.codec = codec

    def trim(self, start: int, end: int) -> str:
        """Обрезает видео по временным меткам"""
        if not (isinstance(start, int) and start >= 0):
            raise ValueError("Начальная точка должна быть положительным числом")
        if not (isinstance(end, int) and end >= 0):
            raise ValueError("Конечная точка должна быть положительным числом")
        if end <= start:
            raise ValueError("Конечная точка должна быть больше начальной")
            
        self.duration = end - start
        return f"Обрезано до {self.duration} секунд"

    def change_codec(self, new_codec: str) -> str:
        """Изменяет кодек видео"""
        if not isinstance(new_codec, str):
            raise TypeError("Кодек должен быть строкой")
            
        self.codec = new_codec
        return f"Кодек изменен на {new_codec}"

    def get_info(self) -> dict:
        """Возвращает метаданные видео"""
        return {
            'title': self.title,
            'duration': f"{self.duration} сек",
            'codec': self.codec
        }
    
class AudioTrack:
    """Класс для работы с аудиозаписями"""
    
    def __init__(self, track_name: str, length: int, audio_format: str):
        """
        Инициализация аудиозаписи
        
        Args:
            track_name: Название трека
            length: Длительность в секундах
            audio_format: Формат аудио (MP3, WAV и т.д.)
        """
        if not isinstance(track_name, str):
            raise TypeError("Название трека должно быть строкой")
        if not (isinstance(length, int) and length > 0):
            raise ValueError("Длительность должна быть положительным целым числом")
        if not isinstance(audio_format, str):
            raise TypeError("Формат должен быть строкой")

        self.track_name = track_name
        self.length = length
        self.audio_format = audio_format

    def edit(self, start: int = 0, end: int = None) -> str:
        """Редактирует аудиозапись"""
        if not (isinstance(start, int) and start >= 0):
            raise ValueError("Начальная точка должна быть положительным числом")
        if end is not None:
            if not (isinstance(end, int) and end >= 0):
                raise ValueError("Конечная точка должна быть положительным числом")
            if end <= start:
                raise ValueError("Конечная точка должна быть больше начальной")
            self.length = end - start
        return f"Длительность трека: {self.length} сек"

    def convert_format(self, new_format: str) -> str:
        """Конвертирует аудио в другой формат"""
        if not isinstance(new_format, str):
            raise TypeError("Формат должен быть строкой")
            
        self.audio_format = new_format
        return f"Трек конвертирован в {new_format}"

    def metadata(self) -> str:
        """Возвращает информацию о треке"""
        return (f"Аудиотрек: {self.track_name}\n"
                f"Длительность: {self.length} секунд\n"
                f"Формат: {self.audio_format}")
