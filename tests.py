from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_dir = "calculator"

#get_file_content test 
    # print(get_file_content(working_dir, "main.py"))
    # print(get_file_content(working_dir, "pkg/calculator.py"))
    # print(get_file_content(working_dir, "pkg/noteexists.py"))
    # print(get_file_content(working_dir, "/bin/cat"))

#write_file test
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "pkg2/temp.txt", "this should be allowed"))

#run_python file 

    print(run_python_file(working_dir, "main.py", ["3 + 5"]))
    # print(run_python_file(working_dir, "tests.py"))
    # print(run_python_file(working_dir, "../main.py"))
    # print(run_python_file(working_dir, "nonexistent.py"))

main()



 