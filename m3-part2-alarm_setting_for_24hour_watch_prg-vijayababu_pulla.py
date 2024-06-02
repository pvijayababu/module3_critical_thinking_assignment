def main():
    # Ask the user for the current time in hours (24-hour format)
    current_time = int(input("Enter the current time (in hours, 0-23): "))
    
    # Validate the current time input
    if current_time < 0 or current_time > 23:
        print("Provide valid input! Please check and make sure that entered time is between 0 and 23.")
        return
    
    # Ask the user for the number of hours to wait for the alarm
    wait_hours = int(input("Enter the number of hours to wait for the alarm: "))
    
    # Calculate the time when the alarm will go off
    alarm_time = (current_time + wait_hours) % 24
    
    # Output the result
    print(f"The time when the alarm goes off will be: {alarm_time:02d}:00 (24-hour format)")

if __name__ == "__main__":
    main()
