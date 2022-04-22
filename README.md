
## Atividade

Adicione uma novo ator (microsserviço) no projeto que será responsável por notificar através do telegram ou e-mail que a operação do 'rotate' ou 'grayscale' foi finalizada. Para isso será necessário alterar o projeto adicionando uma nova etapa de pubicação num novo tópico (por exemplo **/notificacao**) por parte do microsserviço 'rotate' e 'grayscale'. O novo microsserviço '**notifacador**' será responsável por checar (pooling) o tópico e fazer o envio de mensagem no telegram ou e-mail para um contato defindo (pode ser fixo ou variável**) quando a operação estiver finalizada. 
** Se fizer variável, coloque um input de e-mail/telegram_id no HTML do microsserviço 'upload'. 

As mensagens enviadas devem conter:
  1. o nome do arquivo original
  2. a indicação da operação realizada

Por exemplo: 
```
O arquivo perfil.jpg foi rotacionado.
```
```
O arquivo perfil.jpg foi transformado em preto e branco.
```

Sugestões de como usar Telegram/Email: 

* Telegram: 
   * https://usp-python.github.io/05-bot/
   * https://stackoverflow.com/questions/43291868/where-to-find-the-telegram-api-key
  
* E-mail:
   * https://realpython.com/python-send-email/

## Configs do projeto 

Pra mandar o email e necessario adicionar 2 variaveis em um arquivo chamdo secret na pasta notificacao 
ea variavel msg['to'] para onde o email sera mandado: 
- EMAIL_ADRESS 
- EMAIL_PASSWORD 
- msg['To'] = 'Email de destino'

