import readSound as p
import loadInfos as l

(buttons, sounds) = l.load()

while True:
    choice = int(input("Sound (<= " + str(len(sounds) - 1) + ") : "))

    if(choice < len(sounds) and choice >= 0):
        p.read(sounds[choice])
    else:
        print("Error")