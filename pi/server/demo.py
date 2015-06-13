import urllib2
import time


def square():
    x = 100
    y = 200
    cap = 3.14 / 2
    for i in range(100, 800, 20):
        req(i, y, cap)

    x = 800
    cap = 0
    for i in range(200, 800, 20):
        req(x, i, cap)

    cap = 3.14 / 2
    y = 800
    for i in range(800, 100,  -20):
        req(i, y, cap)

    cap = 0
    x = 0
    for i in range(800, 200, -20):
        req(x, i, cap)


def req(x, y, cap):
    try:
        urllib2.urlopen('http://127.0.0.1:5000/set_big_robot?x={}&y={}&cap={}'.format(x, y, cap))
    except:
        pass
    time.sleep(0.05)

if __name__ == "__main__":
    while True:
        square()

