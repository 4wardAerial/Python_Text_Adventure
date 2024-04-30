import time

def print_fast(text):
    """Prints and waits a small interval. Used for quick texts.
    """
    print(text)
    time.sleep(1)


def print_med(text):
    """Print and waits a slight bigger interval. Used for dialogues.
    """
    print(text)
    time.sleep(2)


def print_long(text):
    """Prints and waits a big interval. Used for dramatic pauses.
    """
    print(text)
    time.sleep(4)
