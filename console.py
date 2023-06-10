#!/usr/bin/python
import cmd

class Myconsole(cmd.Cmd):
    prompt = "(hbnb: )"
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
  Myconsole().cmdloop()