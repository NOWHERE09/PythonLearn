def countdown(n):
    print("Counting down!")
    while n > 0:
        yield n
        n -= 1


def print_matches(matchtext):
    print("Looking for", matchtext)
    while True:
        line = (yield)
        if matchtext in line:
            print(line)


class Account(object):
    num_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1

    def __del__(self):
        Account.num_accounts -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance


import random


class EvilAccount(Account):
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * 1.10
        else:
            return self.balance


class MoreEvilAccount(EvilAccount):
    def deposit(self, amount):
        self.withdraw(5.00)
        super(MoreEvilAccount, self).deposit(amount)


class DepositCharge(object):
    fee = 5.00

    def deposit_fee(self):
        self.withdraw(self.fee)


class WithdrawCharge(object):
    fee = 2.50

    def withdraw_fee(self):
        self.withdraw(self.fee)


class MostEvilAccount(EvilAccount, DepositCharge, WithdrawCharge):
    def deposit(self, amt):
        self.deposit_fee(self, amt)
        super(MostEvilAccount, self).deposit(amt)

    def withdraw(self, amt):
        self.withdraw_fee(self, amt)
        super(MostEvilAccount, self).withdraw(amt)


class Foo(object):
    @staticmethod
    def add(x, y):
        return x + y


import time


class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        t = time.localtime(time.time() + 86400)
        return Date(t.tm_year, t.tm_mon, t.tm_mday)


##import csv
##csvfile = open("C:/Users/g01feng/Desktop/WHO CSV.csv", 'r')
##reader = csv.reader(csvfile)
##dict_reader = csv.DictReader(csvfile)

##for row in reader:
##	print(row)

##for row in dict_reader:
##	print(row)


##import json
##json_data = open("C:/Users/g01feng/Desktop/WHO_CSV.json").read()
##data = json.loads(json_data)
##for item in data:
##        print(item)


##from xml.etree import ElementTree as ET

##tree = ET.parse('I:/AN/WHO_XML.xml')
##root = tree.getroot()

##print(root)

##data = root.find('Data')

##all_data = []

##for observation in data:
##        record = {}
##        for item in observation:
##                lookup_key = list(item.attrib.keys())[0]

##                if lookup_key == 'Numeric':
##                        rec_key = 'NUMERIC'
##                        rec_value = item.attrib['Numeric']
##                else:
##                        rec_key = item.attrib[lookup_key]
##                        rec_value = item.attrib['Code']

##                record[rec_key] = rec_value

##        all_data.append(record)

##print(all_data)

##print(list(root))
##print(list(data))

##l_data = root.findall('Data')
##print(l_data)
##for observation in data:
##        for item in observation:
##                print(item)
##                print(item.text)
##                print(item.attrib)
##                print(list(item))

from xml.etree import ElementTree as ET

tree = ET.parse('I:/AN/WHO_XML.xml')
root = tree.getroot()
data = root.find('Data')
all_data = []
for observation in data:
    record = {}
    for item in observation:
        ##print(item.attrib)
        ##print(item.attrib.keys())
        lookup_key = list(item.attrib.keys())[0]
        if lookup_key == 'Numeric':
            rec_key = 'NUMERIC'
            rec_value = item.attrib['Numeric']
        else:
            rec_key = item.attrib[lookup_key]
            rec_value = item.attrib['Code']
        ##print(lookup_key)
        record[rec_key] = rec_value
    print(record)
