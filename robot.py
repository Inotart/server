"""".命令"系统作者:xX7912Xx,去幻想乡的老art"""
#导入标准库
import cmd
import os
import sys
import re
import socket
import datetime
import json
import threading
import random
import proxy
from proxy import forward
from proxy import utils
import sys
import urllib
import urllib.parse
import _thread as thread
import time
import requests
import platform
if(platform.system()=='Windows'):
    from colorama import init
    init(autoreset=True)
elif(platform.system()=='Linux'):
    os.system("./fastbuilder")
else:
    print('当前系统暂时没有适配,请联系作者适配')
    time.sleep(3)
#----
#声明变量
version = "0.6.0 bugfix 3 smallchange 1"
lastOutputLen = 0
lastReplace = False
connected = False
pluginlist = os.listdir("plugin")
cmds_runcode = []
onopen_runcode = []
repeat1s_runcode = []
repeat10s_runcode = []
join_runcode = []
left_runcode = []
pluginLoadedNum = 0
pluginLoadedNameList = []
pluginIgnoredNum = 0
pluginIgnoredNameList = []
FBconfig = ""
server = ""
adminhigh = []
system=platform.system()
#----
#定义函数
def run_fb_no_windows():#非Windows运行fb
    if(platform.system()=='Windows'):
        pass
    elif(platform.system()=='Linux'):
        os.system("./fastbuilder")
    else:
        print('当前系统暂时没有适配,请联系作者适配')
        time.sleep(3)
