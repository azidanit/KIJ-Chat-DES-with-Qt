import math
from prime_generator import *

class RSA:
    def __init__(self):
        self.prime_bit_size = 7

        self.p_prime = generate_prime(self.prime_bit_size)
        self.q_prime = generate_prime(self.prime_bit_size)
        while self.p_prime == self.q_prime:
            self.q_prime = generate_prime(self.prime_bit_size)

        self.n = self.p_prime * self.q_prime
        self.phi = (self.p_prime - 1) * (self.q_prime - 1)
        self.public_key, self.private_key = self._generate_keys()
        self.acc_public_key = None

    def _generate_keys(self):
        # find prime e that less than phi, for Public Key
        e = random.randint(2, self.phi - 1)
        while math.gcd(e, self.phi) != 1:
            e = random.randint(2, self.phi - 1)

        # find d for Private Key
        d = pow(e, -1, self.phi)

        public_key = (e, self.n)
        private_key = (d, self.n)

        return public_key, private_key

    def getMyPublicKey(self):
        return self.public_key

    def setAcrossPublicKey(self, acc_pub_key_):
        self.acc_public_key = acc_pub_key_
        print("SETTED UP pub key", self.acc_public_key)

    def encryptOneByte(self, msg):
        # print("ENCR", self.public_key[0], self.public_key[1])
        e1 = pow(msg,self.acc_public_key[0], self.acc_public_key[1])
        # print(e1)
        # e2 = e1 % self.public_key[1]

        return e1

    def decrypytOneByte(self, msg):
        # print("decrpyting", msg)
        e1 = pow(msg,self.private_key[0], self.private_key[1])
        # e2 = e1 % self.private_key[1]
        # print("decrypted int", e1)
        return e1

    def splitIntoOneBytes(self, string):
        pass

    def encryptMsg(self, msg):
        encrypted_string = ""

        for i in msg:
            encrypted_string += str(hex(self.encryptOneByte(ord(i))))

        return encrypted_string


    def decryptMsg(self, msg):
        decrypted_string = ""
        list_decrypted_hex = msg.split("0x")
        print(list_decrypted_hex[1:])
        for i in list_decrypted_hex[1:]:
            decrypted_string += chr(self.decrypytOneByte(int(i,16)))

        return decrypted_string


