from my_class import BankAccount

# ask user for account holder name
name = input("Enter account holder name: ")
initial = float(input("Enter initial balance (or 0): "))

account = BankAccount(name, initial)

while True:
    print("\nOptions: deposit, withdraw, balance, account holder, exit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "deposit":
        amount = float(input("Enter amount to deposit: "))
        try:
            print(account.deposit(amount))
        except Exception as e:
            print(e)

    elif choice == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        try:
            print(account.withdraw(amount))
        except Exception as e:
            print(e)

    elif choice == "balance":
        print(account.get_balance())
    
    elif choice == "account holder":
        print(account.get_account_holder())

    elif choice == "exit":
        print("Exiting program.")
        break

    else:
        print("Invalid option, try again.")