
from confluent_kafka import Consumer, KafkaError
import json
import logging

# Email MOdules 
import os 
import smtplib
from email.message import EmailMessage

from secret import EMAIL_ADRESS,EMAIL_PASSWORD,SENDER_EMAIL

# telegramMensage
import requests

msg = EmailMessage()

# funçao que ira mandar o email 
def sendEmail(subject,content):
    msg = EmailMessage()
    msg['subject'] = subject
    msg['From'] = EMAIL_ADRESS
    msg['To'] = SENDER_EMAIL
    msg.set_content(content)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)

# funçao que ira mandar a mensagem do telegram

def sendMensage(mensage):
    token = '5312728318:AAFmGvZMbTMeHG-OnjVnGglCHBeU4Pb3tHs'
    chat_id = '5252193765'
    mensagem = mensage
    URL = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+mensagem
    requests.get(URL)



#sleep(30)
### Consumer
c = Consumer({
    'bootstrap.servers': 'kafka1:19091,kafka2:19092,kafka3:19093',
    'group.id': 'send-email',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
})

c.subscribe(['notify'])
#{"timestamp": 1649288146.3453217, "new_file": "9PKAyoN.jpeg"}



try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            data = json.loads(msg.value())
            filename = data['new_file']
            datatype = data['MensageType']
            try:
                sendEmail(f'Serviço {datatype} foi Usado ',f'A foto {filename} usou o serviço de {datatype}')
                sendMensage(f'Serviço {datatype} foi Usado A foto {filename} usou o serviço de {datatype}')
            except:
                print("Ouve um erro ")

            
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            logging.warning('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            logging.error('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass
finally:
    c.close()
