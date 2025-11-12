# Count how many times a word appears in a list.

words = ['apple','banana','banana','grapes','apple']

count = 0
for word in words:
    if word == "banana":
        count+=1
print(count)

