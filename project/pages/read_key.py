import platform
import msvcrt


def read_key():
    system = platform.system()
    if system == "Windows":
        try:
            key = msvcrt.getch().decode()
            if key == '\r':
                key = 'ENTER'
            elif key == '\x1b':
                key = 'ESC'
            return key
        except UnicodeDecodeError:
            key = msvcrt.getch().decode()
            if key == 'H':
                key = 'ARROW_UP'
            elif key == 'P':
                key = 'ARROW_DOWN'
            elif key == 'K':
                key = 'ARROW_LEFT'
            elif key == 'M':
                key = 'ARROW_RIGHT'
            else:
                key = ''
            return key
    elif system == "Linux":
        pass
