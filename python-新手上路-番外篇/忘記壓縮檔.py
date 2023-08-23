import pyzipper
from multiprocessing import Process
import time

zip_file = pyzipper.AESZipFile("aa.zip", 'r')
zip_flag = False
start_time = time.time()

# 開始破解壓縮檔密碼


def decode(start_pwd, end_pwd):
    global zip_file
    global zip_flag
    for password in range(start_pwd, end_pwd):
        try:
            if zip_flag == False:
                zip_file.extractall(pwd=str(password).encode())
                print('成功破解,密碼：{}'.format(password))
                end_time = time.time()
                print("總共花費{}秒".format(end_time-start_time))
                zip_file.close()
                zip_flag = True
                break
            else:
                break
        except:
            pass


if __name__ == '__main__':
    print("正在破解...")
    process_num = 1  # 設定要使用的process數量
    workload = 12000  # 設定每個process負責破解的密碼數量
    processes = []
    # 建立processes
    for i in range(process_num):
        curr_process = Process(
            target=decode, args=(i*workload, (i+1)*workload))
        processes.append(curr_process)
    # 開始processes
    for p in processes:
        p.start()
    # 等待各process完成
    for p in processes:
        p.join()
