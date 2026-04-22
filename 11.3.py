
file_name = "sample.txt"

try:
    with open(file_name, "r") as file:
        content = file.read().lower()  # convert to lowercase

        words = content.split()  # split into words
        word_count = {}

        for word in words:
            word = word.strip(".,!?;:\"'()[]{}")  # remove punctuation

            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    print("Word Frequencies:\n")
    for word, count in word_count.items():
        print(word, ":", count)

except FileNotFoundError:
    print("File not found. Make sure sample.txt is in the same directory.")