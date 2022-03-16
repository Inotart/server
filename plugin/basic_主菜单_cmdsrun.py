match msg:
        case ".help" | "help" | ".帮助": #帮助命令.
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n帮助菜单\n请检查你的游戏id\n部分玩家会因为id无法正常运作\n主程序提供者: §lCL_P §r(游戏昵称: §l一包绿豆糕_§r )\n脚本程序制作: §lart §r(游戏昵称: §l敏羽的老art§r), §l7912 §r(游戏昵称: §l7912mail§r)"}]}''')
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"输入§l.kill§r返回重生点,\n输入§l.rtp§r随机传送,\n输入§l.main§r返回主城\n输入§l.shop§r去商店\n输入§e.shop help§r查看商店帮助\n输入§l.dp§r去地皮区\n输入§l.gm0§r改为生存模式\n输入§l.surArea§r去生存区\n输入§a.htp§r 查看玩家互传帮助"}]}''')
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"输入§l.myself§r查看个人信息\n输入§l.sendtogrp <信息>§r可将信息转发到§6Qgroup§r\n输入§b.admin§r查看管理员菜单帮助\n输入.setsp设置重生点"}]}''')
        case ".admin" | ".admin ": #管理员可以使用的命令的帮助.
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n管理选项 帮助菜单\n§r输入§b.admin ban <玩家名> <时间> [理由] §r封禁玩家(仅管理可用)"}]}''')
        case ".shop help" | ".shop help ": #商店命令帮助.
            sendcmd("/tellraw "+playername+r''' {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n商店命令 帮助菜单\n§r输入§e.shop trans tobank <存金币数> §r可将金币存入银行\n§r输入§e.shop trans frombank <取金币数> §r可将金币从银行取出\n注意: 改游戏名前请将金币从银行全部取出, 否则银行内你存的金币会丢失.\n购买/卖出商品时会在金币余额内进行, 所以在购买前请将金币从银行取出.\n玩家间转账(还没做)会在银行余额内进行, 所以转账前请将金币存入银行."}]}''')
        case ".game" | ".game ": #小游戏的菜单
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> game--帮助菜单\\n§a.game list §r获取当前租赁服已安装游戏列表以及房间数\\n§a.game stop §r暂停当前游戏\\n§a.game next §r继续当前游戏\\n§a.game run [游戏名] §r运行游戏"}]}""")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"§a.game exit §r退出当前游戏\\n§a.game reset §r重新启动当前游戏\\n§a.game resetall§r重制游戏加载记录\\n§a.game totp [游戏名] §r开放房间并邀请玩家进入（一次一个）\\n§a.game detotp §r取消邀请"}]}""")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"§a.game roomlist [游戏名]§r列表游戏房间（默认全部）\\n§a.game help §r打开该游戏界面帮助"}]}""")
        case ".ver" | ".version": #查看当前辅助程序版本号
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> %s"}]}""" % version)
        case ".rtp" | ".rtp " | ".随机传送": #随机传送
            x = random.randint(-100000, 100000)
            z = random.randint(-100000, 100000)
            sendcmd("/tp "+playername+" "+str(x)+" 80 "+ str(z))
            sendcmd("/tellraw "+playername+""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送到"""+" "+str(x)+" 80 "+str(z)+""""}]}""")
        case ".dp": #去地皮
            sendcmd("/tp "+playername+ " 250250 125 250250")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送到地皮, 顺便一提, 地皮做完就是干完活了."}]}""")
        case ".kill" | ".kill ": #自杀
            sendcmd("/kill "+playername)
        case ".main" | ".main " | ".hub" | ".hub ": #回主城
            sendcmd("/tp "+playername+" 14454 65 114631")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 传送成功."}]}""")
        case ".me" | ".me " | ".myself" | ".myself ": #个人信息
            sendcmd(r'''/execute '''+playername+'''~~~ /tellraw  @s {"rawtext":[{"text":"====§l§6Ritle§aBlock§r====\\n玩家名称:"},{"selector":"@s"},{"text":"\\n§4EXP: §r"},{"score":{"name":"@s","objective":"exp"}},{"text":"§4 / §r"},{"score":{"name":"@s","objective":"expCanUpt"}},{"text":"\\n§6等级: §r"},{"score":{"name":"@s","objective":"expLevel"}},{"text":"\\n§e金币: §r"},{"score":{"name":"@s","objective":"coin"}},{"text":"§e 银行金币存款: §r%s\\n§a在线时间: §r"},{"score":{"name":"@s","objective":"time"}},{"text":" §as"}]}''' % getCoin(playername))
            sendcmd(r'''/execute '''+playername+'''~~~ /tellraw  @s {"rawtext":[{"text":"{"score":{"name":"@s","objective":"time"},§as\\n§b跑酷时间: §r"},{"score":{"name":"@s","objective":"parkouring"}},{"text":"§b /\\n§r"},{"score":{"name":"@s","objective":"timeParkour"}},{"text":"§b ticks\\n§r扔雪球关闭\\n§r\\n§r"}]}''')
        case ".shop" | ".shop ": #商店
            sendcmd("/tp "+playername+" 150003 14 150003")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送至商店."}]}""")
        case ".gm0" | ".gamemode 0": #改生存模式
            sendcmd("/gamemode 0 "+playername)
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 你的游戏模式已刷新."}]}""")
        case ".surArea": #去生存区
            sendcmd("/tp "+playername+ " 7000 202 7000")
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已传送"}]}""")
        case ".htp" | ".htp ": #玩家互传菜单
            sendcmd("/tellraw "+playername+r""" {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> \n玩家互传  帮助菜单\n输入§a.htp list §r查询目前的玩家互传列表\n输入§a.htp tp <数字> §r传送到目标玩家\n输入§a.htp totp §r发起传送命令\n输入§a.htp detotp §r取消发起传送命令"}]}""")
        case ".test":
            thread.start_new_thread(loadFunc, ("timeSleep0.txt", playername, ))
            thread.start_new_thread(loadFunc, ("timeSleep1.txt", playername, ))
            thread.start_new_thread(loadFunc, ("timeSleep2.txt", playername, ))
        case ".test2":
            thread.start_new_thread(loadFunc, ("timeSleep30.txt", playername, ))
            thread.start_new_thread(loadFunc, ("timeSleep31.txt", playername, ))
        case ".setsp" | ".spawnpoint" | ".setSP": #重新设置出生点
            sendcmd("""/tellraw @a[name=%s, tag=mainCity] {"rawtext":[{"text":"<§l§4ERROR§r> §c主城无法设置重生点."}]}""" % playername)
            sendcmd("/execute @a[name=%s, tag=!mainCity] ~ ~ ~ /spawnpoint" % playername)
            sendcmd("""/tellraw @a[name=%s, tag=!mainCity] {"rawtext":[{"text":"<§l§6Ritle§aBlock§r> 已设置"}]}""" % playername)
        case ".stop" | ".restart" | ".reload": #退出
            if playername in adminhigh:
                tellrawText("@a", "§l§6System§r", "§6''.命令''系统正在重启.")
                exitChatbarMenu()
            else:
                tellrawText(playername, "§l§4ERROR§r", "§c权限不足.")
if ".command" in msg and playername in adminhigh:
    sendcmd(msg[9:])
