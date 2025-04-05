def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me the name."
        except KeyError:
            return "No such contact."

    return inner

def parse_input(user_input) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts) -> str:
    name, phone = args
    result = 'No contact found'
    if name in contacts:
        contacts[name] = phone
        result = 'Contact updated.'    
    return result 

@input_error
def show_phone(args, contacts) -> str:
    name = args[0]
    result = contacts[name]    
    return result 

@input_error
def show_all(contacts:dict) -> str:
    result = ''

    for name, phone in contacts.items():
        result += f'{name}:{phone}\n'
    if not result:
        return 'no contacts :('
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()