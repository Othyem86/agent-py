from functions.get_files_info import get_files_info

def test():
    print(f"Result for current directory:")
    print(get_files_info("calculator", "."))
    print()

    print(f"Result for 'pkg' directory:")
    print(get_files_info("calculator", "pkg"))
    print()

    print(f"Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))
    print()

    print(f"Result for '../' directory:")
    print(get_files_info("calculator", "../"))
    print()

if __name__ == "__main__":
    test()