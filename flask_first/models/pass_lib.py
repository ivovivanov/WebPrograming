from random import choice
from string import ascii_letters, digits, punctuation

class passlib():
    pass_lenght = 20
    def gen_letter_only(self):
        ret_pass = str()
        for _ in range(passlib.pass_lenght):
            ret_pass += choice(ascii_letters)
        return ret_pass

    def gen_letter_digit(self):
        ret_pass = str()
        for _ in range(passlib.pass_lenght):
            ret_pass += choice(ascii_letters+digits)
        return ret_pass

    def gen_letter_digit_chars(self):
        ret_pass = str()
        for _ in range(passlib.pass_lenght):
            ret_pass += choice(ascii_letters+digits+punctuation)
        return ret_pass

if __name__ == '__main__':
    pass_obj = passlib()
    print(pass_obj.gen_letter_only())
    print(pass_obj.gen_letter_digit())
    print(pass_obj.gen_letter_digit_chars())
