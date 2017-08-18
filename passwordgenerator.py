#coding:utf-8
from datetime import date, timedelta, datetime
from itertools import product as iter_product

LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET = LOWER_LETTERS + UPPER_LETTERS
DIGITS = '0123456789'
NORMAL = ALPHABET + DIGITS
PUNCTUATION = ' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
VISIBLE = ALPHABET + DIGITS + PUNCTUATION
ASCII_LETTERS = [chr(i) for i in range(0xff+1)] 

class PasswordGenerator(object):
    def product(self, *iterables, **kw):
        repeat = kw.get('repeat', 1)
        for i in iter_product(*iterables, repeat=repeat):
            yield ''.join(i)

    def product_digits(self, length):
        return self.product(DIGITS, repeat=length)

    def product_visible_letters(self, length):
        return self.product(VISIBLE, repeat=length)

    def product_all_letters(self, length):
        return self.product(ASCII_LETTERS, repeat=length)

    def product_letters(self, pass_format):
        """
            using hashcat password format with additional ?p?n
            ?l = abcdefghijklmnopqrstuvwxyz
            ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
            ?d = 0123456789
            ?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            ?a = ?l?u?d?s
            ?b = 0x00 - 0xff
            ?p = ?l?u
            ?n = ?l?u?d
            format: [{types}]{number}[{type}]{number}...
            type: a -> ascii_letters
                  d -> digits
                  p -> punctution
                  l -> letters(a+d+p)
            number: repeat time
            example:
                  [d]8: 8 bytes digit(12345678)
                  [a]3[d]3: 3 bytes ascii_letters + 3 bytes digits(xxx123)
                  [ad]5: 5 bytes asccii_letters or digits(a34Fe)
        """
        return self.product(letters, repeat=length)

    def product_date(self, start_date, end_date):
        d = start_date = datetime.strptime(start_date, '%Y%m%d').date()
        end_date = datetime.strptime(end_date, '%Y%m%d').date()
        day1 = timedelta(days=1)
        while d<=end_date:
            yield d
            d += day1

    def product_birthday(self, start_date='19700101', end_date=None, century=1):
        if century:
            output_format = '%Y%m%d'
        else:
            output_format = '%y%m%d'
        if not end_date:
            end_date = date.today().strftime('%Y%m%d')
        for d in self.product_date(start_date, end_date):
            yield d.strftime(output_format)
        
    def product_month_day(self):
        # choose 2000 for there is 20000229
        for d in self.product_date('20000101', '20001231'):
            yield d.strftime('%m%d')

    def product_chinesename_shortcut(self):        
        name_alphabet = ALPHABET.replace('u', '').replace('U', '')\
                                .replace('v', '').replace('V', '')\
                                .replace('e', '').replace('E', '')\
                                .replace('i', '').replace('I', '')
        chars = list(p.product(name_alphabet, repeat=3))
        for i in p.product(chars):
            yield i
        chars = list(p.product(name_alphabet, repeat=2))
        for i in p.product(chars):
            yield i

p = PasswordGenerator()
for i in p.product_chinesename_shortcut():
    print i
