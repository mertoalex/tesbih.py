import sys, os

def wait_key(): # https://stackoverflow.com/questions/983354/how-do-i-wait-for-a-pressed-key
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getwch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

def go_up(): # https://stackoverflow.com/questions/52079846/how-to-hide-input-in-python-3-6
	'''goes a line up'''
	sys.stdout.write("\033[F");
