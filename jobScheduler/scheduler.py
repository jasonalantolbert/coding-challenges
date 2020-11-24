import time


def scheduler(f, n: float):
    time.sleep(n / 1000)
    exec(f"f()")
