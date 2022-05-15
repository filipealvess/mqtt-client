# Subscriber
import paho.mqtt.client as mqtt

host = 'test.mosquitto.org'
port = 1883

def on_message(client, userdata, msg):
  print(msg.topic + " = " + str(msg.payload))

if __name__ == '__main__':
  print('Listening...')

  client = mqtt.Client()
  client.on_message = on_message

  client.connect(host, port, 60)

  client.subscribe('temperature')
  client.subscribe('humidity')

  while client.loop() == 0:
    pass
