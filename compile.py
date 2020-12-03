import sys
import subprocess
from config import language_dict


def main(args):
    language = args[1]
    compile(language)

def compile(language):
    command = language_dict[language]['compile']
    if command:
        try:
            subprocess.run(command, check = True)
        except:
            sys.exit(1)

if __name__ == '__main__':
    main(sys.argv)
