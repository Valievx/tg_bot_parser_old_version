from telethon import TelegramClient
from datetime import datetime, timedelta
from config import DESTINATION, API_ID, API_HASH, SESSION

BEGIN = datetime.now() - timedelta(days=30)
CHAT = -1001369370434  # кортеж из телеграм чатов, которые мы будем парсить
KEY_WORDS = ''  # ключевые слова которые должны быть в сообщении

client = TelegramClient(SESSION, API_ID, API_HASH)


def parse_msg():
    async def parse():

        chat = await client.get_input_entity(CHAT)

        async for message in client.iter_messages(chat, reverse=True, offset_date=BEGIN):
            try:
                if KEY_WORDS in message.text:
                    await client.forward_messages(DESTINATION, message)
                    print(message.chat.title, "\t\t", message.date, "\t\t", message.text)
            except Exception as ex:
                pass

    with client:
        client.loop.run_until_complete(parse())


if __name__ == "__main__":
    parse_msg()
