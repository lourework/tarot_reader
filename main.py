
from tarot.reader import TarotReader

def main():
    reader = TarotReader()

    while True:
        print("\n Welcome to Tarot Reader 🔮")
        print("1. Daily Card")
        print("2. Past, Present and Future")
        print("3. Yes or No")
        print("4. Exit")

        choice = input("\n Choose an option ")

        if choice == "1":
            result = reader.daily_card()
            print(f"\n{result['name']}")
            print(result["meaning"])

        elif choice == "2":
            spread = reader.past_present_future()
            for card in spread:
                print(f"\n{card['position']}: {card['name']}")
                print(card["meaning"])

        elif choice == "3":
            result = reader.yes_or_no()
            print(f"\n{result['name']} ({result['orientation']})")
            print("Answer:", result["answer"])
            print(result["meaning"])

        elif choice == "4":
            break
            
        else:
            print("\n Invalid option.")

if __name__ == "__main__":
    main()

