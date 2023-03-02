import string
import time

class Cezar:
    def __init__(self):
        self.alphabet_index = list(range(0, 26))
        self.alphabet_chars = list(string.ascii_uppercase)
        self.start = 0



    def check_validaton(self,char):
        if char not in self.alphabet_chars:
            return {
                "time": time.time() - self.start,
                "context": "",
                "response": {
                    "process": False,
                    "error": "Incorrect input, the symbol " + char + " is not accepted. Only A-Z, a-z"
                }

            }
        else: return False



    def encrypt_message(self,string,key,mode,key2):
        self.start = time.time()
        text= list(string.upper().replace(" ",""))
        key2 = key2.upper().replace(" ","")
        new_string = ""
        if 1 <= len(key2) < 7:
            return {
                    "time":time.time()-self.start,
                    "context": "",
                    "response": {
                        "process": False,
                        "error": "Text key is wrong, length of key should be more than 7 or equal"
                    }
            }
        elif len(key2) >= 7:
            new_alphabet = []
            for char in key2:
                check = self.check_validaton(char)
                if check:
                    return check
                if char not in new_alphabet:
                    new_alphabet.append(char)
            '''if 1 <= len(new_alphabet) < 7:
                return {
                    "time":time.time()-self.start,
                    "context": "",
                    "response": {
                        "process": False,
                        "error": "After processing the key, its length is less than 7, you can enter a key with repeated characters, but the length of non-repeating characters must be greater than or equal to 7"
                    }
            }'''
            for char in self.alphabet_chars:
                if char not in new_alphabet:
                    new_alphabet.append(char)

            for char in text:
                check = self.check_validaton(char)
                if check:
                    return check
                new_string += new_alphabet[(new_alphabet.index(char) + mode * key) % 26]
            return {
                "time": time.time() - self.start,
                "context": new_string,
                "response": {
                    "process": True,
                    "error": ""
                }
            }
        else:
            for char in text:
                check = self.check_validaton(char)
                if check:
                    return check
                new_string += self.alphabet_chars[(self.alphabet_chars.index(char)+mode*key) % 26]
            return {
                "time": time.time() - self.start,
                "context": new_string,
                "response": {
                    "process": True,
                    "error" : ""
                }
            }


