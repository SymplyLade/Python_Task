import time
def countdown_timer():
    # User input handling with validation
    while True:
        try:
            duration = int(input("Enter countdown duration in seconds: "))
            if duration <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    # Countdown using a while loop
    while duration > 0:
        print(f"Time remaining: {duration} seconds", end='\r')
        time.sleep(1)
        duration -= 1
    print("\nCountdown finished!")
if __name__ == "__main__":
    countdown_timer()
