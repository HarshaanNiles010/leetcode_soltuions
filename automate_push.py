""" import subprocess
import sys
import os

msg = input('Type the commit message (+ ENTER):') 
repo_directory = os.getcwd()

subprocess.run(["git", "add", "."], cwd=repo_directory)
# commit file
subprocess.run(["git", "commit", "-m", msg], cwd=repo_directory)
# push
subprocess.run(["git", "push"], cwd=repo_directory)  """
# I want the python script to run at a certain time and a repeated number of times