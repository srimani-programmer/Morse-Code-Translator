# Morse Code Generator
# done by @Sri_Programmer
# python v3.7.2

class Generator:

    def __init__(self, filename):
        
        # Morse Code Dictionary for the Encryption and Decryption

        self.MORSE_CODE_DICTIONARY = {
                    'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    'a':'.-', 'b':'-...', 
                    'c':'-.-.', 'd':'-..', 'e':'.', 
                    'f':'..-.', 'g':'--.', 'h':'....', 
                    'i':'..', 'j':'.---', 'k':'-.-', 
                    'l':'.-..', 'm':'--', 'n':'-.', 
                    'o':'---', 'p':'.--.', 'q':'--.-', 
                    'r':'.-.', 's':'...', 't':'-', 
                    'u':'..-', 'v':'...-', 'w':'.--', 
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'
        }

        self.filename = filename

    
    def encryption(self):

        # Handling the file data

        output_file = open('output','w')
        try:
            file_handle = open(self.filename,'r')
            file_data = file_handle.readlines()

            # It will parse through all the lines            
            for data in file_data:
                # It will parse through the set of lines
                cipher = ''
                for content in data:
                    if content != ' ' and content != '\n':
                        cipher += self.MORSE_CODE_DICTIONARY[content] + ' '
                    elif content == '\n':
                        continue
                    else:
                        cipher += ''
                
                output_file.write(cipher)
                output_file.write('\n')

        except FileNotFoundError:
            print('Unable to find {} '.format(self.filename))

        finally:
            file_handle.close()
            output_file.close()

    def decryption(self):
        pass

print('1. Morse Code Generation')
print('2. Normal Text Generation')
choice = input('Enter your choice:')
user_file = input('Enter your filename: ')
g = Generator(user_file)

if int(choice) == 1:
    g.encryption()
elif int(choice) == 2:
    pass
else:
    pass


    
