from collections import deque

user_input = input("Enter a command: ")

def is_palindrom(user_input):
    sent = [letter.lower() for letter in str(user_input)]
    
    char_deque = deque(sent)
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

print(is_palindrom(user_input))