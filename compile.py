import subprocess
import sys

from config import language_dict


def compile(language):
    try:
        command = language_dict[language]['compile']
    except:
        print(f'Info for {language} is not found in "config.py".')
        print(f'Add info for {language} with reference to the others.')
        exit(0)
    if command:
        res = subprocess.run(command)
        if res.returncode:
            sys.exit(res.returncode)
