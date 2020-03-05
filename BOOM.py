#该代码需要安装pywin32库
'''
Version: 0.92 alpha
'''
import win32gui
import win32con
import win32clipboard as w



def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 将消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 测试

#to_who='test'              #群名称
print('推荐语言：'+'你爸当初心态失衡的时候我忘劝了，四处放荡，没给你爹少带帽子，还给你传了个入脑的老梅毒\n')#要发的消息
print("骚话来源：https://nmsl.shadiao.app/")

print()
print()
       
xunhuangcishu = int(input("请输入发送次数："))

msg = input("请输入需要发送的文本：")

to_who = input("请输入需要轰炸的群名称：")

for i in range(xunhuangcishu):
#循环执行**次
    send_qq(to_who, msg)

