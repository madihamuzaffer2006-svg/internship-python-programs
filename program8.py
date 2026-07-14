import time

seconds = int(input("Enter countdown time in seconds: "))

for i in range(seconds, 0, -1):
    print(f"Time left: {i} seconds")
    time.sleep(1) # Wait for 1 second

print("⏰ BEEP BEEP! Time's up!")