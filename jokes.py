import random

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the chicken cross the road? To get to the other side.",
        "Why did the banana go to the doctor? Because it wasn't peeling well."
    ]

    return random.choice(jokes)

print(tell_joke())
