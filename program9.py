emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "cat": "🐱",
    "dog": "🐶",
    "pizza": "🍕",
    "love": "❤️",
    "fire": "🔥"
}

sentence = input("Enter a sentence (try using words like happy, cat, pizza, or love): ")
words = sentence.split()

# Replace words if they exist in our emoji dictionary
translated_words = [emoji_dict.get(word.lower(), word) for word in words]
result = " ".join(translated_words)

print(f"Translated: {result}")