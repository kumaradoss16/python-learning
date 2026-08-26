import json
from telethon import TelegramClient

API_ID = 12345678
API_HASH = "YOUR_API_HASH"

CHANNEL = "channel_username"

client = TelegramClient("telegram_session", API_ID, API_HASH)


async def main():

    messages = []

    async for message in client.iter_messages(
        CHANNEL,
        reverse=True
    ):

        messages.append({
            "id": message.id,
            "date": message.date.isoformat() if message.date else None,
            "text": message.text or "",
        })

    with open(
        "telegram_messages.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            messages,
            file,
            ensure_ascii=False,
            indent=4
        )

    print(f"Extracted {len(messages)} messages")


with client:
    client.loop.run_until_complete(main())