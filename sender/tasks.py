from core.requester import APIRequester


def send_telegram_message(message):
    requester = APIRequester()
    data = {
        "chat_id": message.chat_id,
        "text": message.text,
    }
    url_token = message.sender_bot.token
    response = requester(
        # Important to have the `./` at the beginning (Preventing bug with urljoin)
        endpoint=f"./bot{url_token}/sendMessage",
        method="POST",
        **{"data": data}
    )