import enkripsi_one
import dekripsi_one

class DES:
    def __init__(self):
        pass
        self.key_str_des = self._generateDesKey()

    def _generateDesKey(self):
        import string
        import random
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return ran

    def setDesKey(self, key_):
        self.key_str_des = key_

    def getDesKey(self):
        return self.key_str_des

    def encryptIntoString(self, msg_str):
        msg_chunk = self.splitIntoChunk(msg_str)

        enc_chunk = self.encryptChunkList(msg_chunk)
        all_enc = ""

        for i in enc_chunk:
            all_enc += i

        return all_enc

    def decryptIntoString(self, msg_str):
        enc_msg_chunk = self.splitIntoChunk(msg_str)
        dec_chunk = self.decryptChunkList(enc_msg_chunk)

        all_dec = ""

        for i in dec_chunk:
            all_dec += i

        # check carry space
        pos_space = 1
        for i in range(len(all_dec)):
            pos_space = i + 1
            if " " != (all_dec[-pos_space]):
                break

        # return all_dec[:-pos_space + 1]
        return all_dec

    def splitIntoChunk(self, msg_to_split):
        # msg_to_encrpyt = "Aku sayang kamu Juliii, hehe terimakasih telah ada yaaaa"
        chunk_msg = []
        chunk = len(msg_to_split) // 8
        carry_space = ""
        if len(msg_to_split) > (chunk * 8):
            # print("exe")
            chunk += 1
            carry_space = " " * ((chunk * 8) - len(msg_to_split))

        # print(chunk)
        # print(carry_space)

        y = 0
        for i in range(chunk - 1):
            y = i * 8
            print(msg_to_split[y:y + 8])
            chunk_msg.append(msg_to_split[y:y + 8])

        if(chunk == 1):
            chunk_msg.append(msg_to_split + carry_space)
        else:
            chunk_msg.append(msg_to_split[y + 8:] + carry_space)

        # print(msg_to_split[y + 8:] + carry_space)

        return chunk_msg

    def encryptChunkList(self, list_chunk):
        encrypted_chunk = []
        for i in list_chunk:
            encrypted_chunk.append(str(enkripsi_one.encryptDES(i, self.key_str_des)))
            # print(enkripsi_one.encryptDES(i))
        return encrypted_chunk

    def decryptChunkList(self, list_chunk):
        decrypted_chunk = []
        for i in list_chunk:
            decrypted_chunk.append(dekripsi_one.decryptDES(i, self.key_str_des))

        return decrypted_chunk
