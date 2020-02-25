def tanyakan_ok(prompt, retries=4, reminder='TOLONG ULANGI!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# panggil fungsinya
tanyakan_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')