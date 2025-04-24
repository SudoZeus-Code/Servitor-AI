
### Windows venv activation

To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called `myenv`, the command would be:

# In cmd.exe

python -m venv myenv

venv\Scripts\activate.bat

pip install transformers torch

# In powershell
python -m venv myenv

Set-ExecutionPolicy Bypass 

myenv\Scripts\activate