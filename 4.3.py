text = input("Enter a string: ")

punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

for p in punctuations:
    text = text.replace(p, "")

print("After removing punctuation:", text)
