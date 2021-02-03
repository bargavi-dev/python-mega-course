import time

while True:
    with open("file.txt") as file:
        print(file.read())
        time.sleep(10)