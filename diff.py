import sys
import compile
import create_testcase
from config import language_dict
import test 

def main():
    main_language, ans_language = sys.argv[1:3]
    
    compile.compile(main_language)
    compile.compile(ans_language)

    input_file = '../src/in.txt'

    for i in range(10 ** 5):
        test_case = create_testcase.create_testcase()
        input_ = create_testcase.to_str(test_case)
        create_testcase.write(input_file, input_)
        main_output = test.execute(main_language, input_file)
        ans_output = test.execute(ans_language, input_file)
        if main_output != ans_output:
            test.print_diff(input_file, input_, ans_output, main_output)
            break
        else:
            print(i, end = '\r')

if __name__ == '__main__':
    main()
