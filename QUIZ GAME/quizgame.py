print("Welcome to the Quiz..!")

playing = input("Do you want to Play? ")

if playing.lower() != "yes": 
    quit()

print("Okay! Let's play :] ")
score = 0

## CPU
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

## GPU
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

## RAM
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

## ROM
answer = input("What does ROM stand for ")
if answer.lower() == "read only memory":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score) + " questions correct")
print("Your score is " + str((score/4) * 100) + "% ")