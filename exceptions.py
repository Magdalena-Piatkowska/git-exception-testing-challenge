# BROAD REASONS WHY YOU MIGHT GET AN EXCEPTION
# (1) Trying to refer to something that doesn't exist
# (2) Using a value that is inappropriate in some way

# CORE EXAMPLES OF EXCEPTIONS IN THIS FILE
# AttributeError (1)
# KeyError (1)
# IndexError (1)
# NameError (1)
# UnboundLocalError (1)
# TypeError (2)
# ValueError (2)
# ZeroDivisionError (2)
# OverflowError (2)
# FileNotFoundError (1)
# UnicodeEncodeError (2)
# ModuleNotFoundError (1)
# ImportError (1)

# BONUS EXAMPLES YOU CAN TRY IF YOU WISH
# PermissionError (2)
# IsADirectoryError (2)


# AttributeError - EXAMPLE
def produce_attribute_error():
    print(12.34.upper())



# KeyError
def produce_key_error():
    ages = {"tom": 3, "Kim": 32, "Lee": 23}
    print(ages["jack"])

# IndexError
def produce_index_error():
    animals = ['lion', 'tiger', 'bear']
    print(animals[3])


# NameError
def produce_name_error():
    spelling = 'abc'
    print(spellling)


# UnboundLocalError
def produce_unbound_local_error():
    counter = 0
    def increment():
        # global counter
        counter += 1
    increment()


# TypeError
def produce_type_error():
    text = "python"
    number = 2
    print(text + number)


# ValueError
def produce_value_error():
    num = int("string")


# ZeroDivisionError
def produce_zero_division_error():
    print(20/0)

# OverflowError
def produce_overflow_error():
    import math
    print(math.exp(250000))


# FileNotFoundError
def produce_file_not_found_error():
    with open('haiku.txt', 'r') as file:
        text = file.read()


# UnicodeEncodeError
def produce_unicode_encode_error():
    pass


# ModuleNotFoundError
def produce_module_not_found_error():
    import a
    print (a.find())


# ImportError
def produce_import_error():
    from lol import lol
