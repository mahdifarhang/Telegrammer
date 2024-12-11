from celery import shared_task

from core.requester import APIRequester


@shared_task
def send_telegram_message(message_id):
    from sender.models import Message

    message = Message.objects.get(id=message_id)
    requester = APIRequester()
    data = {
        "chat_id": message.chat_id,
        "text": message.text,
    }
    if message.parse_mode != Message.ParseMode.NORMAL:
        data["parse_mode"] = Message.ParseMode(message.parse_mode).label
    if not message.enable_notification:
        data["disable_notification"] = True
    url_token = message.sender_bot.token
    try:
        response = requester(
            # Important to have the `./` at the beginning (Preventing bug with urljoin)
            endpoint=f"./bot{url_token}/sendMessage",
            method="POST",
            **{"data": data}
        )
    except Exception as exp:
        unsuccessful_message_sending(message, exp)
        return
    if response.get('ok'):
        message.status = Message.StatusChoices.SENT
        result = response.get('result')
        if result:
            message.telegram_message_id = result.get('message_id')
        message.save()
    else:
        unsuccessful_message_sending(message, response)


def unsuccessful_message_sending(message, error=None):
    from sender.models import Message

    message.status = Message.StatusChoices.FAILED
    message.error = error
    message.save()
