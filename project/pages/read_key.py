import platform
import msvcrt


def read_key():
    system = platform.system()
    if system == "Windows":
        try:
            key = msvcrt.getch().decode()
            return key
        except UnicodeDecodeError:
            key = msvcrt.getch().decode()
            if key == 'H':
                key = 'ARROW_UP'
            elif key == 'P':
                key = 'ARROW_DOWN'
            else:
                key = ''
            return key
    elif system == "Linux":
        pass
