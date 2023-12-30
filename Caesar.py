
class CaesarAlg:

    # upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    def __init__(self, lang=False, direction=False, shift=False):

        self.lang = lang
        self.direction = direction
        if shift is not False:
            self.fixed = True
        else:
            self.fixed = False

        self.silent = True

        self.get_settings()
        self.request_text(self.silent)
        self.construct_output()

    def get_settings(self):

        if self.lang is False and self.direction is False:
            self.silent = False

        if self.lang is False and self.silent is False:
            # getting language and target for encryption
            self.lang = input('Enter lang (en, ru):')
        else:
            self.lang = 'en'

        # define language for coding\decoding
        if self.lang.startswith('en'):
            self.lang = 'en'
            self.alpha = self.lower_eng_alphabet
            self.max_shift = 26
        else:
            self.lang = 'ru'
            self.alpha = self.lower_rus_alphabet
            self.max_shift = 32

        if self.direction is False and self.silent is False:
            self.direction = input('Enter direction (encrypt, decrypt):')
        else:
            self.direction = 'enc'

        # define if we need to encrypt  message or decrypt it
        if self.direction.startswith('enc'):
            self.direction = 'encr'
        elif self.direction.startswith('dec'):
            self.direction = 'decr'
        else:
            self.direction = 'encr'

        # define algorithm
        if self.silent is False:
            while True:
                self.fixed = input('Fixed or variable shift? (fix, var):')
                if self.fixed.startswith('fix'):
                    self.fixed = True
                    break
                elif self.fixed.startswith('var'):
                    self.fixed = False
                    break
                else:
                    print('Wrong input try again\n')

        # requesting the shift if fixed algorithm
        if self.fixed is True and self.silent is False:
            while True:
                self.shift = input('Set shift:')
                try:
                    self.shift = int(self.shift) % self.max_shift
                    break
                except ValueError:
                    print('Entered shift is not a number, try again')
                    continue

    def request_text(self, silent=True):
        # getting the text for the task
        request = ''
        if silent is False:
            request = f'Enter the text for the {self.direction}yption:'

        self.text = input(request)
        if self.lang == 'ru':
            self.text.replace('ё', 'е')

    def construct_output(self):
        if self.direction == 'encr':

            if self.fixed:
                output = self.caesar_encr(self.text)
            else:
                output = self.split_output()
        else:
            if self.fixed:
                output = self.caesar_decr(self.text)
            else:
                output = self.split_output()
        print(output)

    def split_output(self):
        output = ''
        start = 0
        stop = len(self.text)-1
        for i, char in enumerate(self.text):
            if char.lower() not in self.alpha:
                if start != i:
                    self.shift = (i - start) % self.max_shift
                    if i == stop:
                        self.shift = (i - start) % self.max_shift
                    output += self.caesar_encr(self.text[start:i])
                output += char
                start = i + 1

            elif i == stop:
                self.shift = (i - start + 1) % self.max_shift
                output += self.caesar_encr(self.text[start:i+1])

        return output

    def caesar_encr(self, text):
        encrypted_text = ''

        for c in text:
            curr_idx = self.alpha.find(c.lower())

            if curr_idx != -1:
                encr_idx = (curr_idx + self.shift) % self.max_shift
                encrypted_char = self.alpha[encr_idx]

                if c.isupper():
                    encrypted_char = encrypted_char.upper()
            else:
                encrypted_char = c

            encrypted_text += encrypted_char

        return encrypted_text

    def caesar_decr(self, text):
        decrypted_text = ''

        for c in text:
            curr_idx = self.alpha.find(c.lower())

            if curr_idx != -1:
                decr_idx = (curr_idx - self.shift)
                decrypted_char = self.alpha[decr_idx]

                if c.isupper():
                    decrypted_char = decrypted_char.upper()
            else:
                decrypted_char = c

            decrypted_text += decrypted_char

        return decrypted_text


x = CaesarAlg(lang='en', direction='encr', shift=False)
