from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def main():
    # ...or, in a non-blocking fashion:
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
