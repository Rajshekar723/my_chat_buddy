import random
import time

def flip_coin():
    time.sleep(2)
    if random.random() < 0.5:
        return "heads"
    else:
        return "tails"

print("Flipping coin...")
result = flip_coin()
print("The coin landed on", result)
