import sys
import os
import make_list

def main(args):
    problem = args[1]
    os.chdir(f'../test/{problem}')
    rename_all('in')
    rename_all('out')
    os.chdir('../../bin')
    make_list.make_list(problem)

# ここを定義
def new_name(old_name):
    return old_name.split('.')[0] + '.txt'

def rename_all(path):
    os.chdir(path)
    for old_name in os.listdir():
        os.rename(old_name, new_name(old_name))
    os.chdir('../')

if __name__ == '__main__':
    main(sys.argv)
