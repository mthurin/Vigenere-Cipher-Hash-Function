alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z', 26:',', 27:'.', 28:'-'}

def encrypt_message(plain_text, key):
    cipher_text = ""
    key_count = 0
    plain_text = capitalize_text(plain_text)
    key = capitalize_text(key)
    text_length = len(plain_text)
    key_length = len(key)
    master_key = make_key(text_length, key_length, key)
    for char in plain_text:
        if str.isalpha(char) == True:
            cipher_key = ((return_key(char) + return_key(master_key[key_count])) % 29)
            cipher_text = cipher_text + alphabet[cipher_key]
        else:
            cipher_key = ((return_key(char) + return_key(master_key[key_count])) % 29)
            cipher_text = cipher_text + alphabet[cipher_key]
        key_count = key_count + 1
    return cipher_text

def decrypt_message(encrypt_text, key):
    plain_text = ''
    key_count = 0
    encrypt_text = capitalize_text(encrypt_text)
    key = capitalize_text(key)
    text_length = len(encrypt_text)
    key_length = len(key)
    master_key = make_key(text_length, key_length, key)
    for char in encrypt_text:
        if str.isalpha(char) == True:
            plain_value = ((return_key(char) - return_key(master_key[key_count])) % 29)
            plain_text = plain_text + alphabet[plain_value]
        else:
            plain_value = ((return_key(char) - return_key(master_key[key_count])) % 29)
            plain_text = plain_text + alphabet[plain_value]
        key_count = key_count + 1
    return plain_text

def return_key(letter):
    for index in alphabet.keys():
        if alphabet[index] == letter:
        	return int(index)

def reverse_key(key):
    txt = []
    #goes through string in from last char to first char
    for i in range(len(key)-1, -1, -1):
        #appends each char to txt
        txt.append(key[i])
    return "".join(txt)

def make_key(t_length, k_length, key):
    while t_length > k_length:
        #adds key and reverse key
        key = key + reverse_key(key)
        #gets new length of key; should be 2xlen(key)
        k_length = len(key)
    if k_length > t_length:
        #shortens key to be the same as the plain_text
        key = key[0:t_length]
    return key

def capitalize_text(text):
    text = str.upper(text)
    text = text.replace(" ", "")
    return text

def print_list(string, read):
	print(string + ('').join(str(x) for x in read))

def shift_hash(binary):
	return binary[12:] + binary[:12]

def get_bits(s, woof):
    bit = "{0:08b}".format(ord(s))
    for x in range(0,8):
        woof[x] = bit[x:x+1]
    return woof

def get_first_byte(woof):
    return woof[:8]

def compare_byte(woof, ruppy, check):
    hi = int(("").join(woof),2)
    there = int(("").join(map(str,ruppy)),2)
    #print_list("first 8:", ruppy)
    #print_list("letter: ", woof)
    wow = hi ^ there
    howdy = "{0:08b}".format(wow)
    for x in range(0, 8):
        check[x] = howdy[x:x+1]
    
    #print_list("equals: ", check)
    return check


def add_bits(s, woof):
	bit = "{0:08b}".format(ord(s))
	for x in range(0,8):
			woof[x] = bit[x:x+1]
	return woof

def hash_input(string):
    new = [0] * 32
    car = [0] * 8
    test = [0] * 8
    check = [0] * 8
    for s in string:
        #print_list(s + ": \t", new)
        shifted = shift_hash(new)
        #print_list("Shift:\t",  shifted)
        select = get_first_byte(shifted)
        added = get_bits(s, car)
        result = compare_byte(added, select, check)
        #print_list("Result:\t",  result)
        new =  result + shifted[8:]
        #print_list("New:\t",  new)
    return new

def prompt_user():
    print("Would you like to encrypt or decrypt? ")
    print("1-Encrypt")
    print("2-Decrypt")
    print("3-Hash")
    print("4-Exit")
    print()
    answer = input("So, what's it going to be? ")
    try:
    	a = int(answer)
    except ValueError:
    	print("Pleas input a valid ineger")
    	prompt_user()
    if int(answer) == 1:
        plain_text = input("Enter in a message to be encrypted: ")
        key = input("Enter in a key: ")
        encrypt_text = encrypt_message(plain_text, key)
        print("Encrypted message: ")
        print(encrypt_text)
        prompt_user()
    elif int(answer) == 2:
        encrypt_text = input("Enter in a message to be decrypted: ")
        key = input("Enter in a key: ")
        decrypt_text = decrypt_message(encrypt_text, key)
        print("Decrypted message: ")
        print(decrypt_text)
        prompt_user()
    elif int(answer) == 3:
        plain_text = input("Enter in a message to be hashed: ")
        key = input("Enter in a key: ")
        hash_string = plain_text + key
        result = hash_input(hash_string)
        together = ('').join(str(x) for x in result)
        print("")
        print("Hashed: " + together)
        hexed  = "{0:0x}".format(int(together,2))
        print("Hexed: \t" + hexed)
        print("")
        prompt_user()
    elif int(answer) == 4:
    	print("Thanks! Have a good day!")
    else:
        print("You did not enter a valid answer")
        prompt_user()

prompt_user()