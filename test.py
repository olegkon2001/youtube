import json



channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
#channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(channel, indent=2, ensure_ascii=False))

class Channel:
    channel_id = ''

    def __init__(self, channel_id):
        self.channel_id = channel_id

        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))