def login():
    # セッション開始
    session = requests.session()

    LOGIN_URL = "https://atcoder.jp/login"

    # csrf_token取得
    r = session.get(LOGIN_URL)
    s = BeautifulSoup(r.text, 'lxml')
    csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

    # パラメータセットses
    login_info = {
        "csrf_token": csrf_token,
        "username": "yama2019",
        "password": "r9N6VAmd4CpDBYikU3wL"
    }

    result = session.post(LOGIN_URL, data=login_info)
    result.raise_for_status()
    if result.status_code==200:
      print("log in!")
    else:
      print("failed...")
    return session
