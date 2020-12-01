import subprocess
import sys

cmd_dict = \
    {  'java': 'java -cp ../build Main',
     'python': 'python ../src/main.py',
          'c': '../build/a.exe'}

def main(args):
    language = args[1]
    problem = args[2].upper()
    judge(language, problem)

def read(file):
    with open(file) as f:
        return f.read().strip()

def judge(language, problem):
    cmd = cmd_dict[language]
    test_home = '../test/' + problem

    sample_file_list = read(test_home + '/list.txt').split('\n')

    WA = False

    for sample_file in sample_file_list:
        input_file = test_home + '/in/' + sample_file
        output_file = test_home + '/out/' + sample_file

        actual = execute(cmd, input_file)
        expected = read(output_file)

        if expected != actual:
            input_ = read(input_file)
            print_diff(sample_file, input_, expected, actual)
            WA |= True

    if not WA:
        print('AC')

def execute(cmd, input_file):
    try:
        byte_res = subprocess.check_output(cmd, stdin = open(input_file))
        str_res = byte_res.decode().strip().replace('\r', '')
        return str_res
    except:
        exit(0)

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
