def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add =str(input('Enter what you want to add to the shopping list: '))
            shopping_list.append(add)
            pass
        elif choice == '2':
            delete = str(input('Enter what you want to remove from the shopping list: '))
            for item in shopping_list:
                if delete == item:
                    shopping_list.remove(delete)
                    
                else:
                   print("The Item was not found on the list") 
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()