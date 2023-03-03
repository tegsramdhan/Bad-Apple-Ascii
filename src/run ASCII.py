import time
import json


def animate(strASCII):

    #clear screen
    print("\033c", end="")

    #print ASCII
    print(strASCII)

    # wait a short time before updating again
    time.sleep(0.05)

#read txt of ASCII
with open("./output/ASCII.txt", "r") as file:
    json_string = file.read()

#convert it to dictionary
dictASCII = json.loads(json_string)

#get frames lenght
intframes =  len(dictASCII)

#loop dictionary and print it
for i in range(1, intframes):
    animate(dictASCII[str(i)])



