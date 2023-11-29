## Gitとは
- コメント: バージョン管理の仕組みも書きたい
- https://tetoblog.org/2021/06/git-how/
- https://techtoge.com/summary-what-is-git/

## 使い方
### 参照ページ
- https://www.sejuku.net/blog/70775　を参照した。
- https://codelikes.com/git-commit-push/　も参考になりそう。
- https://tetoblog.org/category/programming/syntax/git/

### 主な使い方
1. リモートリポジトリの作成（これはGUIで作成する）
   1. リモートリポジトリを作成したあと、ライセンスファイルを選択しなかった場合、以降で打つべきコマンドをGitHubが教えてくれる。
2. ローカルリポジトリの作成（ローカル環境でターミナルを使って作成する）
   1. `mkdir <ディレクトリ名> && cd <ディレクトリ名>`
      1. 任意の場所にディレクトリを作成して、作成したディレクトリに移動する。
   2. `git init`
      1. ローカルリポジトリの初期化
      2. `Initialized empty Git repository in ~` と表示されればOK
3. ファイルを新規に作成して、それをローカルリポジトリに登録してみる
   1. ファイルを新規に作成する。
   2. `git add` でファイルをインデックスに追加する。この操作によって、Gitで管理する対象とすることができる（`git add` にはオプションがあるので、適宜使い分ける）以下は一例。
      1. `git add -A`: 全てのファイルを追加
      2. `git add .`: カレントディレクトリ配下の全てのファイルを追加
      3. `git add -u`: 変更のあった全てのファイルを追加
   3. `git commit -m "<コミットメッセージ>"` でローカルリポジトリに追加する。