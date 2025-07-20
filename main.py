from bank_system import BankSystem

def main():
    bank_system = BankSystem()
    while True:
        print('\n' + '*' * 35)
        print('== 🏦 Welcome to Assassin Bank ==')
        print('*' * 35)
        print('1. Sign up')
        print('2. Log in')
        print('3. Exit')

        choice = input('👉 Choose an option: ')

        if choice == '1':
            bank_system.sign_up()
        elif choice == '2':
            pass
        elif choice == '3':
            print('👋 Thanks for checking out Assassin Bank. Goodbye!')
            break
        else:
            print('❌ Invalid option. Please try again.')
 

if __name__ == '__main__':
    main()