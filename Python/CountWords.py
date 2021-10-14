import os
import re

# Check if the target file exists
path = "C:\\...\\Python\\subtitle - 1.1.txt"
os.path.isfile(path)

# Call words' list with duplication
document_raw = open(path, 'r')
document_lower = document_raw.read().lower()
words_duplication = re.findall(r'\b[a-z]{3,15}\b', document_lower)
# Regular expression to avoid meaningless or wrong words

# Remove duplication from the list
words = set(words_duplication)
print(len(words))