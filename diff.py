import sys
import test

import compile
import create_testcase
import simulate


def main():
    main_language, ans_language = sys.argv[1:3]

    compile.compile(main_language)
    compile.compile(ans_language)

    input_file = '../src/in.txt'

    for i in range(10 ** 5):
        test_case = create_testcase.create_testcase()
        input_ = create_testcase.to_str(test_case)
        create_testcase.write(input_file, input_)
        main_output, main_error = test.execute(main_language, input_file)
        ans_output, _ = test.execute(ans_language, input_file)

        AC = not main_error and (
            main_output == ans_output
            or simulate.simulate(input_, main_output)[0]
        )
        if AC:
            print(i, end = '\r')
        else:
            test.print_diff(
                input_file, test.trim(input_), test.trim(ans_output),
                f'{test.trim(main_output)}\n\n{main_error}'.strip()
            )
            break


if __name__ == '__main__':
    main()
