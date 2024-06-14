def show_main_menu():
    print("Hello! Welcome to Menkins. How can I assist you today?")
    print("1. View Menu")

def show_menu_categories():
    print("Sure! Here are our menu categories:")
    print("1. Appetizers")
    print("2. Main Courses")
    print("3. Desserts")
    print("4. Beverages")
    print("5. Back to Main Menu")

def show_main_courses():
    print("Here are our Main Courses:")
    print("1. Grilled Chicken - $12.99")
    print("2. Beef Steak - $15.99")
    print("3. Veggie Pasta - $10.99")
    print("4. Back to Menu Categories")
    print("5. Back to Main Menu")

def main():
    while True:
        show_main_menu()
        choice = input("Please enter the number of your choice: ")
        if choice == '1':
            show_menu_categories()
            category_choice = input("Please enter the number of your choice: ")
            if category_choice == '2':
                show_main_courses()
                dish_choice = input("Please enter the number of your choice: ")
                if dish_choice == '1':
                    print("You've selected Grilled Chicken. Would you like to:")
                    print("1. Add to Cart")
                    print("2. View Menu Categories")
                    print("3. Back to Main Menu")
                    action_choice = input("Please enter the number of your choice: ")
                    if action_choice == '1':
                        print("Grilled Chicken has been added to your cart.")
                        print("1. Place an Order")
                        print("2. View Menu Categories")
                        print("3. Back to Main Menu")
                        order_choice = input("Please enter the number of your choice: ")
                        if order_choice == '1':
                            print("Your cart contains:\n1 x Grilled Chicken - $12.99\nTotal: $12.99")
                            print("Would you like to:")
                            print("1. Confirm Order")
                            print("2. Cancel Order")
                            print("3. Back to Main Menu")
                            confirm_choice = input("Please enter the number of your choice: ")
                            if confirm_choice == '1':
                                print("Thank you for your order! Your food will be ready shortly.")
                            elif confirm_choice == '2':
                                print("Your order has been canceled.")
                            else:
                                continue
                        elif order_choice == '2':
                            continue
                        else:
                            continue
                    elif action_choice == '2':
                        continue
                    else:
                        continue
        elif choice == '3':
            print("You can contact us at:\nPhone: (123) 456-7890\nEmail: info@restaurant.com\nAddress: 123 Foodie Lane, Taste Town, FL")
            print("1. Back to Main Menu\n2. Exit")
            contact_choice = input("Please enter the number of your choice: ")
            if contact_choice == '2':
                break
        elif choice == '4':
            print("We are open from 9 AM to 9 PM every day.")
            print("1. Back to Main Menu\n2. Exit")
            hours_choice = input("Please enter the number of your choice: ")
            if hours_choice == '2':
                break
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
