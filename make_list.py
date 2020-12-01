import os
import sys

def main(args):
    for problem in args[1]:
        make_list(problem.upper())

def make_list(problem):
    path = '../test/{}'.format(problem)
    file_name_list = os.listdir(path + '/in')

    with open(path + '/list.txt', 'w', newline = '\n') as f:
        f.write('\n'.join(sorted(file_name_list)))

if __name__ == '__main__':
    main(sys.argv)
