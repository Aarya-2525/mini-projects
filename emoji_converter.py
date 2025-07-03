message = input(">")
words = message.split(" ")
emojis = {":)": "😊", ":(": "😞","<3": "❤️",":D": "😄"}
output = ""
for word in words:
    output += emojis.get(word,word) + " "
print(output)


