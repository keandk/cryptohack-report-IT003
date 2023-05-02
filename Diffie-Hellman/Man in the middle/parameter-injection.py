import pwn
import json
import hashlib
from Crypto.Cipher import AES

host = "socket.cryptohack.org"
port = 13371

def exploit():
    pr = pwn.connect(host, port)
    try:
        # This code is establishing a connection to a remote server at `host` and `port` using the
        # `pwn` library. It then reads data from the server until it encounters a colon (`:`)
        # character using the `pr.readuntil(": ")` method. The data is then loaded as a JSON object
        # using `json.loads(pr.readline().strip().decode())`. The values of `p`, `g`, and `A` are
        # extracted from the JSON object by converting the hexadecimal strings to integers using the
        # `int()` function with a base of 16.
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        #p = int(line['p'][2:].strip('f'), 16)
        p = int(line['p'], 16)
        g = int(line['g'], 16)
        A = int(line['A'], 16)

        # This code is creating a JSON object with keys "p", "g", and "A" and their corresponding
        # values as hexadecimal strings converted from the integer variables `p`, `g`, and `p`
        # respectively. The `json.dumps()` method is used to convert the Python dictionary to a JSON
        # string. The resulting JSON payload and its length are printed to the console, and then sent
        # to the remote server using the `pr.sendlineafter(": ", payload)` method.
        payload = json.dumps({"p":hex(p),"g":hex(g),"A":hex(p)})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        # This code is reading data from the remote server using the `pr.readuntil(": ")` method,
        # which reads data from the server until it encounters a colon (`:`) character. The data is
        # then loaded as a JSON object using `json.loads(pr.readline().strip().decode())`. The value
        # of `B` is extracted from the JSON object by converting the hexadecimal string to an integer
        # using the `int()` function with a base of 16.
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        B = int(line['B'], 16)

        # This code is creating a JSON object with a key "B" and its corresponding value as the
        # hexadecimal string converted from the integer variable `p`. The `json.dumps()` method is
        # used to convert the Python dictionary to a JSON string. The resulting JSON payload and its
        # length are printed to the console, and then sent to the remote server using the
        # `pr.sendlineafter(": ", payload)` method. This is part of a larger exploit script that is
        # communicating with a remote server and sending JSON payloads to it.
        payload = json.dumps({"B":hex(p)})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        print(line)

        # This code is decrypting an encrypted flag using AES encryption in CBC mode.
        iv = bytes.fromhex(line['iv'])
        encrypted_flag = bytes.fromhex(line['encrypted_flag'])
        sha1 = hashlib.sha1()
        secret = 0
        sha1.update(str(secret).encode())
        key = sha1.digest()[:16]
        aes = AES.new(key, AES.MODE_CBC, iv)
        print(aes.decrypt(encrypted_flag))
    finally:
        pr.close()

exploit()