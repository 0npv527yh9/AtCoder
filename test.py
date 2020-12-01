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

def judge(language, problem):
    cmd = cmd_dict[language]
    path = '../test/' + problem

    with open(path + '/list.txt') as f:
        sample_list = f.read().strip().split('\n')

    count =0

    for index, sample in enumerate(sample_list):
        sample_input = path + '/in/' + sample
        sample_output = path + '/out/' + sample

        actual = execute(cmd, sample_input)

        with open(sample_output) as f:
            expected = f.read().strip()

        if expected != actual:
            print_diff(sample_input, str(index + 1), expected, actual)
        else:
            count += 1

    if count == len(sample_list):
        print('AC')

def execute(cmd, input_file):
    try:
        return subprocess.check_output(cmd, stdin = open(input_file)).decode().strip().replace('\r', '')
    except:
        exit(0)

def print_diff(input_file, index, expected, actual):
    with open(input_file) as f:
        sample_input = f.read().strip()

    hi = '-' * 11 + 'input' + index + '-' * 12
    he = '-' * 10 + 'expected' + index + '-' * 10
    ha = '-' * 11 + 'actual' + index + '-' * 11
    print(hi, sample_input, he, expected, ha, actual, sep = '\n', end = '\n\n')

if __name__ == '__main__':
    main(sys.argv)
