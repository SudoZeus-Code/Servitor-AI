
ollama create serve1 -f ./servitor-modelfile.txt

modelfile:
```
FROM llama3.2
PARAMETER temperature 5
SYSTEM "You are a Servitor of the Omnissiah. Answer as a machine with a purpose."
PARAMETER num_ctx 4096
PARAMETER top_k 50
#PARAMETER personality "Mechanistic"
#PARAMETER tone "Neutral"
#PARAMETER humor "Dry"
#PARAMETER jargon "Yes"
#PARAMETER schematics "Yes"
  
```

python servitor-level1.py
```
import ollama

import subprocess

  

# Define function to interact with Ollama

def ask_ollama(prompt):

    """Sends a message to the Ollama model and returns the response."""

    response = ollama.chat(model="serve1", messages=[{"role": "user", "content": prompt}])

    return response['message']['content']

  

# Define function to execute shell commands

def execute_command(command):

    """Executes a shell command and returns the output."""

    try:

        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)

        return f"Command Output:\n{output}"

    except subprocess.CalledProcessError as e:

        return f"Error executing command:\n{e.output}"

  

def main():

    print("🔹 Servitor Ready. Type 'exit' to quit.")

    while True:

        user_input = input("\n>>> ")

  

        # Exit command

        if user_input.lower() == "exit":

            print("Shutting down...")

            break

        # Check if user wants to run a system command

        if user_input.lower().startswith("execute: "):

            command = user_input[len("execute: "):]  # Extract command

            confirm = input(f"⚠️ Are you sure you want to run `{command}`? (yes/no): ")

            if confirm.lower() == "yes":

                response = execute_command(command)

            else:

                response = "Command execution cancelled."

        else:

            # Ask Ollama for a response

            response = ask_ollama(user_input)

        print(f"\n🟢 Servitor: {response}")

  

if __name__ == "__main__":

    main()
```