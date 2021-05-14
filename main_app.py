# Call module 'functions.py'
from functions import string_reverse
# Importing Fore (foreground color)  Back (background color) the package "colorama"
from colorama import Fore, Back

print('Reverse String of AIRPORT is : ', string_reverse('AIRPORT'))

print(Fore.LIGHTBLUE_EX + 'Reverse String of FULLSTACK DEVELOPER is : ',
      string_reverse('FULLSTACK DEVELOPER'))

print(Back.RED + 'Reverse String of DESIGNER is : ', string_reverse('DESIGNER'))
print(Fore.RESET + Back.RESET)
