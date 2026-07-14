message = input("Enter a secret message: ")

# The [::-1] trick tells Python to step through the text backwards!
encoded = message[::-1]

print(f"Encoded message: {encoded}")
print(f"To decode it, just flip it again: {encoded[::-1]}")