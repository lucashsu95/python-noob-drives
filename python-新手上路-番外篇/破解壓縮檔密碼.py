import zipfile
import itertools


# 破解一个4位数密码数字和字母为23ab大概5-10分钟。
dictionaries = [chr(i + 97) for i in range(26)] + [chr(i + 65) for i in range(26)] + [str(i) for i in range(10)]  # 组戳numbers和letters的共同字共同组戳numbers和letters的
end_for = True      # 用于破解成功后，停止循环的变量
# 设置密码的长度1到16位密码
for x in range(1, 17):
    if end_for:
        def allkeyword():
            allkey1 = itertools.product(dictionaries, repeat=x)
            allkey2 = (''.join(i) for i in allkey1)
            return allkey2

        def trypassword(password):
            try:
                ZIPFILE = zipfile.ZipFile(
                    'aa.zip')   # 需要解压带有密码的本地abc.zip
                ZIPFILE.extractall(
                    path=r'./result', pwd=password.encode('utf-8'))     # 解压到哪个路径下
                print(f"解压成功,正确密码为：{password}")       # 解压成功，并打印出正确密码
                global end_for      # 声明为全局变量，没有声明，重新赋值无效
                end_for = False     # 解压成功，停止循环
                return True
            except:
                print(f"解压失败,尝试密码为：{password}")
                return False

        # 用trypassword函数返回的True或者Flase来判定程序是否终止。
        for pwd in allkeyword():
            if trypassword(pwd):
                break
