import sys
import subprocess
from pathlib import Path

def git_ipfs():
    target_script = Path(__file__).resolve().parent.joinpath('git-ipfs')
    completed = subprocess.run([sys.executable, target_script] + sys.argv[1:])
    sys.exit(completed.returncode)

def git_remote_ipfs():
    target_script = Path(__file__).resolve().parent.joinpath('git-remote-ipfs')
    completed = subprocess.run([sys.executable, target_script] + sys.argv[1:])
    sys.exit(completed.returncode)
