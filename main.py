import os
import sys
from dotenv import load_dotenv
from google import genai  #google sdk
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_files_info import schema_get_files_info
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")  # api key extraction
    # print("API key : ", api_key)

    client = genai.Client(api_key = api_key)
    system_prompt =   """
            You are a helpful AI coding agent.

            When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

            - List files and directories

            All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

        """

    if len(sys.argv) < 2:
        print("Enter prompt completely!!")
        sys.exit(1)

    verbose_Flag = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_Flag = True
    
    prompt = sys.argv[1]
   # print("Args", sys.argv) # sys argv for extracting sys arguements
    
    messages = [ types.Content(role="user", parts = [types.Part(text= prompt)])]  #A1

    available_functions = types.Tool(
        function_declarations=[schema_get_files_info],
    )

    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config = config, # types.GenerateContentConfig(system_instruction = system_prompt),

    )


    if response is None or response.usage_metadata is None:
        print("Invalid response")
        return
    
    if verbose_Flag :

        print(f"User Prompt : {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    
    if response.function_calls:
        for function_call_part in response.function_calls:
            print(
                f"Calling function: {function_call_part.name}({function_call_part.args})"
            )   
    else: 
        print(response.text)
 

# print(get_files_info("calculator"))
# if __name__ == "__main__":  
main()




# """ triple quotes for multiline string
#     otherwise need to use one double quotes and /n
#     to enter for new line"""

# sys.argv --> for extracting command line arguements

# TO CHECK TOKEN USED
#     print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#     print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

# A1

# User: What is Python?
# Assistant: Python is a programming language.
# User: Give an example.

# messages = [
#     {"role": "user", "content": "Hi"},
#     {"role": "model", "content": "Hello"},
#     {"role": "user", "content": "Explain Java"}
# ]


# verbose_flag
#   if user asks for rate limit detail only we display them.
#   they ask by --verbose after the prompt "what is 10 + 8" --verbose

