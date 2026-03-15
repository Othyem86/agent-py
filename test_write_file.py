from functions.write_file import write_file


def test() -> None:
    working_dir = "calculator"
    write_data = [
        ("lorem.txt", "wait, this isn't lorem ipsum"),
        ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("/tmp/temp.txt", "this should not be allowed")
    ]
    for data in write_data:
        file_name = data[0]
        data_to_write = data[1]
        result = write_file(working_dir, file_name, data_to_write)
        print(result)

if __name__ == "__main__":
    test()