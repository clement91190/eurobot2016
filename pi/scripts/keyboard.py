import termios, fcntl, sys, os
import serial 


def main(): 
    fd = sys.stdin.fileno()
    serr = serial.Serial('/dev/ttyUSB7', 9600, timeout=0.1)
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

    try:
        while 1:
            try:
                c = sys.stdin.read(1)
                if c == "A":
                    print "av"
                    serr.write('1550\n')
                if c == "B":
                    print"rec"
                    serr.write('1450\n')
                if c == "D":
                    print "gauche"
                    cap += 5
                    serr.write('2530\n')
                if c == "C":
                    print "droite"
                    cap -= 5
                    serr.write('2470\n')
                if c == "d":
                    serr.write('D\n')
                if c not in ["A", "B", "C", "D"]:
                    print c, "not recognized -> STOP"
                    serr.write('1500\n')
            except IOError: pass
            l = serr.readline()
            if l != "" and l!="\n":
                print "##", l

    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

if __name__ == "__main__":
    main()