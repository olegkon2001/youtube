import os


from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('UCMCgOm8GZkHp8zJ6l7_hIuA')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
vdud.print_info()

