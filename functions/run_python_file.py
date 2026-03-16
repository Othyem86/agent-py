import os
import subprocess
from google.genai import types


def run_python_file(working_directory: str, file_path:str, args: list[str]=None) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file: str = os.path.normpath(os.path.join(abs_working_dir, file_path))
        is_valid_path = os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir

        if not is_valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        completedProcess = subprocess.run(
            args=command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )
        output_strings: list[str] = []
        if completedProcess.returncode != 0:
            output_strings.append(f"Process exited with code {completedProcess.returncode}")
        if not completedProcess.stdout and not completedProcess.stderr:
            output_strings.append("No output produced")
        if completedProcess.stdout:
            output_strings.append(f"STDOUT:\n{completedProcess.stdout}")
        if completedProcess.stderr:
            output_strings.append(f"STDERR:\n{completedProcess.stderr}")
        return "\n".join(output_strings)
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file (*.py), relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to the python file to be run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional arguments for running the python file",
            ),
        },
    ),
)