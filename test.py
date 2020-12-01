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
            print_diff(input_file, expected, actual)
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

def print_diff(input_file, index, expected, actual):
    index = str(index)
    input_file = read(input_file)

    hi = '-' * 11 + 'input' + index + '-' * 12
    he = '-' * 10 + 'expected' + index + '-' * 10
    ha = '-' * 11 + 'actual' + index + '-' * 11
    print(hi, input_file, he, expected, ha, actual, sep = '\n', end = '\n\n')

if __name__ == '__main__':
    main(sys.argv)
