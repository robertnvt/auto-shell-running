import subprocess
import time

def execute_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())

        return process.poll()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

# Example usage
command = "yarn cli mint-dft higgsboson --satsbyte=80"  # Replace with your desired command
num_repeats = 5  # Number of times to repeat the command
retry_delay = 3  # Delay in seconds between command executions

for i in range(num_repeats):
    print(f"Executing command: {command}")
    return_code = execute_command(command)
    if return_code == 0:
        print("Command executed successfully.")
    else:
        print(f"Command execution failed with return code: {return_code}")

    if i < num_repeats - 1:
        print(f"Waiting {retry_delay} seconds before the next execution...")
        time.sleep(retry_delay)
