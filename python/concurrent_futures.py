from concurrent.futures import ThreadPoolExecutor
import time


def func_1() -> None:
    for n in range(3):
        time.sleep(2)
        print(f"func_1 - {n}")

def func_2() -> None:
    for n in range(3):
        time.sleep(1)
        print(f"func_2 - {n}")

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(func_1)
        executor.submit(func_2)


if __name__ == "__main__":
    main()
