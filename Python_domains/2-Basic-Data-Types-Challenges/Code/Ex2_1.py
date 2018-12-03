#!/usr/bin/env python3
'''
Input: String of commands and values

Output: print list

'''

INPUT_COMMANDS = '''12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print'''

def do_command_list(input_commands):
    commands = input_commands.strip().split("\n")
    my_list = []
    for line_command in commands[1:]:
        actions = line_command.split(" ")
        if actions[0] == "insert":
            my_list.insert(int(actions[1]), int(actions[2]))
        elif actions[0] == "remove":
            my_list.remove(int(actions[1]))
        elif actions[0] == "append":
            my_list.append(int(actions[1]))
        elif actions[0] == "pop":
            my_list.pop()
        elif actions[0] == "sort":
            my_list.sort()
        elif actions[0] == "reverse":
            my_list.reverse()
        else:
            print(my_list)

def main():
    do_command_list(INPUT_COMMANDS)

if __name__ == "__main__":
    main()
