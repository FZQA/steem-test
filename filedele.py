import os
import shutil
import socket
import re

def del_dir(path):
    if os.path.exists(path+"/database.cfg"):
        os.remove(path+"/database.cfg")
    if os.path.exists(path+"/blockchain"):
        shutil.rmtree(path+"/blockchain")
    if os.path.exists(path + "/logs"):
        shutil.rmtree(path + "/logs")
    if os.path.exists(path + "/p2p"):
        shutil.rmtree(path + "/p2p")

def alter_knip(file, ipaddr = "127.0.0.1"):
    """
    将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字
    :param file: 文件路径
    """
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if "k-number" in line:
                line = 'k-number = ' + str(k) + '\n'
            if "n-number" in line:
                line = 'n-number = ' + str(n) + '\n'
            if ipaddr != re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line):
                line = re.sub(re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"), ipaddr, line)
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

def del_mul_dir(dir):
    ls = os.listdir(dir)
    print(ls)
    for i in ls:
        del_dir(dir + i)

def alter_knip_configini(dir, ipaddr):
    ls = os.listdir(dir)
    print(ls)
    for i in ls:
        alter_knip(dir + i + "/config.ini", ipaddr)

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()
    return ip

k=2
n=3
#递归遍历/root目录下所有文件
testdir = '/home/fzqa/a-vssgstest/onehost-3node/'
del_mul_dir(testdir)
#
ip = get_host_ip()
print(ip)
alter_knip_configini(testdir, ip)