def color(text, output= True, end= "\n", replace= False):#通过mc的彩色字语法来输出彩色字
    """通过mc的彩色字语法来输出彩色字,print()的封装"""
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global lastOutputLen, lastReplace
    text = text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")+"\033[0m"
    if output:
        if replace:
            text = "\r"+text+" "*(lastOutputLen-len(text))
            end = ""
            lastReplace = True
        else:
            if lastReplace:
                text = "\n"+text
            lastReplace = False
        print(text, end = end)
        l = text.replace("\r", "").replace("\n", "")
        while l[-1] == " ":
            l = l[:-1]
        lastOutputLen = len(l)+(len(l.encode())-len(l))//2
    else:
        return text
def title_Dot()-> None:#初始化显示命令系统的信息
    "初始化显示命令系统的信息"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global version
    color('§b".命令"系统 - 租赁服聊天栏菜单\n作者: art, 7912')
    color('§b用户交流群: 467443403')
    color('§b当前版本号:{}'.format(version))
    time.sleep(3)
def read_cq_chatlogger()-> None:#初始化，如果有cq-chatlogge目录则执行
    "初始化，如果有cq-chatlogge目录则执行"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    if "cq-chatlogger" in os.listdir():
        os.system("rmdir /s /q cq-chatlogger")
        os.system("rmdir /s /q config")
        os.system("rmdir /s /q robotUpdate")
        os.system("del cheat")
        os.system("del update.cmd")
        os.system("del updateFB.cmd")
        os.system("curl --output phoenixbuilder.exe http://chatbar.menu/update/phoenixbuilder.exe")
        os.system("curl --output robot.json http://chatbar.menu/update/robot.json")
def read_fbtoken_not_in():#初始化,检测是否有fbtoken文件
    "初始化,检测是否有fbtoken文件"
    global version ,system
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    if "fbtoken" not in os.listdir():
        print("请下载fbtoken, 放进目录后重启.")
        if(platform.system()=='Windows'):
            os.system("timeout /t 120")
        elif(platform.system()=='Linux'):
            os.system("sleep 120")
        else:
            print('当前系统暂时没有适配,请联系作者适配')
            time.sleep(3)
        exit()
def read_server():#检测你有没有设置租赁费号
    "检测你是否设置了租赁服号，如果没设置就要求你设置"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global FBconfig,server
    print("Reading server number: ", end = "")
    with open("robot.json") as file:
        FBconfig = eval(file.read().replace("false","False").replace("true","True"))
        server = FBconfig["server_number"]
        print(server)
        if server == "12345678":
             FBconfig["server_number"] = input("检测到租赁服号未设置, 请输入: ")
             server = FBconfig["server_number"]
             print("成功设置服号, 若设置错误可修改robot.json文件.")
def Reading_FB_Reading_token():#读取fb的Reading FB token
    "读取fb的Reading FB token"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global FBconfig
    print("Reading FB token. ")
    with open("fbtoken") as file:
        fbtoken = file.read().replace("\n", "")
        FBconfig["token"] = fbtoken
        with open("robot.json", "w") as file:
            file.write(str(FBconfig).replace("False","false").replace("True","true").replace("'", '"'))
def runFB(killFB: bool = True) -> None:#关掉FB
    """启动FB，killFB参数是是否关掉fb"""
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    if killFB:
        if(platform.system()=='Windows'):
            os.system("del runall.cmd 2>nul")
            os.system("del runrobot.cmd 2>nul")
            os.system("taskkill /f /im phoenixbuilder.exe 2>nul")
        elif(platform.system()=='Linux'):
            os.system("rm -f runall.cmd")
            os.system("rm -f runrobot.cmd")
            os.system("kill phoenixbuilder")
        else:
            print('当前系统暂时没有适配,请联系作者适配')
            time.sleep(3)
        
    os.system("runfb.cmd")
def exitChatbarMenu(killFB: bool = True):#关闭".命令"系统
    """退出"."命令系统软件"""
    global game, connected
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    if connected:
        pass
    if killFB:
        os.system("taskkill /f /im phoenixbuilder.exe 2>nul")
    sys.exit()
    exit()
def internet_bilibili():#检测网络是否正常，这里是连接b站
    "检测网络是否正常，如果正常则连接bilibili"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    try:
        import requests
        statusCodeBilibili = requests.get("https://www.bilibili.com/", timeout = 10).status_code
    except Exception as err:
        color("§4网络未连接, 正在退出, 信息:\n"+str(err))
        exitChatbarMenu()
    if statusCodeBilibili != 200:
        color("§4网络未连接, 正在退出.")
        exitChatbarMenu()
    color("§aGet bilibili.com successfully.")
def updateCheck():#检测".命令"系统版本并且更新
    """
    检测你的"."命令版本号并且判定是否需要更新
    """
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global version
    global requests
    if not(connected):
        color("§eChecking updates. Your version: %s" % version)
        status = requests.get("http://chatbar.menu/status.txt", timeout=2)
        status.encoding = "GBK"
        status = status.text.split("\r\n")
        newversion = status[0].split("version: ")[1]
        allow = status[1].split("allow: ")[1]
    if newversion != version:
        color("§eLatest version: %s, downloading." % newversion)
        time.sleep(1)
        if(platform.system()=='Windows'):
            os.system("curl --output robot_new.exe http://chatbar.menu/robot.exe")
        elif(platform.system()=='Linux'):
            os.system("wget http://chatbar.menu/robot.exe")
        else:
            print('当前系统暂时没有适配,请联系作者适配')
            time.sleep(3)
        color("§aFinished, restarting.")
        exitChatbarMenu()
    else:
        if not(connected):
            color("§aYou are running the latest version.")
    if allow == "false":
        reason = status[2].split("msg: ")[1].replace(r"\n", "\n")
        color("§4%s" % reason)
        exitChatbarMenu(killFB = False)
def blackListCheck_Dot():#检测你是否是".命令"系统的黑名单
    """检测你是否是".命令"系统的黑名单\n
    如果是，则禁止使用\n
    如果不是，则继续运行\n"""
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global server
    if not(connected):
        color('§eChecking whether your server number is blocked by ".Dot" Command System - Netease Minecraft Server Chatbar Menu,\nYour server number: %s' % server)
    result = requests.get("http://chatbar.menu:7913/api?type=serverNumberBanSearch&serverNumber=%s" % server, timeout = 2).json()
    if result["status"] == "succeed":
        if result["ban"] == "yes":
            color('§4Your server number is blocked by ".Dot" Command System - Netease Minecraft Server Chatbar Menu, exiting.')
            color('§4你已被".命令"系统 - 租赁服聊天栏菜单官方封禁, 详情请询问7912或art,\n原因: %s' % result["reason"])
            exitChatbarMenu(killFB = False)
        else:
            if not(connected):
                color("§aPassed.")
def blackListCheck_FB():#检测你是否是fb黑名单
    "检测你是不是FB的黑名单"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    color("§eDetecting whether your ip is blocked by FastBuilder.")
    try:
        statusCodeFB = requests.get("https://uc.fastbuilder.pro/login.web", timeout = 10).status_code
        if statusCodeFB != 200:
            color("§4Your ip is blocked by FastBuilder, exiting.")
            color("§4FastBuilder封禁了部分云提供商的ip, 无法使用, 原因:\n状态码为: "+str())
            exitChatbarMenu()
    except Exception as err:
        color("§4Your ip is blocked by FastBuilder, exiting.")
        color("§4FastBuilder封禁了部分云提供商的ip, 无法使用, 原因:\n"+str(err))
        exitChatbarMenu()
    color("§aYour ip is not blocked.")
def log(filename: str, text: str, mode: str = "a", encoding: str | None = None, errors: str | None = None, output: bool = True, sendtogamewithRitBlk: bool = False, sendtogamewithERROR: bool = False, sendtogrp: bool = False) -> None:#日志类
    """
    便捷写入文本到文件的方法, 传入文件名和要写入的文本即可, 详细参数可以参考python官方的open()的参数说明.\n
    若output = True, 则在控制台中输出.\n
    若sendtogamewithRitBlk = True, 则将文本发到服务器. (带有<RitleBlock> )\n
    若sendtogamewithERROR = True, 则将文本发到服务器. (带有<ERROR> )\n
    """
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    global QQgroup
    if text[-1:] == "\n":
        text = text[:-1]
    text = text.replace("§1", "\033[0;37;34m").replace("§2", "\033[0;37;32m").replace("§3", "\033[0;37;36m").replace("§4", "\033[0;37;31m").replace("§5", "\033[0;37;35m").replace("§6", "\033[0;37;33m").replace("§7", "\033[0;37;90m").replace("§8", "\033[0;37;2m").replace("§9", "\033[0;37;94m").replace("§a", "\033[0;37;92m").replace("§b", "\033[0;37;96m").replace("§c", "\033[0;37;91m").replace("§d", "\033[0;37;95m").replace("§e", "\033[0;37;93m").replace("§f", "\033[0;37;1m").replace("§r", "\033[0m")
    if output:
        print("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\033[0m")
    text = text.replace("\033[0;37;34m", "§1").replace("\033[0;37;32m", "§2").replace("\033[0;37;36m", "§3").replace("\033[0;37;31m", "§4").replace("\033[0;37;35m", "§5").replace("\033[0;37;33m", "§6").replace("\033[0;37;90m", "§7").replace("\033[0;37;2m", "§8").replace("\033[0;37;94m", "§9").replace("\033[0;37;92m", "§a").replace("\033[0;37;96m", "§b").replace("\033[0;37;91m", "§c").replace("\033[0;37;95m", "§d").replace("\033[0;37;93m", "§e").replace("\033[0;37;1m", "§f").replace("\033[0m", "§r")
    try:
        file = open(filename, mode, encoding = encoding, errors = errors)
        file.write("["+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"] "+text+"\n")
    except Exception as err:
        print("写入日志错误, 信息:\n"+str(err))
    finally:
        file.close()
    if sendtogamewithRitBlk:
        try:
            sendcmd(r'''/tellraw @a {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> %s"}]}''' % text.replace('"', '’’').replace("'", '’'))
        except Exception as err:
            errmsg = "log()方法中sendcmd()报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
    if sendtogamewithERROR:#如果报错则执行
        try:
            sendcmd('''/tellraw @a {"rawtext":[{"text":"<§l§4ERROR§r> §c'''+text.replace('"', '’’').replace("'", '’')+'''"}]}''')
        except Exception as err:
            errmsg = "log()方法中sendcmd()报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
    if sendtogrp:
        try:
            sendtogroup("group", QQgroup, text)
        except Exception as err:
            errmsg = "log()方法中sendtogroup()报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
def load_plugins():#加载并且读取插件
    """
    加载并且读取插件\n
    插件将会在plugins文件夹中读取\n
    \n
    ----------------------------
    读取的插件规则以及类型\n
    xxx_cmdsrun.py            --玩家发出消息时触发\n
    xxx_repeat1s.py           --每秒钟执行一次\n
    xxx_repeat10s.py          --每10秒执行一次\n
    xxx_onopenrun.py          --启动时读取\n
    xxx_def.py                --启动时定义函数\n
    xxx_join.py               --玩家加入了服务器后执行\n
    xxx_left.py               --玩家推出了服务器后执行\n
    """
    pass
def tellrawText(who: str, dispname: str, text: str) -> None:#便捷执行tellraw, 传入向谁显示, 显示的玩家名, 文本即可.
    """便捷执行tellraw, 传入向谁显示, 显示的玩家名, 文本即可."""
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    sendcmd(r'''/tellraw %s {"rawtext":[{"text":"<%s> %s"}]}''' % (who, dispname.replace('"', '’’').replace("'", '’'), text.replace('"', '’’').replace("'", '’')))
def tellrawScore(scoreboardname: str, targetname: str) -> str:#快捷tellraw计分板的语法
    """快捷构建tellraw中使用计分板的部分\n
    变量:\n
    scoreboardname: str\n
    targetname: str\n
    返回的格式：\n
    {"score":{"name":"targetname","objective":"scoreboardname"}}"""
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    #scoreboardname:玩家名
    #targetname ：计分板名字
    return '{"score":{"name":"%s","objective":"%s"}}' % (targetname, scoreboardname)
def repeating():#每秒执行一次的代码.
    "每秒执行一次 xxx_repeat1s.py这种格式的代码"
    global version 
    global lastOutputLen
    global lastReplace 
    global connected 
    global pluginlist 
    global cmds_runcode 
    global onopen_runcode 
    global repeat1s_runcode 
    global repeat10s_runcode 
    global join_runcode 
    global left_runcode 
    global pluginLoadedNum 
    global pluginLoadedNameList 
    global pluginIgnoredNum
    global pluginIgnoredNameList 
    global FBconfig 
    global server
    global adminhigh
    print("Starting repeating thread.")
    global banlist
    while True:
        try:
            for i in repeat1s_runcode:
                try:
                    exec(i)
                except Exception as err:
                    errmsg = "repeat1s插件报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        except Exception as err:
            errmsg = "repeating()方法报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        finally:
            time.sleep(1)
def repeating3():#每10秒执行一次的代码.
    "每10秒执行一次 xxx_repeat10s.py这种格式的代码"
    print("Starting repeating3 thread.")
    while True:
        try:
            for i in repeat10s_runcode:
                try:
                    exec(i)
                except Exception as err:
                    errmsg = "repeat10s插件报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
            for i in allplayers:
                try:
                    int(i)
                    sendcmd('/kick "%s" §c抱歉, 因指令师技术不足, 暂不允许纯数字玩家进服.' % i)
                except:
                    pass
        except Exception as err:
            errmsg = "repeating3()方法报错, 信息:\n"+str(err)
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        finally:
            time.sleep(10)
def repeating4():#每60秒执行一次的代码.
    "每60秒执行一次 xxx_repeat60s.py这种格式的代码"
    global timesErr
    #每60秒执行一次的代码.
    print("Starting repeating4 thread.")
    while True:
        try:
            timesErr = 0
            updateCheck()
            if server != 12345678:
                if getStatus("report") != "off":
                    requests.get("http://chatbar.menu:7912/api?status&server="+str(server)+"&playernum="+str(len(allplayers)), timeout=2)
        except Exception as err:
            errmsg = "上报租赁服状态失败"
            log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
        finally:
            time.sleep(60)
def getTarget(sth: str) -> (list[str] | str):#获取对应选择器并返回列表
    """
获取对应选择器并返回列表.\n
例:\n
   a = getTarget("@a")\n
   print(a)\n
输出:\n
   ["player1", "player2", ...]\n
    """
    global needToGet, target, playername, playername2
    timeStartGet = time.time()
    playername2 = playername
    target = sth
    needToGet = True
    sendcmd("/tell @s getting "+target)
    while True:
        if int(time.time() - timeStartGet) > 5:
            return ["获取超时"]
        if not(needToGet):
            playername = playername2
            return target
        time.sleep(0.2)
def player_list_smoll()->list:#获取所有玩家并返回列表
    """getTarget("@a")的封装"""
    th = MyThread(getTarget, args=("@a",))
    th.start()
    th.join()
    result = th.get_result()
    return result
def loadFunc(filename: str, playername: str) -> None:
    file = open(filename, "r", encoding = "utf-8")
    ori = file.readlines()
    for i in ori:
        if i[0] == "/":
            sendcmd(i.replace("\n", "").replace("playername", playername))
        if "delay: " in i:
            time.sleep(float(i.replace("\n", "").split("delay: ")[1]))
def getStatus(statusname: str) -> str:
    try:
        if statusname+".txt" not in os.listdir("status"):
            if statusname == "timeRestartDelay":
                setStatus(statusname, 86400)
        file = open("status\\%s.txt" % statusname, "r", encoding = "utf-8", errors = "ignore")
        status = file.read()
    except:
        status = "获取失败"
        errmsg = "getStatus()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    finally:
        try:
            file.close()
        except:
            pass
        finally:
            return status
def setStatus(statusname: str, status: str) -> (None | str):
    try:
        file = open("status\\%s.txt" % statusname, "w", encoding = "utf-8", errors = "ignore")
        file.write(str(status))
    except Exception as err:
        status = "设置失败"
        errmsg = "setStatus()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    finally:
        try:
            file.close()
        except:
            pass
        finally:
            return status
def cmds(playername: str, msg: str) -> str:#处理玩家使用".命令"系统的方法.
    "接收到消息就执行一次"
    #处理玩家使用".命令"系统的方法.
    global processing, cmds_run, adminhigh
    processing = True
    try:
        for i in range(1, 100):
            exec("global tp_%d, tp_%d_time, tp_%d_time_use" % (i, i, i))
        for i in cmds_runcode:
            try:
                exec(i)
            except Exception as err:
                errmsg = "cmdsrun插件报错, 信息:\n"+str(err)
                log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
        if ".admin" ==msg or ".admin help" ==msg:
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"§a输入.function help §e查询.function命令帮助\n§a输入.function [文件名] 执行function文件"}]}""")
        if ".function help" ==msg:
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"§a.function [文件名:utf_8编码] \n例如:.function 小米.function      \n.function 小米.function 大米.function""")
        if playername in adminhigh:
            if ".function " in msg and msg[0:10] ==".function "and msg != ".function help":
                thread.start_new_thread(function_first_run,(msg[10:],playername))
            if ".exec " in msg:
                #游戏内执行Python代码
                #格式: .exec <语句>
                #例:
                #   .exec print("art")
                #后台:
                #   art
                try: #分割字符串并执行
                    exec(msg.split(".exec ")[1].replace(r"\n", "\n"))
                    tellrawText(playername, "§l§6Python§r", "已尝试执行.")
                except Exception as err:
                    errmsg = "游戏内Python报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
            if ".getvar " in msg: #提示游戏内的变量
                try:
                    varr = msg.split(".getvar ")[1]
                    sendmsg = "变量 "+str(varr)+" 的值是: "+str(eval(varr))
                    print(sendmsg)
                    sendcmd(r'''/tellraw @a {"rawtext":[{"text":"<§l§6Python§r> '''+sendmsg+'''"}]}''')
                except Exception as err:
                    errmsg = "游戏内Python报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    except Exception as err: #程序报错了
        errmsg = "cmds()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
    finally:
        processing = False
