from pyrogram import Client

api_id = 'your_api_id'
api_hash = 'your_api_hash'
chat_ids = ['chat_id1', 'chat_id2', 'chat_id3', ...] 
message = "Hello, it's me"

with Client("my_account", api_id, api_hash) as app:
    for chat_id in chat_ids:
        app.send_message(chat_id, message)
