import subprocess
import sys

from config import language_dict


def main():
    language = sys.argv[1]
    compile(language)


def compile(language):
    command = language_dict[language]['compile']
    if command:
        res = subprocess.run(command)
        if res.returncode:
            sys.exit(res.returncode)


if __name__ == '__main__':
    main()
