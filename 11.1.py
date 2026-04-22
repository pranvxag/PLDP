
file_name = "sample.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        char_count = len(content)

    print("Total number of characters in the file:", char_count)

except FileNotFoundError:
    print("File not found. Make sure sample.txt is in the same directory.")