import re

token = []  # an empty list, in order to generate the token
data_type = ['str', 'int', 'float', 'bool']
keywords = ['break', 'continue', 'return', 'goto', 'while', 'if', 'for', 'else', 'switch']
reserved_keywords = ['TRUE', 'FALSE']
operators = ['+', '-', '*', '/', '%', '=', '++', '--', '+=', '-=', '*/', '/=', '']
print("This is a program to build the lexical analyzer")
string = input("Enter your string: ")
# writing the input string into the source_code.txt file
with open("source_code.txt", "w") as file:
    file.write(string)
    file.close()
# reading the input string from source_code.txt file
with open("source_code.txt", "r") as file:
    string = file.read()  # getting the whole file inside a string
    file.close()
string = string.split()  # slicing the string into an array using the delimiter whitespace


# checking if there is a keyword present in the statements
def keyword_check(char):
    if char in keywords:
        token.append(["KEYWORD", char])


# checking the data type mentioned in the statements
def data_type_check(char):
    if char in data_type:
        token.append(["DATA_TYPE", char])


# checking if there is any identifier present in the statements
def identifier_check(char):
    if char[len(char) - 1] == ",":
        if char[:-1].lower() not in keywords and char[:-1].lower() not in data_type and char[
                                                                                        :-1] not in reserved_keywords:
            if re.match(r"^[a-zA-Z_0-9]+$", char) and char.isidentifier():
                token.append(["IDENTIFIER", char[:-1]])
    else:
        if char.lower() not in keywords and char.lower() not in data_type and char not in reserved_keywords:
            if re.match(r"^[a-zA-Z_0-9]+$", char) and char.isidentifier():
                token.append(["IDENTIFIER", char])


# checking the presence of any operator in the statements
def operator_check(char):
    if char in operators:
        token.append(["OPERATOR", char])


# checking for the string data type of the variable
def string_check(char):
    if re.match(r'"[^"]*"', char):
        if char[len(char) - 1] == ",":
            token.append(["STRING", char[:-1]])
            token.append(["END_STATEMENT", ","]) 
        else:
            token.append(["STRING", char])


# checking the integer data type of the variable
def integer_check(char):
    if re.match(r"^[-+]?[0-9]+[,]+$", char) or re.match(r"^[-+]?[0-9]+$", char):
        if char[len(char) - 1] == ",":
            token.append(["INTEGER", char[:-1]])
            token.append(["END_STATEMENT", ","])
        else:
            token.append(["INTEGER", char])


# checking the float data type of the variable
def float_check(char):
    if re.match(r"^[+-]?[0-9]+\.[0-9]", char):
        if char[len(char) - 1] == ",":
            token.append(["FLOAT", char[:-1]])
            token.append(["END_STATEMENT", ","])
        else:
            token.append(["FLOAT", char])


# checking the boolean data type of the variable
def boolean_check(char):
    if re.match(r"\W*(TRUE)\W*", char) or re.match(r"\W*(FALSE)\W*", char):
        if char[len(char) - 1] == ",":
            token.append(["BOOLEAN", char[:-1]])
            token.append(["END_STATEMENT", ","])
        else:
            token.append(["BOOLEAN", char])


# loop over the number of items present in the string array
for character in string:
    # checking if there is any keyword present
    keyword_check(character)
    # checking the data type
    data_type_check(character)
    # checking the presence of the identifier in the statement
    identifier_check(character)
    # checking the presence of the operator in the statement
    operator_check(character)
    # checking the format of the string data type
    string_check(character)
    # checking the format of the integer data type
    integer_check(character)
    # checking the format of float data type
    float_check(character)
    # checking the format of the boolean data type
    boolean_check(character)

print('The generated token is as follows ', token, "\n")
# ast = {'VariableDeclaration': []}
# # Now going to parse with the available token
# for a in range(len(token)):

#     token_type = token[a][0]
#     token_value = token[a][1]

#     if token_type == 'END_STATEMENT':
#         pass

#     if token_type == 'DATATYPE':
#         ast['VariableDeclaration'].append({'type': token_value})

#     if token_type == 'IDENTIFIER':
#         ast['VariableDeclaration'].append({'name': token_value})

#     if token_value == '=':
#         pass

#     if token_type == 'INTEGER' or token_type == 'STRING' or token_type == 'FLOAT' or token_type == 'BOOLEAN':
#         ast['VariableDeclaration'].append({'value': token_value})
# print(ast)
