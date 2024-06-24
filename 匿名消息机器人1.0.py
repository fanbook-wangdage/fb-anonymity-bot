import requests#http请求
import json#json数据处理
import time#延时
import websocket#ws接口链接
import base64#请求体编码
import threading
import queue
import re
import traceback
import random
from pygments import highlight#高亮
from pygments.lexers import JsonLexer#高亮
from pygments.formatters import TerminalFormatter#高亮
from colorama import Fore, Back, Style,init#高亮
import ctypes
import sentry_sdk

sentry_sdk.init(
    dsn="https://a30ed1f97ae54e663e8cf7db6928b17d@o4506171336753152.ingest.sentry.io/4506176633896960",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

def colorize_json(smg2,pcolor=''):
    json_data=smg2
    try:
        parsed_json = json.loads(json_data)  # 解析JSON数据
        formatted_json = json.dumps(parsed_json, indent=4)  # 格式化JSON数据

        # 使用Pygments库进行语法高亮
        colored_json = highlight(formatted_json, JsonLexer(), TerminalFormatter())

        print(colored_json)
    except json.JSONDecodeError as e:
        print(json_data)

def addmsg(msg, color="white"):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")
init(autoreset=True)
def colorprint(smg2,pcolor):
    if pcolor=='red':
      print(Fore.RED + smg2)
    elif pcolor=='bandg':
      print(Back.GREEN + smg2)
    elif pcolor=='d':
      print(Style.DIM + smg2)
    # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
    #print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True

null=None

gjc=['https://fanbook.mobi','妈','傻','垃圾','滚','逼','死','病','sb','邀请码','https://in.fanbook.cn']

def gjc_re(wb):
    for x in range(len(gjc)):
        print(re.findall(gjc[x], wb))
        if len(re.findall(gjc[x], wb)) !=0:
            return False
    return True

def get_ad():
    ads=['[广告]\n广告位仅4元/月，加入服务器了解：\nhttps://fanbook.mobi/LmgLJF3N','']
    return ads[random.randint(-1,len(ads)-1)]
    
# 获取控制台窗口句柄
kernel32 = ctypes.windll.kernel32
hwnd = kernel32.GetConsoleWindow()

# 设置窗口标题
if hwnd != 0:
    kernel32.SetConsoleTitleW("匿名消息机器人公用终端进程-1")

false=False
wgcs=[]
yhlb=[]
sycs=[]
fwqpd=['545092921893175296','557134746363478016','558885318607360000','558932697146568704','560675497693278208','561452707010170880','569352831371698177','573116147738996736','574104841631416320']#匿名频道
kyfwqid=['545092248111800320','433204455396081664','534542578788708353','476259807335403520','543395863498969088','521514647564972032','507133168198205440','544085489737916416','400926618899456000']#可用服务器id
yhxz=[]
syyh=[]
glpd=['545093215918080000','433212507046281216','558886088127922176','558934411819986944','560675566450495488','558972192021667840','569353608068718592','573116293679788032','574104746643009536']#管理频道
fwqxl=[10,10,10,10,10,10,10,10,10]#服务器限量
fwqyl=[0,0,0,0,0,0,0,0,0]#服务器用量
cs=0
qggfwq=[557134746363478016]#去广告服务器
fwqyl2=[0,0,0,0,0,0,0,0,0]

lingpai='b27c98a520500c7c0b5f3baacac1e55cf5c4b5'
for i in range(30):
    try:
        data_queue = queue.Queue()
        def on_message(ws, message):
            global yhlb,syyh,wgcs,yhxz
            # 处理接收到的消息
            addmsg('收到消息',color='green')
            colorize_json(message)
            message=json.loads(message)
            content = json.loads(message["data"]["content"])
            print(content)
            if message['data']['resource_type']=="friend_chat_stranger":
                if message["data"]["author"]["bot"] == false:
                    if message['data']['user_id'] in yhlb:
                        print('用户已被记录过')
                        sycs[yhlb.index(message['data']['user_id'])]+=1
                    else:
                        try:
                            yhlb.append(message['data']['user_id'])
                            sycs.append(1)
                            wgcs.append(0)
                            yhxz.append(0)
                            print('新使用用户已被记录')
                        except:
                            pass
                            print('error')
                    if message['data']['user_id'] in syyh:
                        print('用户已被记录过')
                    else:
                        syyh.append(message['data']['user_id'])
                        print('新使用用户已被记录')
                    if sycs[yhlb.index(message['data']['user_id'])] >5:
                        if sycs[yhlb.index(message['data']['user_id'])]==6:
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text":"你发送消息过快，请稍后再试",
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text)
                    else:
                        if wgcs[yhlb.index(message["data"]["user_id"])] > 2:
                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                            headers = {'content-type':"application/json;charset=utf-8"}
                            jsonfile=json.dumps({
                            "chat_id":int(message["data"]["channel_id"]),
                            "text":"你违规次数过多，请稍后再试",
                            "reply_to_message_id":int(message["data"]["message_id"])
                            })
                            print(jsonfile)
                            postreturn=requests.post(url,data=jsonfile,headers=headers)
                            colorize_json(smg2=postreturn.text)
                        else:
                            if len(re.findall("王大哥机器人体验中心",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=557134746363478016
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("控制台日志输出",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=545092921893175296
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("地跑营地",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=558885318607360000
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("Sunset",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=558932697146568704
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("跑跑学院",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=560675497693278208
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("小不点王国",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=561452707010170880
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("蛋仔派对11365551",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=569352831371698177
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                                
                            elif len(re.findall("地铁之家",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=573116147738996736
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif len(re.findall("跑酷营地",str(content))) !=0:
                                yhxz[syyh.index(message["data"]["user_id"])]=574104841631416320
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"选择成功，目标频道：${#"+str(yhxz[syyh.index(message["data"]["user_id"])])+"}",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            elif yhxz[syyh.index(message["data"]["user_id"])] ==0:
                                url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                headers = {'content-type':"application/json;charset=utf-8"}
                                jsonfile=json.dumps({
                                "chat_id":int(message["data"]["channel_id"]),
                                "text":"你没有选择目标服务器，请使用切换服务器功能选择你需要发送匿名消息的服务器，或者直接发我服务器名即可",
                                "reply_to_message_id":int(message["data"]["message_id"])
                                })
                                print(jsonfile)
                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                colorize_json(smg2=postreturn.text)
                            else:
                                if fwqyl[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))] > fwqxl[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))]:
                                    url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                    headers = {'content-type':"application/json;charset=utf-8"}
                                    jsonfile=json.dumps({
                                    "chat_id":int(message["data"]["channel_id"]),
                                    "text":"服务器2分钟内总使用次数已达上限，请等待一段时间，或者联系服务器主",
                                    "reply_to_message_id":int(message["data"]["message_id"])
                                    })
                                    print(jsonfile)
                                    postreturn=requests.post(url,data=jsonfile,headers=headers)
                                    colorize_json(smg2=postreturn.text)
                                else:
                                    fwqyl[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))]+=1
                                    print('收到私信消息')
                                    gjcjc=True
                                    try:
                                        gjcjc=gjc_re(str(content['text']))
                                    except:
                                        try:
                                            if content['type']=='image':
                                                gjcjc=True
                                            else:
                                                gjcjc=gjc_re(str(content))
                                        except:
                                            pass
                                    if gjcjc:
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        try:
                                            jsonfile=json.dumps({
                                            "chat_id":yhxz[syyh.index(message["data"]["user_id"])],
                                            "text":message['data']['content']
                                            })
                                        except:
                                            jsonfile=json.dumps({
                                            "chat_id":yhxz[syyh.index(message["data"]["user_id"])],
                                            "text":message['data']['content']
                                            })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        nmtext=postreturn.text
                                        colorize_json(smg2=postreturn.text)

                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":yhxz[syyh.index(message["data"]["user_id"])],
                                        "text":"{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\"#57aeff\\\",\\\"#E8F4FF\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\"匿名消息信息\\\",\\\"style\\\":{\\\"color\\\":\\\"#ffffff\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\"匿名消息id:**"+str(json.loads(nmtext)["result"]["message_id"])+"**"+"\\\"}},{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,12,0,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"button\\\",\\\"category\\\":\\\"outlined\\\",\\\"color\\\":\\\"FF6A00\\\",\\\"size\\\":\\\"medium\\\",\\\"widthUnlimited\\\":true,\\\"href\\\":\\\"https://oauth.fanbook.mobi/authorize?response_type=code&client_id=456442818882310144&state="+str(yhxz[syyh.index(message["data"]["user_id"])])+"-"+str(json.loads(nmtext)["result"]["message_id"])+"-"+str(json.loads(postreturn.text)["result"]["chat"]["guild_id"])+"-"+str(message["data"]["author"]["nickname"])+"("+str(message["data"]["author"]["username"])+")-"+str(glpd[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))])+"-jb-0\\\",\\\"label\\\":\\\"违规消息请点此举报\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}",
                                        "reply_to_message_id":json.loads(postreturn.text)["result"]["message_id"]
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text)
                                        
                                        if yhxz[syyh.index(message["data"]["user_id"])] not in qggfwq:
                                            url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                            headers = {'content-type':"application/json;charset=utf-8"}
                                            getad=get_ad()
                                            if getad!='':
                                                jsonfile=json.dumps({
                                                "chat_id":yhxz[syyh.index(message["data"]["user_id"])],
                                                "text":getad,
                                                "reply_to_message_id":json.loads(postreturn.text)["result"]["message_id"]
                                                })
                                                print(jsonfile)
                                                postreturn=requests.post(url,data=jsonfile,headers=headers)
                                                colorize_json(smg2=postreturn.text)

                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":"{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\"#2600BF80\\\",\\\"#0d00BF80\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\"匿名消息发送成功\\\",\\\"style\\\":{\\\"color\\\":\\\"#11A675\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\"匿名消息id:**"+str(json.loads(postreturn.text)["result"]["message_id"])+"**\\\"}},{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,12,0,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"button\\\",\\\"category\\\":\\\"outlined\\\",\\\"color\\\":\\\"FF0000\\\",\\\"size\\\":\\\"medium\\\",\\\"widthUnlimited\\\":true,\\\"href\\\":\\\"https://oauth.fanbook.mobi/authorize?response_type=code&client_id=456442818882310144&state="+str(yhxz[syyh.index(message["data"]["user_id"])])+"-"+str(json.loads(nmtext)["result"]["message_id"])+"-"+str(json.loads(postreturn.text)["result"]["chat"]["guild_id"])+"-"+str(message["data"]["author"]["nickname"])+"("+str(message["data"]["author"]["username"])+")-"+str(glpd[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))])+"-c-0\\\",\\\"label\\\":\\\"撤回消息\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}",
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text)
                                        
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(glpd[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))]),
                                        "text":"{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\"#57aeff\\\",\\\"#E8F4FF\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\"匿名消息信息\\\",\\\"style\\\":{\\\"color\\\":\\\"#ffffff\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\"匿名消息id:**"+str(json.loads(nmtext)["result"]["message_id"])+"**  \\\\n发送者:**"+str(message["data"]["author"]["nickname"])+"("+str(message["data"]["author"]["username"])+")"+"**\\\"}},{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,12,0,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"button\\\",\\\"category\\\":\\\"outlined\\\",\\\"color\\\":\\\"FF0000\\\",\\\"size\\\":\\\"medium\\\",\\\"widthUnlimited\\\":true,\\\"href\\\":\\\"https://oauth.fanbook.mobi/authorize?response_type=code&client_id=456442818882310144&state="+str(yhxz[syyh.index(message["data"]["user_id"])])+"-"+str(json.loads(nmtext)["result"]["message_id"])+"-"+str(json.loads(postreturn.text)["result"]["chat"]["guild_id"])+"-"+str(message["data"]["author"]["nickname"])+"("+str(message["data"]["author"]["username"])+")-"+str(glpd[fwqpd.index(str(yhxz[syyh.index(message["data"]["user_id"])]))])+"-c-1\\\",\\\"label\\\":\\\"撤回消息\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}"
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text)
                                        
                                    else:
                                        print('违规消息')
                                        wgcs[yhlb.index(message["data"]["user_id"])]+=1
                                        url='https://a1.fanbook.mobi/api/bot/'+lingpai+'/sendMessage'
                                        headers = {'content-type':"application/json;charset=utf-8"}
                                        jsonfile=json.dumps({
                                        "chat_id":int(message["data"]["channel_id"]),
                                        "text":"勿发送违规消息",
                                        "reply_to_message_id":int(message["data"]["message_id"])
                                        })
                                        print(jsonfile)
                                        postreturn=requests.post(url,data=jsonfile,headers=headers)
                                        colorize_json(smg2=postreturn.text)
            if len(yhxz) != len(syyh):
                del yhxz[-1]
                print('[BUG]已重置使用记录')
            # 在这里添加你希望执行的操作
        def on_error(ws, error):
            # 处理错误
            error=traceback.format_exc()
            addmsg("发生错误:"+str(error),color='red')
        def on_close(ws):
            # 连接关闭时的操作
            addmsg("连接已关闭",color='red')
        def on_open(ws):
            # 连接建立时的操作
            addmsg("连接已建立",color='green')
            # 发送心跳包
            def send_ping():
                print('发送：{"type":"ping"}')
                ws.send('{"type":"ping"}')
            send_ping()  # 发送第一个心跳包
            # 定时发送心跳包
            def schedule_ping():
                send_ping()
                # 每25秒发送一次心跳包
                websocket._get_connection()._connect_time = 0  # 重置连接时间，避免过期
                ws.send_ping()
                websocket._get_connection().sock.settimeout(70)
                ws.send('{"type":"ping"}')
            websocket._get_connection().run_forever(ping_interval=25, ping_payload='{"type":"ping"}', ping_schedule=schedule_ping)
        # 替换成用户输入的BOT令牌
        lingpai = lingpai
        url = f"https://a1.fanbook.mobi/api/bot/{lingpai}/getMe"
        # 发送HTTP请求获取基本信息
        response = requests.get(url)
        data = response.json()
        def send_data_thread():
            global cs
            global yhlb,wgcs,yhxz
            global sycs,fwqyl,syyh
            while True:
                # 在这里编写需要发送的数据
                time.sleep(20)
                cs+=1
                ws.send('{"type":"ping"}')
                addmsg('发送心跳包：{"type":"ping"}',color='green')
                requests.get(url='https://uptime.betterstack.com/api/v1/heartbeat/5qK3yTuTk9GPE1qz7boMbyiN')
                if cs > 10:
                    cs = 0
                    yhlb=[]
                    sycs=[]
                    wgcs=[]
                    fwqyl=[0,0,0,0,0,0,0,0,0]
                    print('已重置使用记录')
        if response.ok and data.get("ok"):
            user_token = data["result"]["user_token"]
            device_id = "your_device_id"
            version_number = "1.6.60"
            super_str = base64.b64encode(json.dumps({
                "platform": "bot",
                "version": version_number,
                "channel": "office",
                "device_id": device_id,
                "build_number": "1"
            }).encode('utf-8')).decode('utf-8')
            ws_url = f"wss://gateway-bot.fanbook.mobi/websocket?id={user_token}&dId={device_id}&v={version_number}&x-super-properties={super_str}"
            threading.Thread(target=send_data_thread, daemon=True).start()
            # 建立WebSocket连接
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp(ws_url,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)
            ws.on_open = on_open
            ws.run_forever()
        else:
            addmsg("无法获取BOT基本信息，请检查令牌是否正确。",color='red')
    except:
        continue
    
