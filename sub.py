# Subscriber
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

host = 'test.mosquitto.org'
port = 1883

def on_message(client, userdata, msg):
  topic = msg.topic
  payload = float(msg.payload.decode())
  high_temperature = (topic == 'temperatura' and payload > 50)

  if (high_temperature):
    publish.single(topic='ativar-led', payload='off', hostname=host)

  else:
    publish.single(topic='ativar-led', payload='on', hostname=host)

  print(topic + ' = ' + str(payload))

if __name__ == '__main__':
  print('Escutando os tópicos "temperatura" e "umidade"...')

  client = mqtt.Client()
  client.on_message = on_message

  client.connect(host, port, 60)

  client.subscribe('temperatura')
  client.subscribe('umidade')

  while client.loop() == 0:
    pass
