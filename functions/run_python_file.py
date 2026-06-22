import os
import subprocess

def run_python_file(working_directory, file_path, args = []): # arsg is default parameter for passing input strings
    abs_working_dir = os.path.abspath(working_directory)  # file path of directory
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))  # file path with text file lorem
 
    if not abs_file_path.startswith(abs_working_dir): # esures valid file path is made
        return f'Error: "{file_path}" is not in the working directory'
    
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file' 
    
    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(final_args, cwd = abs_working_dir, timeout = 90, capture_output = True)
        final_string = f"""

        STDOUT: {output.stdout}
        STDERR: {output.stderr}
        """

        if output.stdout == "" and output.stderr == "":
            final_string = "No output produced.\n"
        if output.returncode != 0:
            final_string += f'Process exited with code {output.returncode}'
        return final_string
        
    except Exception as e:
        return f'Error: executing Python file: {e}'