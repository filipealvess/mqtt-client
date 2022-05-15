# Cliente MQTT
Cliente MQTT criado com o pacote [Paho MQTT](https://pypi.org/project/paho-mqtt/).

## Como executar
1. Clone o repositório:
```
git clone https://github.com/filipealvess/mqtt-client.git
```

2. Entre na pasta do projeto:
```
cd mqtt-client
```

3. Crie o ambiente virtual:
```
python3 -m venv venv
```

4. Ative o ambiente virtual:
```
. venv/bin/activate
```

5. Instale o Paho-MQTT
```
pip install paho-mqtt
```

6. Execute o cliente MQTT ouvinte (_subscriber_)
```
python sub.py
```

7. Em outro terminal, execute o cliente MQTT emissor (_publisher_)
```
python pub.py
```

8. Pronto! No terminal do ouvinte (_subscriber_) você verá algo como isso:
```
Listening...
temperature = b'36.5'
humidity = b'25.7'
```
