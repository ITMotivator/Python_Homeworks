str = """She sells sea shells on the sea shore. 
    The shells that she sells are sea shells."""
arr = str.lower().split()
print(arr)
newArr = []
for word in arr:
    letters = list(word)
    if '.' in letters:
        letters.remove('.')
    word = ''.join(letters)
    newArr.append(word)
print(newArr)
dict = {}
for letter in newArr:
    dict[letter] = dict.get(letter, 0) + 1
setDict = set(dict.keys())
print(setDict)
print(len(setDict))

