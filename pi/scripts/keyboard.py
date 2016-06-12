import termios, fcntl, sys, os
import time
import serial


def main():
    fd = sys.stdin.fileno()
    serr = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)
    serr.close()
    serr.open()
    print serr.readline()
    raw_input()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    cap = 0
    print  "start"
    c = " "
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
            except IOError:
                pass
            sys.stdin.flush()

            print c
            if c == "A":
                print "av"
                serr.write('1530 ')
                send_data = True
            if c == "B":
                print"rec"
                serr.write('1470 ')
                send_data = True
            if c == "D":
                print "gauche"
                cap += 5
                serr.write('2530 ')
                send_data = True
            if c == "C":
                print "droite"
                cap -= 5
                serr.write('2470 ')
                send_data = True
            if c == " ":
                serr.write('1500\n')
                send_data = True
            if c not in ["A", "B", "C", "D"]:
                #print c, "not recognized -> STOP"
                #serr.write('1500 ')
                pass
            if send_data:
                try:
                    data = sys.stdin.readlines()
                    print "disregard", data
                except:
                    pass
                time.sleep(0.2)
                send_data = False

            c = " "
            #while cont:
            #    c = sys.stdin.read(1)
            #    cont = c is not None
            #    print  c
            l = serr.readline()
            if l != "" and l!="\n":
                print "##", l

    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

if __name__ == "__main__":
    main()
