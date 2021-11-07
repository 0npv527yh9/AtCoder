import os
import sys
from my_requests import AtCoderSession
from contest import title, prefix
from config import language_dict

def main(args):
    top_url = 'https://atcoder.jp'

    problem = args[1].lower()
    language = args[2].lower()
    languageID = language_dict[language]['id']
    extension = language_dict[language]['extension']
    
    session = AtCoderSession()
    
    table_url = f'{top_url}/contests/{title}/submissions?f.Language={languageID}&f.Status=AC&f.Task={prefix}_{problem}&orderBy=time_consumption'
    session.get(table_url)

    submission_url = url = top_url + session.soup.tbody.tr.find_all('td')[-1].a['href']
    session.get(submission_url)

    code = session.soup.find('pre', id = 'submission-code').text.replace('\r', '')
    write('../src/main.' + extension, code)

def write(file, s):
    with open(file, 'w', encoding = 'utf-8', newline = '\n') as f:
        f.write(s)

if __name__ == '__main__':
    main(sys.argv)


