from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    
    next = input("> ")    
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")
        
    if how_much < 50:
        print("nice, you are not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard")
        
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of money.")
    print("The fat bear is in front of another door.")
    print("how are you going to move the bear.")
    bear_moved = False
    
    while True:
        next = input(">")
        
        if next == "take honey":
            