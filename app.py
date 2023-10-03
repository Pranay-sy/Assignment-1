from game_ import Game

def main():
    print("Welcome to the Lost World Adventures!")
    print("\nIn a world enveloped in darkness, where mystical creatures roam freely, and ancient secrets lie hidden, you are about to undertake on an epic adventure like no other. The fate of the realm rests in your hands!\n")

    print("🌟 Overview 🌟")
    print("In the 'Lost World Adventures,' you will step into the shoes of one of two extraordinary roles, each with a unique path and destiny.")
    print("\n1. The Explorer of Enigma:")
    print("As an Explorer, you are steered by curiosity and a thirst for knowledge. Your discoveries will shape the destiny of the Lost World Adventures.  ")
    print("\n2. The Warrior of Valor:")
    print(" As a Warrior, you are a fearless champion of justice and honour. Your path is one of pure strength and bravery. Wield your formidable weapons, stand against the hordes of darkness, and lead the charge to victory. The world relies on your unwavering courage. ")
    print("\nThe choice is yours, brave adventurer! Will you become an Explorer or a champion of valor? Prepare to face mythical beasts, solve perplexing puzzles, and uncover the hidden stories that shape the 'Lost World Adventures.'\n")

    print("Choose your role:")
    print("1. Explorer")
    print("2. Warrior")
    choice = input("Enter the number of your chosen role: ")
    
    if choice == '1':
        role = "Explorer"
    elif choice == '2':
        role = "Warrior"
    else:
        print("Invalid choice. Please select 1 or 2.")
        return

    game = Game(role)
    game.play()


main()
