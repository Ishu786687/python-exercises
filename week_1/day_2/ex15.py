from sys import argv

script, filename = argv   #storing program file name in script and file name in filename

txt = open(filename)        #file object is created and stored in txt variable

print("Here's your file %r:"%filename)
print(txt.read()) #read method reads entire file as string

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


"""txt_again is a variable used to store the file object 
    created when opening a file specified by the user's input 
    (file_again). Let's break down how txt_again is used in the code:
"""
    
txt.close()
txt_again.close()
