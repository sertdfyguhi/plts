from sys import argv

def run(text):
    stack = []
    toprint = ''
    e = False
    a = False
    for idx, letter in enumerate(text):
        if a == False:
            if letter == '?':
                a = True
                stack.append(text[idx + 1])
            elif letter == '%':
                a = True
                stack.insert(0, text[idx + 1])
            elif letter == '&':
                toprint += stack[-1] + '\n'
            elif letter == '$':
                toprint += stack[0] + '\n'
            elif letter == '#':
                toprint += ''.join(stack) + '\n'
            elif letter == '@':
                toprint += ''.join(stack)[::-1] + '\n'
            elif letter == '<':
                del stack[0]
            elif letter == '>':
                del stack[-1]
            else:
                print(f'{str(idx + 1)}: error')
                e = True
                break
        else:
            a = False
    if e == False:
        s = toprint.rsplit('\n', 1)
        print(''.join(s))

if len(argv) > 1:
    with open(argv[1], 'r') as f:
        text = f.read()
    run(text)
else:
    while True:
        text = input('> ')
        run(text)
