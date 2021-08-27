#!/usr/bin/env python
# coding: utf-8

# # Read from file
# - read into format of json
# - take one stack and find it's corresponding factorials 
# - return into the format of:
#     {'stack1': {'factorial':[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]}, 
#     'stack2': {'factorial': [479001600, 2, 6, 120, 720, 40320, 362880, 3628800]}, 
#     'stack3': {'factorial': [479001600, 2, 6, 120, 720, 40320, 362880, 3628800]}}


import json

class IntegerFactorial:
    
    def __init__(self, program_name):
        self.program_name = program_name
    
    def welcome(self):
        print("welcome to the " + self.program_name + " class..!!")
    
    def input_integer(self):
        
        while (True):
            try:
                input_value = int(input("Enter any integer: "))
                return input_value
            except:
                print("please input valid integer..!")
                
                
    def factorial(self, number):
        
        factorial = 1
        input_value = number

        while (number > 0):
            factorial*= number
            number-=1
        if(input_value >= 0):
            if(factorial%2 == 0):
                print("Factorial of ",input_value, " is: ", factorial, ": even")
            else:
                print("Factorial of ",input_value, " is: ", factorial, ": odd")
        else:
            print("Factorial of ",input_value, " is not possible")
            
    
    def factorial_number(self, number):
        
        factorial = 1
        input_value = number

        while (number > 0):
            factorial*= number
            number-=1
        if(input_value >= 0):
            return factorial
        else:
            return False

    def readFile(self, path):
        try:
            file1 = open(path,"r")
            value = file1.read()
            json_value = json.loads(value)
            print(type(json_value))
            return json_value        
        except FileNotFoundError:
            print("invalid path entered")
        finally:
            file1.close()
            
    def writeFile(self, path, dict_value):
        try:
            file1 = open(path,"w")
            file1.write(str(dict_value))
            return True        
        except FileNotFoundError:
            print("invalid path entered")
            return False
        finally:
            file1.close()
    
    def useDictionary(self, dict_value):
        dict_values = {}
        stack_string = "stack"
        count = 1
        for key in dict_value:
            dict_temp = {}
            splitted_list = dict_value[key]
            
            stack = [self.factorial_number(item) for item in splitted_list]
                #stack.append(self.factorial_number(item))
            
            dict_temp["factorial"] = stack
            dict_values[(stack_string+str(count))] = dict_temp
            count+= 1
            
        return dict_values
        

def main():
    print("Hello People!")
    path_read = "input_stream.txt"
    path_write = "output.txt"
    fobject = IntegerFactorial("FACTORIAL APP")
    
    fobject.welcome()
#     number = fobject.input_integer()
#     fobject.factorial(number)
    read_as_dict = fobject.readFile(path_read)
    dict_output = fobject.useDictionary(read_as_dict)
    print(dict_output)
    print(fobject.writeFile(path_write,dict_output))


if __name__ == "__main__":
    main()