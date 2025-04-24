import subprocess
import json
from ollama import Assistant

def execute_command(command):
    try:
        # Executes the terminal command and returns the output
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

# Load the Ollama assistant
assistant = Assistant()

# Define a function to handle AI input and output
def process_input(input_text):
    # If input contains a terminal command (check if it starts with "run:")
    if input_text.startswith("run:"):
        command = input_text[4:].strip()  # Extract the command after "run:"
        return execute_command(command)
    else:
        # Otherwise, process as a normal AI request
        return assistant.chat(input_text)

# Example loop for continuous interaction
if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        response = process_input(user_input)
        print("Response:", response)
