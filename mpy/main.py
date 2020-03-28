# encoding:utf-8
import network
import time
import client
from machine import Pin
import os
import json
local_times = 0
sta_if = ''
def wifi_connect(name, psd):
    global sta_if
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(name, psd)
    for i in range(10):
        time.sleep(1)
        print(i + 1, 'attempt at connection')
    if sta_if.isconnected() == True:
        a = 'WiFi connection successful'
        print(a, sta_if.ifconfig())
    else:
        a = 'WiFi connection failed. Please try again'
        print(a)

def wifi_ap(name, psd):
    ap_if = network.WLAN(network.AP_IF)
    ap_if.config(essid=name, authmode=network.AUTH_WPA_WPA2_PSK, password=psd)
    for i in range(5):
        time.sleep(1)
        print('The AP build......')
    a = 'The AP was created successfully, and you are now ready to connect.'
    print(a)

def ws_led(uri):
    global local_times
    with client.connect(uri) as ws:
        print("waitting for message")
        while True:
            ws.send('{"error":1}')
            getting = ws.recv()
            all_times = int(json.loads(getting)["times"])
            if all_times > local_times:
                a = Pin(2, Pin.OUT)
                a.value(0)
                time.sleep(1)
                a.value(1)
                local_times = all_times
            time.sleep(2)

if __name__ == "__main__":
    wifi_connect("SSID_NAME", "SSID_PWD")
    ws_led("WS_URL")