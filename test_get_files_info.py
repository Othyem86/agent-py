from functions.get_files_info import get_files_info

def test() -> None:
    working_dir = "calculator"
    directories = [".", "pkg", "/bin", "../"]

    for dir in directories:
        print(f"Result for '{dir}':")
        print(get_files_info(working_dir, dir))
        print()

if __name__ == "__main__":
    test()