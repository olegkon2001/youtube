import json



channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
#channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(channel, indent=2, ensure_ascii=False))