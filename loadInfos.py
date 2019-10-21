

def load():
    f = open('setup.txt', 'r', encoding='latin-1')

    buttons = []
    sounds = []
    for line in f.readlines():
        (pin, sound) = line.split(';')
        buttons.append(int(pin))
        sounds.append(sound.replace("\n", ""))

    print(sounds)
    return (buttons, sounds)