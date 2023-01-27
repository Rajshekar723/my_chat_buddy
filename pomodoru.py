import time
import winsound

# Set the length of the Pomodoro (in minutes)
pomodoro_length = 25

# Set the length of the break (in minutes)
break_length = 5

# Set the number of Pomodoros
num_pomodoros = 4

# Initialize a counter for the number of Pomodoros completed
pomodoros_completed = 0

# Set the path to the sound files
pomodoro_sound = "pomodoro.wav"
break_sound = "break.wav"

print("Starting Pomodoro Technique...")

while pomodoros_completed < num_pomodoros:
    # Start the Pomodoro
    print(f"Starting Pomodoro {pomodoros_completed+1} for {pomodoro_length} minutes.")
    time.sleep(pomodoro_length * 60)
    print("Pomodoro complete.")
    winsound.PlaySound(pomodoro_sound, winsound.SND_FILENAME)

    # Take a break
    print(f"Taking a break for {break_length} minutes.")
    time.sleep(break_length * 60)
    print("Break complete.")
    winsound.PlaySound(break_sound, winsound.SND_FILENAME)

    # Increment the counter
    pomodoros_completed += 1

print("Pomodoro Technique complete.")
