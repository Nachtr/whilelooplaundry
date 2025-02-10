'''
Write a Python script that uses a while loop to simulate folding five (5) shirts. Your code should:

Initialize a variable to keep track of the number of shirts folded
Use a while loop to "fold" shirts until five are folded
Print a message for each shirt folded
Print a final message when all shirts are folded
'''

# if we import time, we can create a realistic cycle.
import time

# Create folded_shirts variable
folded_shirts = 0

# lets try making the simulation a little more interactive:
while True: # I originally just tried to check if the users input was = to a number but that failed.
    # After looking around online, I found that using a while True: would be best to check if the folding time = float.
    folding_time = input("How long does it take you to fold a shirt (in seconds): ")

    try:
        folding_time = float(folding_time)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number! ")


# Introduce while loop
while folded_shirts < 5:
    folded_shirts += 1
    print(f"You have folded {folded_shirts} shirt!")
    time.sleep(folding_time)

    # end loop, and announce the completion of the task
    if folded_shirts == 5:
        print("You have folded all of your laundry")

'''
This feels slightly confusing so I might come back around to try to review this!
'''