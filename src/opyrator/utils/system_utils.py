import subprocess
from typing import Optional


def run_command(  # type: ignore
    command: str,
    disable_stdout_logging: bool = False,
    disable_stderr_logging: bool = False,
    exit_on_error: bool = True,
    timeout: Optional[int] = None,
) -> subprocess.CompletedProcess:
    """Run a specified command.

    Args:
        command (str): The shell command that is executed via subprocess.Popen.
        disable_stdout_logging (bool): Disable stdout logging when it is too much or handled by the caller.
        exit_on_error (bool): Exit program if the exit code of the command is not 0.
        timeout (Optional[int]): If the process does not terminate after timeout seconds, raise a TimeoutExpired exception.

    Returns:
        subprocess.CompletedProcess: State
    """
    # Add timeout to command
    if timeout:
        command = f"timeout {timeout} {command}"

    with subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    ) as process:

        try:
            stdout = ""
            stderr = ""
            with process.stdout:  # type: ignore
                for line in iter(process.stdout.readline, ""):  # type: ignore
                    if not disable_stdout_logging:
                        print(line.rstrip("\n"))
                    stdout += line
            with process.stderr:  # type: ignore
                for line in iter(process.stderr.readline, ""):  # type: ignore
                    if not disable_stderr_logging:
                        print(line.rstrip("\n"))
                    stderr += line
            exitcode = process.wait(timeout=timeout)
            process.stdout.close()  # type: ignore
            process.stderr.close()  # type: ignore

            if exit_on_error and exitcode != 0:
                process.terminate()
                # exit_process(exitcode)

            return subprocess.CompletedProcess(
                args=command, returncode=exitcode, stdout=stdout, stderr=stderr
            )
        except Exception as ex:
            print(f"Exception during command run: {ex}")
            process.terminate()
            # exit_process(1)
