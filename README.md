# できること
- [サンプルデータのダウンロード](#サンプルデータのダウンロード)
- [自動テスト](#テスト提出)
- [提出](#テスト提出)

# 環境
- `OS`: Windows, Mac, Linux等
- `Python3`
    - `requests`
    - `bs4`
    - `lxml`


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
- `build`: 実行ファイルの保存先
- `src`: ソースファイルの保存先
- `test`: サンプルデータの保存先

# 初期設定
- `bin`内に`private.py`というファイルを追加し，以下を記入して保存．
    ```python
    login_data = {'username': 'ユーザーネーム', 'password': 'パスワード'}
    rust_path = 'Rustのprojectパス'    
    ```
    - `Rust`を使わない場合は，`''`でよい．


# サンプルデータのダウンロード
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
```shell
$ python atcoder.py [language] [task] [option]
```
- `language`: 用いた言語．
    - `config.py`の`language_dict`の`key`に登録されているもの．
    - `language_dict`にない場合は，適宜追加すればよい．
- `task`: 解いた問題
    - 例: `A`, `B`, ...
- `option`
    - `n`: テストに通っても提出しない．
    - `f`: 強制的に提出する．
- `language`, `task`は，大文字小文字を区別しない．
