"""
max_workers=2の状態で並列処理する処理を3つに変更する
"""

from concurrent.futures import ThreadPoolExecutor
import time


def func_1() -> None:
    for n in range(3):
        time.sleep(2)
        print(f"func_1 - {n}")

    return "結果1"

def func_2(x: str, y: str) -> str:
    for n in range(3):
        time.sleep(1)
        print(f"func_2 - {n} ({x}, {y})")

    return "結果2"

def main():
    print("開始")

    with ThreadPoolExecutor(max_workers=2) as executor:
        future_1 = executor.submit(func_1)
        future_2 = executor.submit(func_2, "あ", "A")
        future_3 = executor.submit(func_2, "い", "B")

    result_1 = future_1.result()
    result_2 = future_2.result()

    print(f"result_1: {result_1}")
    print(f"result_2: {result_2}")

    print("終了")


if __name__ == "__main__":
    main()
