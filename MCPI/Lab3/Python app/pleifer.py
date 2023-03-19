
class Pleifer:
    def __init__(self):
        self.alphabet = []
        for i in range(ord('А'), ord('Я')+1):
            self.alphabet.append(chr(i))
            if i == 1045:
                self.alphabet.append(chr(1025))

    def message_validation(self,message,mode):
        print(message)
        for item in message:
            if item not in self.alphabet and mode == 1:
                return {
                    "context": "",
                    "response": {
                        "process": False,
                        "error": f"The symbol {item} is invalid, only 'А - Я' 'а - я' "
                    }
                }
        return {
            "context": "",
            "response": {
                "process": True,
                "error": ""
            }
        }
    def key_validation(self,key):
        if not len(key) >= 7:
            return {
                "context": "",
                "response": {
                    "process": False,
                    "error": "The length of key should be more or equal than 7 symbols"
                }
            }
        for item in key:
            if item not in self.alphabet:
                return {
                    "context": "",
                    "response": {
                        "process": False,
                        "error": f"The symbol {item} is invalid, only 'А - Я' 'а - я' "
                    }
                }
        return {
                    "context": "",
                    "response": {
                        "process": True,
                        "error": ""
                    }
                }

    def key_processing(self,key):
        new_key = ""
        for i in key:
            if i not in new_key:
                new_key += i
        return new_key

    def create_matrix(self,key):
        used = []
        matrix = []
        tmp = []
        for i in key:
            if len(tmp) == 5:
                matrix.append(tmp)
                tmp = []
            if i != " ":
                tmp.append(i)
                used.append(i)

        for i in self.alphabet:
            if len(tmp) == 5:
                matrix.append(tmp)
                tmp = []
            if i not in used:
                tmp.append(i)

        if tmp not in matrix:
            tmp.append('0')
            tmp.append('1')
            matrix.append(tmp)

        for item in matrix:
            print(item)
        return matrix
    def matrix_separate(self,message,symbol):
        letter = ['Ф','Ъ','Ё']
        let_count = 0
        matrix_bin = []
        count = 0
        bin = []
        for i in range(len(message)):
            if count == 1:
                bin.append(message[i])
                if bin[0] == bin[1]:
                    tmp = bin[1]
                    bin[1] = letter[let_count]
                    let_count +=1
                    if let_count == len(letter):
                        let_count = 0
                    matrix_bin.append(bin)
                    bin = []
                    bin.append(tmp)
                    count = 1
                else:
                    count = 0
                    matrix_bin.append(bin)
                    bin = []
            else:
                bin.append(message[i])
                count+=1
        if len(bin) == 1:
            bin.append(symbol)
            matrix_bin.append(bin)
        return matrix_bin


    def encrypt(self,message,key,letter,mode):
        log = ""
        key = key.upper().replace(" ","")
        response = self.key_validation(key)
        if not response["response"]["process"]:
            return response
        key = self.key_processing(key)

        message = message.upper().replace(" ", "")
        response = self.message_validation(message,mode)
        if not response["response"]["process"]:
            return response
        matrix = self.create_matrix(key)
        matrix_bin = self.matrix_separate(message,letter)
        with open('log.txt', 'w', encoding='utf-8') as file:
            file.write("")
        with open ('log.txt','a',encoding='utf-8') as file:
            for item in matrix:
                lg = str(item)
                file.writelines(lg+"\n")

        print(matrix_bin)
        old = []
        for item in matrix_bin:
            new = []
            for letter in item:
                new.append(letter)
            old.append(new)
        print(message)
        x1,x2,y1,y2 = 0,0,0,0
        for item in matrix_bin:
            count = 0
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == item[0]:
                        x1 = i
                        y1 = j
                        count+=1
                    if matrix[i][j] == item[1]:
                        x2 = i
                        y2 = j
                        count +=1
                    if count == 2:
                        break
            if x1 != x2 and y1 != y2:
                item[0] = matrix[x1][y2]
                item[1] = matrix[x2][y1]
            elif x1 == x2:
                if y1 == len(matrix[0])-1:
                    y1 = -1
                if y2 == len(matrix[0])-1:
                    y2 = -1
                item[0] = matrix[x1][y1+(1*mode)]
                item[1] = matrix[x2][y2+(1*mode)]
            elif y1 == y2:
                if x1 == len(matrix)-1:
                    x1 = -1
                if x2 == len(matrix)-1:
                    x2 = -1
                item[0] = matrix[x1+(1*mode)][y1]
                item[1] = matrix[x2+(1*mode)][y2]

        new_string = ""
        print(matrix_bin)
        print(old)
        for item in matrix_bin:
            new_string += "".join(item)
        print(new_string)

        with open ('log.txt','a',encoding='utf-8') as file:
            file.write("\nProcessing matrix bin:\n\n")
            for i in range(len(matrix_bin)):
                file.write(str(old[i])+" --> "+str(matrix_bin[i])+"\n")
        return {
            "context": new_string,
            "response": {
                "process": True,
                "error": ""
            }
        }
