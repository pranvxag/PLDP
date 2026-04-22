

file_name = "sample.txt"

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

try:
    with open(file_name, "r") as file:
        content = file.read()

        for ch in content:
            if ch.isalpha():  # check only letters
                if ch in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)

except FileNotFoundError:
    print("File not found. Make sure sample.txt is in the same directory.")