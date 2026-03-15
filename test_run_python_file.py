from functions.run_python_file import run_python_file

def test() -> None:
    working_dir = "calculator"
    run_data = [
        ("main.py", None),
        ("main.py", ["3 + 5"]),
        ("tests.py", None),
        ("../main.py", None),
        ("nonexistent.py", None),
        ("lorem.txt", None),
    ]
    for data in run_data:
        command = data[0]
        args = data[1]
        result = run_python_file(working_dir, command, args)
        print(result)

if __name__ == "__main__":
    test()