# Импорт классов из предыдущего задания
from task_1 import DigitalPhoto, VideoClip, AudioTrack

if __name__ == "__main__":
    # Создание экземпляров классов
    photo = DigitalPhoto("Закат", (1920, 1080), "JPEG")
    video = VideoClip("Фильм", 3600, "MP4")
    audio = AudioTrack("Песня", 300, "MP3")

    # Работа с фотографией
    photo.resize(1280, 720)
    photo.convert("PNG")
    print(photo)  

    # Работа с видео
    video.trim(600, 1200)
    video.change_codec("AVI")
    print(video.get_info())

    # Работа с аудио
    audio.edit(start=30, end=90)
    audio.convert_format("WAV")
    print(audio.metadata())

    # Тестирование обработки ошибок
    try:
        photo.resize(-1280, 720)  
    except ValueError as e:
        print(f'Ошибка: {e}')

    try:
        photo.convert(123)  
    except TypeError as e:
        print(f'Ошибка: {e}')

    try:
        video.trim(1200, 600)  
    except ValueError as e:
        print(f'Ошибка: {e}')
