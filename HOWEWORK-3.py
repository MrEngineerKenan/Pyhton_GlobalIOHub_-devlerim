
import time

#welcoming the user
Name = input("What is your name? ")

print ("Hello, " + Name, "Time to play hangman!\n")


#wait for 1 second
time.sleep(2)

print ("Start guessing...\n")

time.sleep(2)

#here we set the secret
word = ("python")
#creates an variable with an empty value

guesses = ''

#determine the number of turns
turns = 5

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char),    

        else:
    
        # if not found, print a dash
            print ("_")     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:    
        
        print ("You won")
        
        time.sleep(0.5)
        
        print ("Game Over...")
        
        time.sleep(3)
        
        quit()
        
    # exit the script
        break              

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")    
 
    # how many turns are left
        print ("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose")
            
            time.sleep(0.5)
            
            print ("Game Over...")
            
            time.sleep(3)
            
            quit()