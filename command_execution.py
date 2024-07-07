import subprocess

def run_command(command):
    prochandle = subprocess.Popen(
            command,
            shell = True,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
    )

    output, errors = prochandle.communicate()
    return output + errors
