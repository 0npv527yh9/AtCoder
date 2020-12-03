import subprocess
import sys
from config import language_dict

def main(args):
    problem = args[1].upper()
    language = args[2]
    test(problem, language)

def test(problem, language):
    test_home = '../test/' + problem

    sample_file_list = read(test_home + '/list.txt').split('\n')

    WA = False

    for sample_file in sample_file_list:
        input_file = test_home + '/in/' + sample_file
        output_file = test_home + '/out/' + sample_file

        actual = execute(language, input_file)
        expected = read(output_file)

        if expected != actual:
            input_ = read(input_file)
            print_diff(sample_file, input_, expected, actual)
            WA = True

    if WA:
        sys.exit(1)
    else:
        print('AC')

def read(file):
    with open(file) as f:
        return f.read().strip()

def execute(language, input_file):
    try:
        command = language_dict[language]['execute']
        option = {
            'stdin': open(input_file),
            'stdout': subprocess.PIPE,
            'check': True
        }
        byte_res = subprocess.run(command, **option).stdout.strip()
        str_res = byte_res.decode().replace('\r', '')
        return str_res
    except:
        sys.exit(1)

def print_diff(file, input_, expected, actual):
    title_tuple = ('input', 'expected', 'actual')
    content_tuple = (input_, expected, actual)

    print(make_title(file, '='))
    for title, content in zip(title_tuple, content_tuple):
        print(make_title(title), content, sep = '\n')
    print('\n')

def make_title(title, style = '-', width = 30):
    w = max(0, width - len(title))
    l = w // 2
    r = w - l
    return style * l + title + style * r

if __name__ == '__main__':
    main(sys.argv)
