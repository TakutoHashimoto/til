# concurrent.futures
* [documentation](https://docs.python.org/ja/3/library/concurrent.futures.html)

## 並列処理とは
### 今までのコード
* 上から順に処理が実行される（逐次処理）
  * 前の処理が終わってから次の処理が実行される。
    ```python
    with open("./text1.txt") as f:
        x = f.read()
    
    with open("./text2.txt") as f:
        x = f.read()
    ```
* 上記の例のような場合、同時に2つのファイルを読み込んで、処理時間を短縮させたいと思う。

* 複数の作業者がそれぞれ同時に処理をこなすことを **並列処理** という。単一の作業者が処理の待ち時間を利用して、別の処理を行うことを **並行処理** という。

## マルチスレッドとマルチプロセス
### マルチプロセス
* 複数のプロセス（コンピュータ上で動いている処理の単位）を扱う。
* 並列処理を実現する。
* CPUリソースを大量に消費するような処理（大量の数値計算処理など）に使う。
  * CPUバウンドな処理という。

### マルチスレッド
* 複数のスレッド（プロセスの中をさらに分割した処理の単位）を扱う。
* 並行処理を実現する。
* 待ち時間が長いような処理（WebAPIの利用、ディスクへの書き込み）に使う。
  * I/Oバウンドな処理という。

### Pythonでの実装方法
* マルチスレッドは **multiprocessing**
* マルチプロセスは **threading**
* Python3.2以降はこれらをまとめた **concurrent.futures** を使う。