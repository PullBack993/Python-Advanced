try:
    text_file = open('1.text.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')