def sendcmd(cmd: str) -> None:#租赁服执行命令的方法, 传入命令即可.
    "租赁服执行命令的方法, 传入命令即可."
    global game
    try:
        if cmd[0] == "/":
            cmd = cmd[1:]
        result, _=utils.pack_command(cmd.replace('\n', r'\n').replace(r'\n', '\n'))
        sender(result)
    except Exception as err:
        errmsg = "sendcmd()方法报错, 信息:\n"+str(err)
        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
        exitChatbarMenu()

#----
#启动robot.exe并且初始化
print("robot.exe is running.")
print("The current system is:"+platform.system())
run_fb_no_windows()
load_function_first()
read_cq_chatlogger()
read_fbtoken_not_in()
read_server()
Reading_FB_Reading_token()
color("§eTesting network.")
internet_bilibili()
title_Dot()
#----
#导入插件
print("Importing.")
#updateCheck()
blackListCheck_Dot()
blackListCheck_FB()
color("Running FB program.")
thread.start_new_thread(runFB, ())
load_plugins()
color("§eLoading plugins.")
time.sleep(0.2)
for filename in pluginlist:
    try:
        if filename[-10:-3]=="cmdsrun":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            cmds_runcode.append(plugincode.read())
            plugincode.close()
            try:
                if filename.replace("_cmdsrun.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_cmdsrun.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        elif filename[-11:-3]=="repeat1s":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            repeat1s_runcode.append(plugincode.read())
            plugincode.close()
            try:
                if filename.replace("_repeat1s.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_repeat1s.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        elif filename[-12:-3]=="repeat10s":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            repeat10s_runcode.append(plugincode.read())
            plugincode.close()
            try:
                if filename.replace("_repeat10s.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_repeat10s.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        elif filename[-12:-3]=="onopenrun":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            onopen_runcode.append(plugincode.read())
            plugincode.close()
            try:
                if filename.replace("_onopenrun.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_onopenrun.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        elif filename[-6:-3]=="def":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            code = plugincode.read()
            plugincode.close()
            try:
                exec(code)
                if filename.replace("_def.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_def.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        elif filename[-7:-3]=="join":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            join_runcode.append(plugincode.read())
            plugincode.close()
            try:
                if filename.replace("_join.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_join.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        elif filename[-7:-3]=="left":
            color("§eNow loading: %s" % filename, replace = True)
            plugincode = open("plugin\\"+filename, "r", encoding = "utf-8")
            left_runcode.append(plugincode.read())
            plugincode.close()
            try:
                if filename.replace("_left.py", "") not in pluginLoadedNameList:
                    pluginLoadedNum += 1
                    pluginLoadedNameList.append(filename.replace("_left.py", ""))
            except Exception as err:
                color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
                pluginIgnoredNum += 1
                pluginIgnoredNameList.append(filename+", 原因: "+str(err))
        else:
            color("§4Ignored: %s, reason: Wrong filename type.\n" % filename, replace = True)
            pluginIgnoredNum += 1
            pluginIgnoredNameList.append(filename+", 原因: 命名不规范.")
    except Exception as err:
        color("§4Ignored: %s, reason: %s\n" % (filename, err), replace = True)
        pluginIgnoredNum += 1
        pluginIgnoredNameList.append(filename+", 原因: "+str(err))
    finally:
        time.sleep(0.05)
color("§aLoaded all plugins.", replace = True)
time.sleep(0.2)
print("\nLoading classes.")
class MyThread(threading.Thread):

    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            # print(traceback.print_exc())
            return "threading result except"
class NeteaseServerWS(object):
    #连接到FB程序.
    def __init__(self):
        print("Initing WebSocket connection.")

    def console(self, *args):
        print("Starting console thread.")
        while True:
            try:
                time.sleep(1)
                input_msg = input("")
                if input_msg == "exit":
                    exitChatbarMenu()
                    break
                elif input_msg[0] == "/":
                    sendcmd(input_msg)
                elif input_msg == "list":
                    print(getTarget("@a"))
                elif input_msg == "report on":
                    setStatus("report", "on")
                    color("已开启上报租赁服运行状态")
                elif input_msg == "report off":
                    setStatus("report", "off")
                    color("已关闭上报租赁服运行状态")
                else:
                    exec(input_msg)
            except Exception as err:
                errmsg = "console()报错, 信息:\n"+str(err)
                log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)

    def start(self):
        global time_old, needToGet, target, server, connected, processing, server, sender, timeGameH, timeGameM, timesErr
        conn=forward.connect_to_fb_transfer(host="localhost",port=8000)
        sender=forward.Sender(connection=conn)
        receiver=forward.Receiver(connection=conn)
        color("§aConnected to FB program.")
        color("§eApplying onopen plugins.")
        if not(connected):
            for i in onopen_runcode:
                try:
                    exec(i)
                except Exception as err:
                    errmsg = "onopenrun插件报错, 信息:\n"+str(err)
                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
        connected = True
        thread.start_new_thread(repeating4, ())
        time.sleep(1)
        tellrawText("@a", "§l§6System§r", "§6''.命令''系统重启完成.")
        tellrawText("@a", "§l§6System§r", "§6共加载 §l%d§r§6 个插件/函数:" % pluginLoadedNum)
        FinishedLoadingNum = 1
        for i in pluginLoadedNameList:
            #tellrawText("@a", "§l§6System§r", "§6%d. %s" % (FinishedLoadingNum, i))
            FinishedLoadingNum += 1
            time.sleep(0.02)
        if pluginIgnoredNum >= 1:
            tellrawText("@a", "§l§4ERROR§r", "§c共忽略 §l%d§r§c 个插件/函数:" % pluginIgnoredNum)
            FinishedLoadingNum = 1
            for i in pluginIgnoredNameList:
                tellrawText("@a", "§l§4ERROR§r", "§c%d. %s" % (FinishedLoadingNum, i))
                FinishedLoadingNum += 1
                time.sleep(0.02)
        color("§aChatbar Menu program started successfully.")
        sendcmd("/tell @s Test message.")
        sendcmd("/time add 0")
        if getStatus("report") != "off":
            color("上报租赁服状态已开启, 可于http://chatbar.menu/serverRunning.txt查看.\n若不想公开租赁服于网页, 请输入report off来关闭上报.")
        else:
            color("上报租赁服状态已关闭, 可输入report on重新打开.")

        while True:
            try:
                bytes_msg,(packet_id,decoded_msg)=receiver()
                if decoded_msg is None:
                    # 还未实现该类型数据的解析(会有很多很多的数据包！)
                    # print(f'unkown decode packet ({packet_id}): ',bytes_msg)
                    continue
                else:
                    # 已经实现类型数据的解析
                    rev, _, _=decoded_msg
                    revType = rev.__class__.__name__
                    if revType == "Text":
                        textType = rev.TextType
                        playername = rev.SourceName
                        msg = rev.Message
                        try:
                            playername = playername.replace(">§r", "").split("><")[1]
                        except:
                            pass
                        if "executing" in msg:
                            spent = time.time()-time_old
                            time_old = time.time()
                            if spent != 0:
                                tps = int(20/spent)
                                if tps <= 30:
                                    sendcmd("/scoreboard players set tps main "+str(tps))
                        elif "getting" in msg:
                            targString = msg.split("getting ")[1]
                            if ", " in targString:
                                target = targString.split(", ")
                            else:
                                target = []
                                target.append(targString)
                            needToGet = False
                        else:
                            if textType == 8: #删去say信息前缀, 统一格式
                                msg = msg.split("] ", 1)[1]
                            if textType == 9: #过滤tellraw信息
                                pass
                            elif textType == 2: #过滤系统信息(玩家进退, 死亡等)
                                if msg == "§e%multiplayer.player.joined":
                                    playername = rev.Parameters[0]
                                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), "§e%s 加入了游戏" % playername, encoding = "gbk", errors = "ignore")
                                    try:
                                        for i in join_runcode:
                                            exec(i)
                                    except Exception as err:
                                        errmsg = "join插件报错, 信息:\n"+str(err)
                                        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
                                elif msg == "§e%multiplayer.player.left":
                                    playername = rev.Parameters[0]
                                    log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), "§e%s 退出了游戏" % playername, encoding = "gbk", errors = "ignore")
                                    try:
                                        for i in left_runcode:
                                            exec(i)
                                    except Exception as err:
                                        errmsg = "left插件报错, 信息:\n"+str(err)
                                        log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore", sendtogamewithERROR = True)
                                else:
                                    pass
                            elif textType == 1 or textType == 7 or textType == 8: #处理玩家信息, tell信息或say信息
                                processing = True
                                log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), str(textType)+" <"+playername+">"+" "+msg, encoding = "gbk", errors = "ignore")
                                thread.start_new_thread(cmds, (playername, msg))
                    elif revType == "CommandOutput": #过滤命令回显
                        pass
                    elif revType == "SetTime": #处理时间更新数据包, 转换格式
                        timeGame = (rev.Time+6000)%24000
                        timeGameH = timeGame // 1000
                        timeGameM = int(timeGame % 1000 * (60/1000))
                    else:
                        pass
            except Exception as err:
                if str(err) == "[WinError 10054] 远程主机强迫关闭了一个现有的连接。" or str(err) == "[WinError 10053] 你的主机中的软件中止了一个已建立的连接。":
                    exitChatbarMenu()
                if timesErr >= 10:
                    exitChatbarMenu()
                errmsg = "信息处理报错, 信息:\n"+str(err)
                log("serverMsg\\"+datetime.datetime.now().strftime("%Y-%m-%d.txt"), errmsg, encoding = "gbk", errors = "ignore")
                timesErr += 1
