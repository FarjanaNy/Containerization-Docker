# app.py
import os

name = os.getenv("NAME", "Friend")

print(f"Hello {name} 👋")
print("I am running inside a Docker container.")

with open("message.txt", "w") as f:
    f.write(f"This file was created inside a container. Hello {name}!")

print("File created: message.txt")
print("Container will stop now. Bye!")
