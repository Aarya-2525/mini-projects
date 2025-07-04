# To clean any additional characters added to the emojis
import unicodedata

def normalize(word):
    return unicodedata.normalize("NFKC", word).strip()

emoji_map = {":)": "😊",":(": "😞",":D": "😄","<3": "❤️"}

# Create reverse map with normalized keys
symbol_map = {normalize(v): k for k, v in emoji_map.items()}

message = input("> ")
words = message.split()

# Normalize all input words for matching
normalized_words = [normalize(word) for word in words]

# Count matches
symbols = sum(word in emoji_map for word in normalized_words)
emojis = sum(word in symbol_map for word in normalized_words)

# Auto-detect direction
if emojis > symbols:
    output = [symbol_map.get(word, word) for word in normalized_words]
else:
    output = [emoji_map.get(word, word) for word in normalized_words]

print(" ".join(output))