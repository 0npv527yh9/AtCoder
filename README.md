# できること
- AtCoderの問題を解いたプログラムのテスト/提出．

## メイン
- [テストケースのダウンロード](#テストケースのダウンロード)
- [自動テスト](#テスト提出)
- [提出](#テスト提出)

## その他
- [実行時間が短い順に提出結果を表示](#実行時間が短い順に提出結果を表示)
- [直近に開催されるコンテストのトップページを開く](#直近に開催されるコンテストのトップページを開く)


# 環境
- `OS`: Windows, Mac, Linux等
- `Python3`
    - `requests`
    - `bs4`
    - `lxml`

# インストール
```shell
$ git clone git@github.com:0npv527yh9/AtCoder.git bin
$ cd bin
```
- リポジトリの名前を`bin`にして`clone`．

# ローカルでの階層
<pre>
.
├── bin
├── build
|   └── a.exe
├── src
│   └── main.cpp
└── test

</pre>
- `bin`: このrepository
- `build`: 実行ファイルの保存先．(**要作成**)
- `src`: ソースファイルの保存先．(**要作成**)
- `test`: テストケースの保存先．
- `build`と`src`は，必ず作成してください．

# 初期設定
- `bin`内に`private.py`というファイルを追加し，AtCoderのアカウント情報を以下のように記入して保存．
    ```python
    login_data = {'username': 'ユーザーネーム', 'password': 'パスワード'}
    ```
- このファイルは，Gitの管理対象外．

# テストケースのダウンロード
```shell
$ python load_testcase.py [url] [hour] [minute] 
```
- `url`: コンテストのトップページ，または問題ページのURL．
    - 例: `https://atcoder.jp/contests/abc272` (トップページ)
    - 例: `https://atcoder.jp/contests/abc272/tasks/abc272_a` (問題Aのページ)
    - トップページの場合，すべての問題がダウンロードされる．
- `hour`, `minute`: ダウンロードを開始する時刻．
    - **省略可能**．省略すると即時ダウンロード開始．
    - `minute`のデフォルトは，`0`．

## 例: これから開始されるコンテストに参加する場合
```shell
$ python load_testcase https://atcoder.jp/contests/abc272 21
```
- 21:00に始まるコンテストに参加予定で，21:00より前に実行する場合

## 例: すでに開始されたコンテストの場合
```shll
$ python load_testcase https://atcoder.jp/contests/abc272
```
- すぐにダウンロードが始まる．
- コンテスト開始後や過去問を解く場合


# テスト/提出
- コンパイル，テストし，全て通れば，提出する．
- 自分の提出画面を開く．
```shell
$ python atcoder.py [language] [task] [option]
```
- `language`: 用いた言語．
    - `config.py`の`language_dict`の`key`に登録されているもの．
    - `language_dict`にない場合は，適宜追加すると使えるようになる．
- `task`: 解いた問題
    - 例: `A`, `B`, ...
- `option`
    - `n`: テストに通っても提出しない．
    - `f`: 強制的に提出する．
- `language`, `task`は，大文字小文字を区別しない．

## 例: テストに通り，提出される場合
```shell
$ python atcoder.py python A
AC
Submitted
```
- その後，自分の提出結果のページが開く．


## 例: テストに通らなかった場合
```shell
$ python atcoder.py python A
===============1.txt===============
---------------input---------------
vvwvw
--------------expected-------------
7
---------------actual--------------
5
```
- 不正解のケースについて，以下を表示する．
    - `input`: 入力
    - `expected`: 期待された出力
    - `actual`: 実際の出力


# 実行時間が短い順に提出結果を表示
```shell
$ python rank.py [task] [language]
```
- 提出結果のページを開き，以下を指定して実行時間が短い順に表示
    - 問題: `task`
    - 言語: `language`
    - 結果: `AC`


# 直近に開催されるコンテストのトップページを開く
```shell
$ python next_contest.py
```
