from functions.get_file_content import get_file_content

def test() -> None:
    working_dir = "calculator"
    files = [
        "main.py", 
        "pkg/calculator.py", 
        "/bin/cat", ""
        "pkg/does_not_exist.py"
    ]

    lorem_len = len(get_file_content(working_dir, "lorem.txt"))
    print(f"Length of 'lorem.txt': {lorem_len}")
    print()

    for file in files:
        print(f"Content in '{file}':")
        print(get_file_content(working_dir, file))
        print()

if __name__ == "__main__":
    test()