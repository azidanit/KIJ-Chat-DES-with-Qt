from DES import DES

des = DES()

msg_to_encrpyt = "Aku "

msg_chunk = des.splitIntoChunk(msg_to_encrpyt)

enc_chunk = des.encryptChunkList(msg_chunk)

print(msg_chunk)
print(enc_chunk)

all_enc = ""

for i in enc_chunk:
    all_enc += i

print(all_enc)
print(len(all_enc))


print("--------------------------------------")

enc_msg_chunk = des.splitIntoChunk(all_enc)
dec_chunk = des.decryptChunkList(enc_msg_chunk)

print(enc_msg_chunk)
print(dec_chunk)

all_dec = ""

for i in dec_chunk:
    all_dec += i

print(all_dec)

#check carry space
pos_space = 1
for i in range(len(all_dec)):
    pos_space = i + 1
    if " " != (all_dec[-pos_space]):
        break

print(pos_space)
print(all_dec[:-pos_space + 1])
