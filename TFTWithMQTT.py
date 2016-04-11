import sys
try:
    import paho.mqtt.client as mqtt
except ImportError:
    import os
    import inspect
    cmd_subflolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe()))[0], "../src")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)
    import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    print("rc: "+str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


def on_publish(mqttc, obj, msg):
    print("mid: "+str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect("www.znh.tw", 1883, 60)
mqttc.subscribe("/inTopic", 0)

mqttc.loop_forever()
