"""This module has function to generate password
"""
import random

def generate_password(
        length=12,
        include_digits=True,
        include_special_characters=True):
    """This function generates password
    
    Args:  
    """
    password = ""
    total_characters = string.ascii_letters 
    for index in range(length):
        password += random.choice('abcde')
    return password

print(generate_password(length=5))