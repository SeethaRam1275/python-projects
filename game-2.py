a = 0
b = 0
while True :
   while True :   
      import random               
      x = input("Let's play rock, paper and scissors!!!(If you want to end the game enter end)\n")
      x = x.lower()
      y = random.choice(["rock", "paper", "scissors"])
      if x != y:
         break   
      else:
         print("OS :", y)
         print("It's a Draw! Please enter again!!")
         b = b + 1 
   if x.lower() == "rock" and y == "scissors" :
      print("OS :", y)
      print("You win!!")
      a = a + 1
      b = b + 1
   elif x.lower() == "rock" and y == "paper" :
      print("OS :", y)
      print("You lose!!")
      a = a - 1
      b = b + 1
   elif x.lower() == "paper" and y == "scissors" :
      print("OS :", y)
      print("You lose!!")
      a = a - 1
      b = b + 1
   elif x.lower() == "paper" and y == "rock" :
      print("OS :", y)
      print("You win!!")
      a = a + 1
      b = b + 1
   elif x.lower() == "scissors" and y == "rock" :
      print("OS :", y)
      print("You lose!!")
      a = a - 1
      b = b + 1
   elif x.lower() == "scissors" and y == "paper" :
      print("OS :", y)
      print("You win!!")
      a = a + 1
      b = b + 1
   elif x.lower() == "end" :
      break
   else :
      print("Please enter either rock, paper or scissors!")   
print("Your score is ", a, "out of ", b)
input("Thanks for playing!!")
    


   



   


 


