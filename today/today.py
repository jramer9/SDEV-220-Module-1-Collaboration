import multiprocessing
import time
import random
from datetime import date, datetime

# --- Function for Chapter 15.1 ---
def process_task():
    # Generate a random float between 0.0 and 1.0
    wait_time = random.random()
    
    # Wait for that random amount of time
    time.sleep(wait_time)
    
    # Print the current time
    current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"Process {multiprocessing.current_process().name} waited {wait_time:.2f} seconds. Time: {current_time}")

if __name__ == "__main__":
    
    print("--- Chapter 13 Exercises ---")
    
    # 13.1 Write the current date as a string to today.txt
    today_string = date.today().isoformat()
    with open("today.txt", "w") as f:
        f.write(today_string)

    # 13.2 Read today.txt into a string
    with open("today.txt", "r") as f:
        today_string = f.read().strip()
    print("today_string:", today_string)

    # 13.3 Parse the date from today_string
    today_date = datetime.strptime(today_string, "%Y-%m-%d").date()
    print("today_date:", today_date)

    # 13.4 Create a date object of your day of birth
    # (Change this to your actual birth date!)
    birth_date = date(1990, 1, 1)
    print("birth_date:", birth_date)

    # 13.5 What day of the week was your day of birth?
    day_name = birth_date.strftime("%A")
    print("I was born on a", day_name)

    # --- Chapter 15.1 Exercise ---
    print("\n--- Chapter 15.1 Exercises ---")
    print("Starting 3 processes...")
    
    processes = []
    
    # Create three separate processes
    for i in range(3):
        p = multiprocessing.Process(target=process_task, name=f"Worker-{i+1}")
        processes.append(p)
        p.start()
    
    # Wait for all processes to finish before exiting the main program
    for p in processes:
        p.join()
        
    print("All processes finished.")