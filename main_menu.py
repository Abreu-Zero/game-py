import game

print("Welcome to YCNW 1.0")
print("-------------------\n")

instance = game.Game()
option = int(input("Please select an option:\n1- Play Game\n2- Rules\n"))

while option != 1 and option != 2:
    option = int(input("\nPlease select an option:\n1- Play Game\n2- Rules\n"))

if option == 2:
    print(instance.show_rules())
    option = int(input("\nWant to start the game now? I want to play!\n1- Yes\n2- No\n"))

while option == 1:

    instance.start_game()
    option = int(input("\nWant to Play again?\n1- Yes\n2- No\n"))

if option != 1:
    print("ok, good bye :(")