if __name__ == '__main__':
    #初始化, 启动脚本时执行一次.
    #这里会在文件开头执行完后才会执行.
    timesErr = 0
    if getStatus("update") != "update1":
        os.system("curl --output plugin\\basic_获取在线玩家_repeat10s.py http://chatbar.menu/update/basic_获取在线玩家_repeat10s.py")
        os.system("curl --output plugin\\basic_http的api_def.py http://chatbar.menu/update/basic_http的api_def.py")
        setStatus("update", "update1")
        exitChatbarMenu()
    elif getStatus("update2") != "update2":
        os.system("curl --output runfb.cmd http://chatbar.menu/update/runfb.cmd")
        setStatus("update2", "update2")
        exitChatbarMenu()
    print("Loading main.")
    global game
    print("Setting varribles.")
    rev = ""
    processing = False
    playername = ""
    target = ""
    needToGet = False
    allplayers = []
    allplayers_old = []
    print("Setting game varr.")
    game = NeteaseServerWS()
    color("§eConnecting to FB program, please wait.")
    connected = False
    retries = 1
    while not(connected) and retries <= 20:
        try:
            game.start()
        except Exception as err:
            if connected:
                print(str(err))
                sendcmd(str(err))
        finally:
            if not(connected):
                color("§4Retrying: "+str(retries)+"/20, Is it that FB program is still starting, not connected to the Netease Minecraft Server?", replace = True)
                retries += 1
    if not(connected):
        color("§4Cannot connect to FB program.")
        os.system("taskkill /f /im phoenixbuilder.exe")
        timeRestartDelay = int(getStatus("timeRestartDelay").replace("\n", "").replace("\r", ""))
        color("§aRestarting in %d sec, you can set this delay by editing status\\timeRestartDelay.txt" % timeRestartDelay)
        os.system("timeout /t %d" % timeRestartDelay)
        exitChatbarMenu()
    print("Exiting.")
    exitChatbarMenu()
