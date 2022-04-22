from lib2to3.pgen2 import token
from urllib import request
import requests




def sendMensage(mensage):
    token = '5312728318:AAFmGvZMbTMeHG-OnjVnGglCHBeU4Pb3tHs'
    chat_id = '5252193765'
    mensagem = mensage
    URL = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+mensagem
    answer = requests.get(URL)
    print(answer.json())
