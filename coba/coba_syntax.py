# import subprocess
#
# # subprocess = subprocess.Popen("python enkripsi.py", shell=True, stdout=subprocess.PIPE)
# subprocess = subprocess.Popen('python enkripsi.py {} {}'.
#                               format("JUKRIDAN", "azidanit"),
#                               shell=True, stdout=subprocess.PIPE)
# subprocess_return = subprocess.stdout.read()
# print(subprocess_return.decode()[:-1])

# print("HAHA")
# dec_array = [13,2,3,4,5,10]
#
# hex_array = [hex(x) for x in dec_array]
#
# hex_str = ""
#
# for i in dec_array:
#     hex_str += hex(i)
#
# print(hex_array)
# print(hex_str)
#
# splitted_hex_str = hex_str.split("0x")
# print(splitted_hex_str[1:])
str = "RSA_KEY," + str(222222) + "," + str(33333)
print(str[:7])
print(str.split(','))

# for i in splitted_hex_str[1:]:
#     print(int(i,16))
#
# str = format(18, '#04x')[2:]
# print(str)

# msg = "a"
#
# msg_int = ord(msg)
#
# print(msg_int)

import enkripsi_one

# print(enkripsi_one.enkripsiLur("azida\nit"))

# msg_to_encrpyt = "Aku "

# chunk = len(msg_to_encrpyt)//8
# carry_space = ""
# if len(msg_to_encrpyt) > (chunk * 8):
#     # print("exe")
#     chunk += 1
#     carry_space = " " * ((chunk*8) - len(msg_to_encrpyt))
#
# print(chunk)
# print(carry_space)
#
# y = 0
# for i in range(chunk - 1):
#     y = i * 8
#     print(msg_to_encrpyt[y:y+8])
#
# print(msg_to_encrpyt[y+8:] + carry_space)
# print(msg_to_encrpyt + carry_space)
#
# carry_space = "A" * 2
# import argparse
#
# my_parser = argparse.ArgumentParser(description='DES ENCRYPTION')
# # Add the arguments
# my_parser.add_argument('Key',
#                        metavar='key',
#                        type=str,
#                        help='key to use DES')
# my_parser.add_argument('PlainText',
#                        metavar='plaintext',
#                        type=str,
#                        help='text to encrypt DES')
#
# args = my_parser.parse_args()
#
# key_input = args.Key
# pt_input = args.PlainText
#
# print("KEY NYA", key_input)
# print("PT NYA", pt_input)