import sys
import os

STACK_FILE = 'stax.txt'
TEMP_FILE = 'stax.txt.bak'

##################
## Presentation ##
##################

def txt_highlight(txt):
    return f"\033[1;4m{txt}\033[0m"

def txt_lowlight(txt):
    return f"\033[1;30m{txt}\033[0m"

def display_stack(stack):
    if len(stack) == 0:
        print('<empty>')
        return

    for index, item in enumerate(stack):
        if index == 0:
            print(txt_highlight(item))
        else:
            print(item)

def display_pop(popped_item, stack):
    # display the popped item
    # display a line of dashes
    # display the stack
    
    print(txt_lowlight(popped_item))
    print('-' * len(popped_item))
    display_stack(stack)

def display_peek(peeked_item):
    print(peeked_item)

def display_clear(stack):
    if len(stack) == 0:
        print('<empty>')
        return

    for item in stack:
        print(txt_lowlight(item))

def display_undo(stack):
    display_stack(stack)

######################
## Stack Management ##
######################

def read_stack():
    if not os.path.exists(STACK_FILE):
        return []
    with open(STACK_FILE, 'r') as file:
        return file.read().splitlines()

def write_stack(stack):
    with open(STACK_FILE, 'w') as file:
        file.write('\n'.join(stack))

def push(item):
    stack = read_stack()
    backup_stack(stack)  # Backup before modification
    stack.append(item)
    write_stack(stack)

def pop():
    stack = read_stack()
    if stack:
        backup_stack(stack)  # Backup before modification
        popped_item = stack.pop()
        write_stack(stack)
        return popped_item
    else:
        return None

def clear():
    stack = read_stack()
    
    if stack == []:
        return True
    
    confirmation = input(f"ℹ️ Are you sure you want to clear the stack? (yes/no): ")
    if confirmation.lower().strip() in ['yes', 'y']:
        backup_stack(stack)  # Backup before modification
        write_stack([])
        return True
    else:
        return False

def undo():
    if os.path.exists(TEMP_FILE):
        os.rename(TEMP_FILE, STACK_FILE)
        return True
    else:
        return False

def view():
    stack = read_stack()
    return list(reversed(stack))

def peek():
    stack = read_stack()
    return stack[-1] if stack else None

def backup_stack(stack):
    with open(TEMP_FILE, 'w') as file:
        file.write('\n'.join(stack))

#########
## CLI ##
#########

def shell_mode():
    print("Entering shell mode. Type 'exit' to leave.")
    
    while True:
        command_input = input("stax> ").strip().split()
        if not command_input:
            continue

        command = command_input[0].lower()
        args = command_input[1:]
        
        if command in ('exit', 'quit'):
            break
        else:
            run_command(command, args)

def run_command(command, args):
    if command in ('push', 'pu') or (command == 'p' and len(args) > 0):
        if args:
            push(" ".join(args))
            display_stack(view())
        else:
            print(f"⚠️ No item provided to push.")
    elif command in ('pop', 'po') or (command == 'p' and len(args) == 0):
        popped_item = pop()
        display_pop(popped_item, view())
    elif command == 'view':
        display_stack(view())
    elif command == 'peek':
        peeked_item = peek()
        if peeked_item is not None:
            display_peek(peeked_item)
        else:
            print("<empty>")
    elif command == 'clear':
        if clear():
            display_clear(view())
        else:
            print(f"ℹ️ Clear operation cancelled.")
    elif command in ('undo', 'u'):
        if undo():
            display_undo(view())
        else:
            print(f"⚠️ No operation to undo.")
    else:
        print(f"⚠️ Invalid command.")
        print(f"ℹ️ Valid commands: push, pop, view, peek, clear, undo, shell")

def main():

    if len(sys.argv) < 2:
        # Default action is to view the stack
        command = 'view'
        args = []
    else:
        command = sys.argv[1].lower()
        args = sys.argv[2:]

    if command == 'shell':
        shell_mode()
    else:
        run_command(command, args)

if __name__ == "__main__":
    main()
