# stax

`stax` is a command-line tool for managing a text stack (FILO), supporting operations like push and pop. It's designed for professionals and thinkers who delve into complex projects, providing a simple way to manage the flow of thoughts and context.

I built this for personal use but feel free to use it and contribute to it.

## Purpose

When coding or pursuing any complex project, it's common to encounter nested sub-problems you drill-down to. As you drill-down it becomes hard to keep track of where you came from and where to backtrack to when you fix the deepest problems. Traditional task managers or TODO lists fall short in these scenarios – they either lack the structure to prioritize immediate tasks or add unnecessary overhead.

`stax` fills this gap by offering a barebones way to manage a text stack. It follows the stack data structure in computer science, perfect for keeping track of your current context and enabling effective backtracking through layers of thought or sub-problems.

The idea for `stax` arose from a personal need, for a tool that could act as a mental stack during complex problem-solving. Unable to find an existing tool built around this concept, I decided to create a simple tool for myself.

The tool is general-purpose though so you can use it for anything.

## Installation

To install `stax`, clone this repository and run the script:

```bash
git clone git@github.com:antonioalegria/stax.git
cd stax
python stax.py
```

## Usage

Run the script with Python:

```bash
Copy code
python stax.py [command]
```

## Available Commands

- `push [item]`: Add an item to the top of the stack, reflecting your current focus or arising sub-problem. Can also use `pu` and `p`.
- `pop`: Remove the top item from the stack, effectively backtracking. Can also use `po` and `p`.
- `peek`: Quickly view the top item without altering the stack.
- `clear`: Clear the entire stack. It allows you to reset your mental context.
- `undo`: Reverse the last change. Currently only supports one undo step. Can also use `u`.
- `shell`: Enter the interactive shell mode.

If no command is provided the view command is run.

## Multiple Stacks

To manage multiple, separate stacks, simply run `stax` in different directories. Each directory will maintain its own independent stack.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
