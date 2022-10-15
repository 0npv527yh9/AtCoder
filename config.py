source_path = '../src'
build_path = '../build'
execute_command = f'{build_path}/a.exe'

from private import rust_path

language_dict = {
    'c': {
        'extension': 'c',
        'compile': ['gcc', f'{source_path}/main.c', '-o', execute_command],
        'execute': execute_command,
        'id': '4001'
    },
    'c++': {
        'extension': 'cpp',
        'compile': ['g++', f'{source_path}/main.cpp', '-o', execute_command],
        'execute': execute_command,
        'id': '4003'
    },
    'java': {
        'extension': 'java',
        'compile': ['javac', '-d', build_path, f'{source_path}/Main.java'],
        'execute': ['java', '-cp', build_path, 'Main'],
        'id': '4005'
    },
    'python': {
        'extension': 'py',
        'compile': None,
        'execute': ['python', f'{source_path}/main.py'],
        'id': '4006'
    },
    'ocaml': {
        'extension': 'ml',
        'compile': None,
        'execute': ['ocaml', f'{source_path}/main.ml'],
        'id': '4039'
    },
    'rust': {
        'extension': 'rs',
        'compile': ['cargo', 'build', '-q', '--manifest-path', f'{rust_path}/Cargo.toml'],
        'execute': f'{rust_path}/target/debug/rust.exe',
        'id': '4050'
    },
    'pypy': {
        'extension': 'py',
        'compile': None,
        'execute': ['pypy', f'{source_path}/main.py'],
        'id': '4047'
    }
}

from contest import title, prefix

option_dict = {
    'test': True,
    'submit': True,
    'title': title,
    'prefix': prefix
}
