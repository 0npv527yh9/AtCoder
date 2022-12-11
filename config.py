source_path = '../src'
file_prefix = f'{source_path}/main.'
build_path = '../build'
execute_command = f'{build_path}/a.exe'

from language_id import language_id

language_dict = {
    'c':
        {
            'file': file_prefix + 'c',
            'compile': ['gcc', file_prefix + 'c', '-o', execute_command],
            'execute': execute_command,
            'id': language_id['C']
        },
    'c++':
        {
            'file': file_prefix + 'cpp',
            'compile': ['g++', file_prefix + 'cpp', '-o', execute_command],
            'execute': execute_command,
            'id': language_id['C++']
        },
    'java':
        {
            'file': file_prefix + 'java',
            'compile': ['javac', '-d', build_path, file_prefix + 'java'],
            'execute': ['java', '-cp', build_path, 'Main'],
            'id': language_id['Java']
        },
    'python':
        {
            'file': file_prefix + 'py',
            'compile': None,
            'execute': ['python', file_prefix + 'py'],
            'id': language_id['Python']
        },
    'ocaml':
        {
            'file': file_prefix + 'ml',
            'compile': None,
            'execute': ['ocaml', file_prefix + 'ml'],
            'id': language_id['OCaml']
        },
    'pypy':
        {
            'file': file_prefix + 'py',
            'compile': None,
            'execute': ['pypy', file_prefix + 'py'],
            'id': language_id['PyPy3']
        },
    'rust':
        {
            'file': f'{source_path}/rust/src/main.rs',
            'compile':
                [
                    'cargo', 'build', '--quiet', '--manifest-path',
                    f'{source_path}/rust/Cargo.toml'
                ],
            'execute': [f'{source_path}/rust/target/debug/rust.exe'],
            'id': language_id['Rust']
        }
}

task_info_file = 'task_info.json'
