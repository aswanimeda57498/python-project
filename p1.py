player1 = input("enter player1 choice:").lower()
player2 = input("enter payer2 choice:").lower()

if player1 == player2:
    result = "draw"
elif(player1 == "rock" and player2 == "scissor") or \
     (player1 == "scissors" and player2 == "paper") or \
     (player1 == "paper" and player2 == "rock"):
    result = "player1 wins"
else:
    result = "player2 wins"
print(result)
       
             
            

