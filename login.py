from my_requests import AtCoderSession

def main():
    session = AtCoderSession(login = True)
    session.save_cookies()

if __name__ == '__main__':
    main()
