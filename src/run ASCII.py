import time
import json
import multiprocessing
import pygame




def animate(strASCII):

    #clear screen
    print("\033c", end="")

    #print ASCII
    print(strASCII)

    # wait a short time before updating again
    time.sleep(0.026000000000000000001)

def play_music():
    pygame.init()
    pygame.mixer.music.load("./input/bad_apple.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def playASCII() :
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


if __name__ == "__main__" :
    p1 = multiprocessing.Process(target=play_music)
    p2 = multiprocessing.Process(target=playASCII)
    p1.start()
    p2.start()
    p1.join()
    p2.join()