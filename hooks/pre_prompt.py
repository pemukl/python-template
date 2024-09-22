import os
import subprocess
import sys


def run(*popenargs):
    FNULL = open(os.devnull, 'w')

    try:
        retcode = subprocess.call(*popenargs, stdout=FNULL, stderr=FNULL)
    except Exception as e:
        raise
    return retcode


def check_installation(program_name, severity="EEROR"):
    try:
        run([program_name, "--version"])
        return True
    except Exception as e:
        print(f"{severity}: {program_name} is not installed but required.")
        return False


if __name__ == "__main__":
    if not check_installation("python3.11"):
        sys.exit(1)

    if not check_installation("pixi"):
        sys.exit(1)

    if not check_installation("git"):
        sys.exit(1)

    if not check_installation("pre-commit"):
        sys.exit(1)

    check_installation("docker", severity="WARNING")
    check_installation("docker-compose", severity="WARNING")
