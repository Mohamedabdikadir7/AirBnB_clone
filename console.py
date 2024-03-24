#!/usr/bin/python3
""" a file implementing the console """
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()  # Print a newline for better formatting
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
