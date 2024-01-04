from queue import Queue
import time
import threading
from random import randint

request_q = Queue()
exit_flag = False  # Флаг для зупинки потоків

def generate_request():
    while not exit_flag:
        new_request = f"Request {randint(100000, 999999)}"
        request_q.put(new_request)
        time.sleep(10)

def process_request():
    while not exit_flag:
        if not request_q.empty():
            request = request_q.get()
            print(f"Processing request: {request}")
        else:
            print("Queue is empty")
        time.sleep(5)

def close_bot():
    global exit_flag
    exit_flag = True  # Встановлюємо флаг для зупинки потоків
    print("Goodbye!")

def main():
    msg = "\n==============================\nWelcome to the queue!\n==============================\n"
    print(msg)

    generate_thread = threading.Thread(target=generate_request)
    process_thread = threading.Thread(target=process_request)

    generate_thread.start()
    process_thread.start()

    while True:
        user_input = input("Enter a command: ")
        command = user_input.lower()

        if command in ["goodbye", "close", "exit"]:
            close_bot()
            break

    generate_thread.join()  # Чекаємо завершення потоків
    process_thread.join()

if __name__ == "__main__":
    main()