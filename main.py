from sys import argv

if len(argv) > 1:
    with open(argv[1], 'r') as f:
        text = f.read()

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
        else:
            a = False
    if e == False:
        print(toprint)
else:
    while True:
        text = input('> ')
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
            else:
                a = False
        if e == False:
            s = toprint.rsplit('\n', 1)
            print(''.join(s))