#!/usr/bin/env python3
# GitHub Lab 2: Inheritance with Classes

# Import Modules
from Main import Contact, ContactEmail, ContactPhone
import random, string, pytest

# Global Lambda Functions
lambda_str = lambda r: "".join(random.sample(string.ascii_letters, r))
lambda_adr = lambda r: " ".join([str(random.randint(1000,9000)), lambda_str(random.randint(5,12)), r])
lambda_eml = lambda r: "".join(["".join(random.sample(string.ascii_letters, r)), "@", "".join(random.sample(string.ascii_letters, r)), ".com"])
lambda_phn = lambda r: f"{r}".join([str(random.randint(200,999)),str(random.randint(100,999)),str(random.randint(1000,9999))])

def test_case1():
    "Case 1: Test set and get the First Name"

    c = Contact("John", "Smith")
    assert c.get_name_first() == "John"

    c = ContactEmail("John", "Smith", "jsmith@example.net")
    c.set_name_first("Victoria")
    assert c.get_name_first() == "Victoria"
    val = lambda_str(random.randint(4,10))
    c.set_name_first(f" {val} ")
    assert c.get_name_first() == val

    c = ContactPhone("John", "Smith", "555-555-5555")
    c.set_name_first("Jack ")
    assert c.get_name_first() == "Jack"

    val = lambda_str(random.randint(4,10))
    c = ContactPhone(val, "Smith", "555-555-5555")
    assert c.get_name_first() == val
    c.set_name_first(f" {val} ")
    assert c.get_name_first() == val

def test_case2():
    "Case 2: Test set and get the Last Name"

    c = Contact("John", "Smith")
    assert c.get_name_last() == "Smith"

    c = ContactEmail("John", "Smith", "jsmith@example.net")
    c.set_name_last("Rogers")
    assert c.get_name_last() == "Rogers"
    val = lambda_str(random.randint(4,10))
    c.set_name_last(f" {val} ")
    assert c.get_name_last() == val

    c = ContactPhone("John", "Smith", "555-555-5555")
    c.set_name_last("  Crusher ")
    assert c.get_name_last() == "Crusher"

    val = lambda_str(random.randint(4,10))
    c = ContactPhone("John", val, "555-555-5555")
    assert c.get_name_last() == val
    val = lambda_str(random.randint(4,10))
    c.set_name_last(f" {val} ")
    assert c.get_name_last() == val

def test_case3():
    "Case 3: Test set and get the Email"

    c = ContactEmail("John", "Smith", "jsmith@example.com")
    assert c.get_info() == "jsmith@example.com"

    c.set_info("\nhello@example.net\t ")
    assert c.get_info() == "hello@example.net"

    val = lambda_eml(random.randint(5,20))
    c = ContactEmail("John", "Smith", val)
    val = lambda_eml(random.randint(5,20))
    c.set_info(f"\n{val}\r")
    assert c.get_info() == val

    with pytest.raises(ValueError):
        c.set_info("Emailing Chaos")
        c.set_info("Raise @ Some . Chaos")
        c.set_info("Chaos In Testing Is Good")
        c.set_info(f" {lambda_eml(random.randint(5,20))}   ")

def test_case4():
    "Case 4: Test set and get the Phone"

    c = ContactPhone("John", "Smith", "555-555-9999")
    assert c.get_info() == "555-555-9999"

    c.set_info(" 444-555-2222 \t ")
    assert c.get_info() == "444-555-2222"

    val = lambda_phn("-")
    c = ContactPhone("John", "Smith", val)
    assert c.get_info() == val
    val = lambda_phn("-")
    c.set_info(f"\t{val}\n")
    assert c.get_info() == val

    with pytest.raises(ValueError):
        c.set_info("Dialing Chaos From International")
        c.set_info("191-212-456-7890")
        c.set_info("+14151231234")
        c.set_info(f"{lambda_eml(random.randint(7,15))}")

def test_case5():
    "Case 5: Test the count of elements in the count variable"
    Contact.contact_list = []

    c = Contact("John", "Smith")
    e = ContactEmail("Sarah", "Jane", "sjane@example.com")
    p = ContactPhone("Thomas", "Tom", "555-555-5555")
    assert len(Contact.contact_list) == 2

def test_case6():
    "Case 6: Verify Data Type of Elements in Class Variable"
    Contact.contact_list = []

    c = Contact("John", "Smith")
    e = ContactEmail("Sarah", "Jane", "sjane@example.com")
    p = ContactPhone("Thomas", "Tom", "555-555-5555")

    assert type(Contact.contact_list[0]) is ContactEmail
    assert type(Contact.contact_list[1]) is ContactPhone
