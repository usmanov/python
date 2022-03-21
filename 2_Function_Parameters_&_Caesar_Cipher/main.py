# alphabet = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


# def encrypt(text, shift):

#     # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     new_text = ""
#     # version 1
#     # for i in range(0, len(text)):
#     #     for j in range(0, len(alphabet)):
#     #         if text[i] == alphabet[j]:
#     #             new_text += chr(ord(alphabet[j]) + shift)

#     # version 2
#     # new_text = ''.join(chr((ord(char) - 97 + shift) % 26 + 97)
#     #                    for char in text)

#     # version 3
#     # for letter in text:
#     #     position = alphabet.index(letter)
#     #     new_position = position + shift
#     #     new_letter = alphabet[new_position]
#     #     new_text += new_letter

#     print(new_text)


# # >> > mylist = ['first', 'second', 'other']
# # >> > s = ""
# # >> > for item in mylist:
# # ...    s += item


# # e.g.
# # plain_text = "hello"
# # shift = 5
# # cipher_text = "mjqqt"
# # print output: "The encoded text is mjqqt"
# # HINT: How do you get the index of an item in a list:
# # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
# # Bug alert: What happens if you try to encode the word 'civilization'?
# # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# # encrypt(text, shift)


# alphabet = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


# def decrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The decoded text is {cipher_text}")


# # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# # e.g.
# # cipher_text = "mjqqt"
# # shift = 5
# # plain_text = "hello"
# # print output: "The decoded text is hello"


# # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("You must specify a direction, try again")

# from turtle import position


# alphabet = [
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
#     "a",
#     "b",
#     "c",
#     "d",
#     "e",
#     "f",
#     "g",
#     "h",
#     "i",
#     "j",
#     "k",
#     "l",
#     "m",
#     "n",
#     "o",
#     "p",
#     "q",
#     "r",
#     "s",
#     "t",
#     "u",
#     "v",
#     "w",
#     "x",
#     "y",
#     "z",
# ]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# variant 1
# def caesar(text,shift,direction):
#     if direction == "encode":
#         cipher_text = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position + shift
#             cipher_text += alphabet[new_position]
#         # print("The encoded text is {}".format(cipher_text))
#         print(f"The {direction}d text is {cipher_text}")
#     elif direction == "decode":
#         plain_text = ""
#         for letter in text:
#             position = alphabet.index(letter)
#             new_position = position - shift
#             plain_text += alphabet[new_position]
#         # print("The encoded text is {}".format(plain_text))
#         print(f"The {direction}d text is {plain_text}")

# variant 2
# def caesar(text,shift,direction):
#     new_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         if direction == "encode":
#             new_position = position + shift
#         elif direction == "decode":
#             new_position = position - shift
#         new_text += alphabet[new_position]
#     print(f"The {direction}d text is {new_text}")


# variant 3
# def caesar(text,shift,direction):
#     new_text = ""
#     if direction == "decode":
#         shift *= -1
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_text += alphabet[new_position]
#     print(f"The {direction}d text is {new_text}")

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(text,shift,direction)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
restart = True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  if shift > 26:
      shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  answer = input("Do you want to restart the cipher? Enter yes / no:")
  if answer == "yes":
    restart = True
  elif answer == "no":
    restart = False

print("Goodbye!")