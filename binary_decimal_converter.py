"""
Practice Project: Binary to Decimal and vice-versa Conversion

Author: Guccifer Shubham (learner)
Instagram : Shubhushubhu99

Description:
This program converts binary numbers to decimal and vice versa.
It's a practice project and may not be perfect.
There might be slight inaccuracies in the binary to decimal conversion due to rounding numbers
assumed in the code.

Warning:
Use this program for learning purposes only.
It may not handle all edge cases or provide exact precision in conversions.

"""

import os,pyfiglet

def clear_func():
    if os == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Binary_Decimal():
    bin_dec = float(input("Enter any Binary number :"))
    bin_dec_str = str(bin_dec)

    x = bin_dec_str.find(".")
    y = (len(bin_dec_str[x:]))
    z = int(y)              

    int_part = int(bin_dec)
    frac_part = bin_dec - int_part
    rounded_frac_part = round(frac_part, z-1 )
    rounded_frac_part_str = str(rounded_frac_part)
    rounded_frac_part_str_int = int(rounded_frac_part_str[2:])
    # print(rounded_frac_part_str_int)
    val1, i1 = 0,0
    while int_part > 0:
        r1 = int_part % 10
        exp1 = r1*(2**i1)
        val1 = val1 + exp1
        int_part = int_part//10
        i1 = i1 + 1

    val2, i2 = 0,0
    while rounded_frac_part_str_int > 0:
        r2 = rounded_frac_part_str_int % 10
        exp2 = r2*(2**-i2)
        val2 = val2 + exp2
        rounded_frac_part_str_int = rounded_frac_part_str_int//10
        i2 = i2 + 1

    print("Decimal value is:",val1 + val2) 
    
def Decimal_Binary():
    bin_dec = float(input("Enter any Binary number :"))
    bin_dec_str = str(bin_dec)

    x = bin_dec_str.find(".")
    y = (len(bin_dec_str[x:]))
    z = int(y)   

    int_part = int(bin_dec)
    frac_part = bin_dec - int_part
    rounded_frac_part = round(frac_part, z-1 )
    rounded_frac_part_str = str(rounded_frac_part)
    rounded_frac_part_str_int = int(rounded_frac_part_str[2:])

    val1, i1 = "",0
    while int_part > 0:
        r = str(int_part%2)
        val1 = val1 + r
        int_part = int_part//2
        i1 = i1 + 1    
    # print(val1[-1::-1])
    val2,i2 = "", 0    
    while rounded_frac_part_str_int > 0:
        r = str(rounded_frac_part_str_int%2)
        val2 = val2 + r
        rounded_frac_part_str_int = rounded_frac_part_str_int//2
        i2 = i2 + 1 
    point = "."   
    print(f"Conversion of Decimal to Binary is :", val1[-1::-1]+point+val2)          


clear_func()
text =pyfiglet.figlet_format("B <-> D")
print(text) 

print("[1] Binary to Decimal")
print("[2] Decimal to Binary")
print("[3] Exit")
opt = int(input("Enter Your Choice :"))

if opt == 1:
    # print("option will be added soon")
    Binary_Decimal()
elif opt == 2:
    # print("option will be added soon")
    Decimal_Binary
elif opt == 3:
    print("Thanks for using this program")
    os.system("exit")









