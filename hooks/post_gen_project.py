import os
import subprocess

if __name__ == "__main__":
    subprocess.call(['pixi', 'install'])
    subprocess.call(['git','init'])
    subprocess.call(['git', 'add', "."])
    subprocess.call(['git', 'commit', "-m", "Initial commit from python template."])
