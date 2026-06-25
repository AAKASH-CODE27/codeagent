import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)  # file path of directory
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))  # file path with text file lorem
 
    if not abs_file_path.startswith(abs_working_dir): # esures valid file path is made
        return f'Error: "{file_path}" is not in the working directory'
    
    if not os.path.isfile(abs_file_path): # ensures file path is valid here 
        return f'Error: "{file_path}" is not a file'
    
    file_content_string = ""
    
    try:
        with open(abs_file_path, "r") as f :
            file_content_string = f.read(MAX_CHARS)

            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (
                    f'[...File"{file_path}" truncated at 10000 characters]'
                )
        return file_content_string
    except Exception as e:
        return f"Exception reading file: {e}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of the given file as a string, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description=" The file_path to list files from the working directory. If not Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)


# os -> The os module gives Python tools to work with files and folders.
# os.path.abspath(folder)  -> gets file math 

