# できること
- [サンプルデータのダウンロード](#サンプルデータのダウンロード)
- [自動テスト](#テスト提出)
- [提出](#テスト提出)

# 使用言語/ライブラリ
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

## ログイン
```shell
$ python login.py
```
- AtCoderのサイトにアクセスできるようにする．
- `cookies.pickle`にクッキーが保存され，次回以降はそれを読み込む．


# サンプルデータのダウンロード
```shell
$ python3 load_testcase.py [url] [hour] [minute] 
```
- `url`: コンテストのトップページ，または問題ページのURL．
    - 例: `https://atcoder.jp/contests/abc272`
    - 例: `https://atcoder.jp/contests/abc272/tasks/abc272_a`
    - トップページの場合，すべての問題がダウンロードされる．
- `hour`, `minute`: 開始時刻．
    - **省略可能**．
    - デフォルトは`21 00`．

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