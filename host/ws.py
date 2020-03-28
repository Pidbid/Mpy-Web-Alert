#encoding:utf-8
import asyncio
import websockets as ws
import json


def readJson(filePath):
    with open(filePath,'rb') as fp:
        a = json.load(fp)
    return a

def writeJson(filepath,msg):
    with open(filepath,'w+',encoding='utf-8') as fp:
        json.dump(msg, fp, indent=4)

async def user_scan(websocket, path):
    async for message in websocket:
        rec_message = json.loads(message.replace("\n",""),strict=False)
        print(rec_message)
        if rec_message["error"] == 0:  # 0表示为接收的消息是有人访问发送来的
            get_json = readJson("ipmsg.json")
            all_ip = get_json["ip"]
            all_ip.append(rec_message["ip"])
            get_json["ip"] = list(set(all_ip))  # 某人多次访问会进行提示，但是不会多次记录
            get_json["times"] += 1
            writeJson("ipmsg.json", get_json)
        elif rec_message["error"] == 1:
            get_json = readJson("ipmsg.json")
            await websocket.send('{"error":2,"times":"'+str(get_json["times"])+'"}')

start_server = ws.serve(user_scan, "0.0.0.0", 2233)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()