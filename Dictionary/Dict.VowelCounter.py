#Count numebr of vowels in a word
print("Vowel Counting Project")
word=input("Enter a word or sentence:").lower()
dictVowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}

for letter in word: #read each letter of word
    if letter in dictVowels: #check for matches in dict. keys
        dictVowels[letter]+=1 #if found, add to value

for l in dictVowels: #read all keys
    print(f"Number of '{l}' in the word = {dictVowels[l]}")