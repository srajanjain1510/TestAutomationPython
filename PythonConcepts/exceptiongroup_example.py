
from pathlib import Path
from exceptiongroup import ExceptionGroup
import os

path_cwd = os.getcwd()
print(path_cwd)
eg = ExceptionGroup("Exception Occured",[ConnectionError('Connection Error'),FileNotFoundError("File not found"),NameError('File Name Incorrect')])
try:

    file_path = Path(path_cwd,'new_exception','.trxt')
    with open(file_path) as file:
        a = file.read()

except* FileNotFoundError as f:
    print("f")
except* ConnectionError as c:
    print('c')
except* NameError as n:
    print('n')

