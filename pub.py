# Publisher
import paho.mqtt.publish as publish

host = 'test.mosquitto.org'
port = 1883

if __name__ == '__main__':
  publish.single(topic='temperatura', payload=36.5, hostname=host)
  publish.single(topic='umidade', payload=25.7, hostname=host)
