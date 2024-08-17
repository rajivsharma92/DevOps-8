import psutil
import time

# Define the CPU usage threshold
THRESHOLD = 80

print("Monitoring CPU usage...")

try:
    while True:  # Infinite loop to keep monitoring
        # Get the current CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)

        # for usage in range(10):
        #     cpu_usage = psutil.cpu_percent(interval=1)
        #     print(f"CPU Usage in 1 sec intervel: {cpu_usage}% ")


        # Check if the CPU usage exceeds the threshold
        if cpu_usage > THRESHOLD:
            # Trigger an alert if the threshold is exceeded
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

        # Sleep for a short time before checking again (optional, to reduce CPU load)
        time.sleep(1)

except KeyboardInterrupt:
    # Graceful exit when the user interrupts the program
    print("Monitoring stopped by user.")
except Exception as e:
    # Handle any other unexpected exceptions
    print(f"An error occurred: {e}")
