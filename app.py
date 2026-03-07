"""import os

def run():
    user_input = input("Enter command: ")
    os.system(user_input)

if __name__ == "__main__":
    run()



"""
import subprocess

def run():
    user_input = input("Enter text: ")
    subprocess.run(["echo", user_input], shell=False)

if __name__ == "__main__":
    run()
