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

    count =0
    sample_file_list = read(test_home + '/list.txt').split('\n')


    for index, sample_file in enumerate(sample_file_list, 1):
        input_file = test_home + '/in/' + sample_file
        actual = execute(cmd, input_file)

        output_file = test_home + '/out/' + sample_file
        expected = read(output_file)

        if expected != actual:
            count += 1
            print_diff(input_file, index, expected, actual)

    if count == len(sample_list):
        print('AC')

def execute(cmd, input_file):
    try:
        return subprocess.check_output(cmd, stdin = open(input_file)).decode().strip().replace('\r', '')
    except:
        exit(0)

def print_diff(input_file, index, expected, actual):
    input_file = read(input_file)

    hi = '-' * 11 + 'input' + index + '-' * 12
    he = '-' * 10 + 'expected' + index + '-' * 10
    ha = '-' * 11 + 'actual' + index + '-' * 11
    print(hi, sample_input, he, expected, ha, actual, sep = '\n', end = '\n\n')

if __name__ == '__main__':
    main(sys.argv)
