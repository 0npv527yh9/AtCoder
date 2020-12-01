import os
import sys

def make_list(problem):
    path = '../test/{}'.format(problem)
    file_name_list = os.listdir(path + '/in')

    with open(path + '/list.txt', 'w', newline = '\n') as f:
        f.write('\n'.join(sorted(file_name_list)))

if __name__ == '__main__':
    make_list(sys.argv[1])
