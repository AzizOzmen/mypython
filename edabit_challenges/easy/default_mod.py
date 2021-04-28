# Default Mood
# Create a function that takes in a current mood
# and return a sentence in the following format:
# "Today, I am feeling {mood}".
# However, if no argument is passed, return
# "Today, I am feeling neutral".

# Examples
# mood_today("happy") ➞ "Today, I am feeling happy"
# mood_today("sad") ➞ "Today, I am feeling sad"
# mood_today() ➞ "Today, I am feeling neutral"

def mood_today(*mood):
    mood2 = ''.join(mood)
    if len(mood2) != 0:
        print(f"Today, I am feeling {mood2}")
    else:
        print(f"Today, I am feeling neutral")
mood_today("happy")
mood_today("sad")
mood_today()