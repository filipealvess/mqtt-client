# Publisher
import paho.mqtt.publish as publish

host = 'test.mosquitto.org'
port = 1883

if __name__ == '__main__':
  publish.single(topic='temperature', payload=36.5, hostname=host)
  publish.single(topic='humidity', payload=25.7, hostname=host)
