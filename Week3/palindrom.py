
word = input("Enter a word: ")

for i, j in zip(range(len(word)), range(len(word) - 1, -1, -1)):
   if i >= j:
      print(f"Word {word} is palindrom")
      break
   if word[i] != word[j]:
      print(f"Word {word} is not palindrom")
      break
    
    