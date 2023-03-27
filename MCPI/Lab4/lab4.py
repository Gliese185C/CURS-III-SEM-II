from ast import literal_eval

hex_dict = {
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}

bin_dict = {
    0:"0000",
    1:"0001",
    2:"0010",
    3:"0011",
    4:"0100",
    5:"0101",
    6:"0110",
    7:"0111",
    8:"1000",
    9:"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111"

}

class Des:
    def __init__(self):
        self.PC_1 = [[57,49,41,33,25,17,9],
                     [1,58,50,42,34,26,18],
                     [10,2,59,51,43,35,27],
                     [19,11,3,60,52,44,36],
                     [63,55,47,39,31,23,15],
                     [7,62,54,46,38,30,22],
                     [14,6,61,53,45,37,29],
                     [21,13,5,28,20,12,4]]

    def validation(self,message):
        if len(message) != 8:
            return {
                "status":{
                    "process":False,
                    "error":"The length of key should be equal 8"
                },
                "context":{
                    "key":"",
                    "keyp":"",
                    "hex":""
                }
            }
        else:
            return {
                "status": {
                    "process": True,
                    "error": ""
                },
                "context": {
                    "key": "",
                    "keyp": "",
                    "hex": ""
                }
            }


    def string_to_hex(self,string):
        hex_string = ""
        for item in string:
            hex_string += self.dec_to_hex(ord(item))
        return hex_string


    def dec_to_hex(self,number):
        string = ""
        while number > 0:
            tmp = number % 16
            if tmp in hex_dict:
                string += hex_dict[tmp]
            else:
                string += str(tmp)
            number //= 16
        return string[::-1]


    def hex_to_bin(self,string):
        string_bin = ""
        count = 0
        for item in string:
            if item in bin_dict:
                string_bin+=bin_dict[item]
                count+=1
            else:
                string_bin += bin_dict[int(item)]
                count+=1
            if count == 2:
                count = 0
                string_bin += " "

        return string_bin


    def key_expanded(self,message):
        response = self.validation(message)
        if not response["status"]["process"]:
            return response
        string_hex = self.string_to_hex(message)
        string_bin = self.hex_to_bin(string_hex)
        kplus_string = ""
        string_sp = string_bin.replace(" ","")
        for item in self.PC_1:
            for num in item:
                kplus_string += string_sp[num-1]
            kplus_string += " "
        with open("log.txt",'w') as file:
            file.write("\tPC-1 table\n\n")
            for item in self.PC_1:
                file.write(str(item)+'\n')
            file.write("\n\nHex format\n\n")
            count = 0
            for i in range(0,len(string_hex),2):
                file.write(message[count]+" ---> "+string_hex[i]+string_hex[i+1]+"\n")
                count +=1
            file.write("\n\nFrom hex to binary ( how ? )\n\n")
            for item in string_hex:
                if item in bin_dict:
                    file.write(item+" ---> "+bin_dict[item]+"\n")
                else:
                    file.write(item+" ---> "+bin_dict[int(item)]+"\n")
            file.write("\n\ninitial key ( binary )\n\n")
            count = 0
            block = 1
            string_up = ""
            string_down = ""

            for i in range(64):
                if i > 7:
                    string_up += string_sp[i] + "   "
                    string_down += str(i + 1) + " "
                else:
                    string_up += string_sp[i] + " "
                    string_down += str(i+1) + " "
                count +=1
                if count == 8:
                    file.write(f"\t {block} - block {i+1} bits total\n\n")
                    file.write(string_up+"\n"+string_down+"\n\n")
                    string_up = ""
                    string_down = ""
                    count = 0
                    block +=1
            count = 0
            block = 1
            string_up = ""
            string_down = ""
            kp = kplus_string.replace(" ", "")
            file.write("\n\nExtended key ( binary )\n\n")
            for i in range(len(self.PC_1)):
                for j in range(len(self.PC_1[i])):
                    string_up += kp[count] + "   "
                    string_down += str(self.PC_1[i][j]) + " "
                    count += 1
                file.write(f"\t {block} - block {count} bits total\n\n")
                file.write(string_up + "\n" + string_down + "\n\n")
                string_up = ""
                string_down = ""
                block += 1


        return {
                "status":{
                    "process":True,
                    "error":""
                },
                "context":{
                    "key":string_bin,
                    "keyp":kplus_string,
                    "hex":string_hex
                }
            }





