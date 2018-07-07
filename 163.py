import yagmail
yag = yagmail.SMTP(user='88888@163.com', password='000000', host='smtp.163.com')
boby = "老师，你好！这是最近工作的文件，请查收。"
yag.send(to='88888@163.com.cn', cc = '888888@163.com',subject='工作文件', contents =[boby,'C:/Users/8888/Pictures/1520058767235.jpg','C:/Users/88888/Pictures/1520058765902.jpg'])
print("已发送邮件")

#运行前需要更改密码为授权码

'''
import yagmail

username = 'sdfsfd@163.com'#邮箱账号
passwd = 'sdfsdfsd'#授权码，不是邮箱密码
mail = yagmail.SMTP(user=username,
                    password=passwd,
                    host='smtp.163.com',#其他服务器就smtp.qq.com  smtp.126.com
                    # smtp_ssl=True
                    ) #如果用的是qq邮箱或者你们公司的邮箱使用是安全协议的话，必须写上 smtp_ssl=True
mail.send(
    to=['123456789@qq.com','125555555@qq.com'], #如果多个收件人的话，写成list就行了，如果只是一个账号，就直接写字符串就行to='12345678@qq.com'
    cc='735557314@qq.com',#抄送
    subject='学习发送邮件',#邮件标题
    contents='你好，你今天开心吗？',#邮件正文
    attachments=[r'C:\Users\Desktop\a.txt',
                 r'C:\pp\b.txt'])#附件如果只有一个的话，用字符串就行，attachments=r'C:\\pp\\b.txt'
print('发送成功')
'''