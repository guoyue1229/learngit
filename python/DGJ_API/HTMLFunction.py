import datetime
import hashlib
import random
import time

ExcuteMsg = None


def GetSign(JsonData, token=None):
    arr = []
    DataStr = ""
    for i in sorted(JsonData):
        if i == 'Signature':
            continue
        arr.append(i)  # 遍历字典的key
    for i in arr:
        if JsonData[i] == "":
            # 参数为空不参与签名a
            continue
        DataStr = DataStr + i + "=" + str(JsonData[i]) + "&"
    if token is None:
        # 去掉最后一位
        DataStr = DataStr[:-1]
    else:
        DataStr = DataStr + "key=" + token
    return hashlib.md5(DataStr.encode(encoding='UTF-8')).hexdigest().upper()


def GetTime(Time=None):
    '''
    :param Time:True 10位时间戳 False13位时间戳
    :return:
    :random.randint(1，999)防止直接命中缓存
    '''
    if Time == 1:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if Time is None:
        return time.strftime("%Y-%m-%d", time.localtime())
    if Time is True:
        return str(int(time.time()) + random.randint(1, 999))
    else:
        return str(int(time.time() * 1000) + random.randint(1, 999))


def GetNonce(Num):
    '''
    :param Num: 随机字符的长度
    :return:
    '''
    seed = "1234567890abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(Num):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


def GetLocalTime():
    # 获取当前时间
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def GetBeforeTime(days):
    # 获取几天前的时间
    # 先获得时间数组格式的日期
    threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days))
    # 转换为时间戳
    int(time.mktime(threeDayAgo.timetuple()))
    # 转换为其他字符串格式
    return threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(GetTime(1))
    print(GetTime(False))
