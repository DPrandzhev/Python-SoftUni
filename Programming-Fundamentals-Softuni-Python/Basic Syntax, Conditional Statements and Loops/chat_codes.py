number_of_messages = int(input())

for _ in range(number_of_messages):
    chat_code = int(input())

    if chat_code == 88:
        print("Hello")
    elif chat_code == 86:
        print("How are you?")
    elif not chat_code == 88 and not chat_code == 86 and chat_code < 88:
        print("GREAT!")
    elif chat_code > 88:
        print("Bye.")