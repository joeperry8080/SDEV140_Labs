'''
Write a class named Person with data attributes for a person’s name, address, and telephone number. 
Next, write a class named Customer that is a subclass of the Person class. 
    The Customer class should have a data attribute for a customer number, and a 
    Boolean data attribute indicating whether the customer wishes to be on a mailing list. 
Demonstrate an instance of the Customer class in a simple program (15 points).
'''
from operator import add
from unicodedata import name

class Person():
    def __init__(self, name, address, tel_number):
        self.name = name
        self.address = address
        self.tel_number = tel_number

    def __str__(self):
        return f"{self.name}, {self.address}, {self.tel_number}"

class Customer(Person):

    def __init__(self, name, address, tel_number, cust_number, mail_list):
        Person.__init__()
        self.cust_number = cust_number
        self.mail_list = bool(mail_list)

        Person.__init__(self, name, address, tel_number)

    def __str__(self):
        return f"Customer Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone}\
        \nCustomer Phone Number: {self.cust_number}\nMailing List: {self.mail_list}\n"

my_person = Customer("Joe", "123 Main Street", "555-1212", "12345", "N")
#my_person = Customer('Joe Perry', '300 N 17th St Noblesville, IN 46060','317-921-4628', '12345', 'N')

print(my_person)


