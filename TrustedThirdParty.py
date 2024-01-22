# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""

# Trusted Third Party (TTP)

import pandas as pd
import time
import random
import sharedMethods

print("Trusted Third Party")

# Generate flag for identification number in the CSV file.
flag = 1

TTP_Objects = []
TTP_ListOfObjects = []

# TTP calculates RSA modulus n=pq. Keep p, and q private, and make n public.
p = 101
q = 757
n = p*q

# Add them to a list, and append that list to another list, which stores all data.
TTP_Objects.append(flag)
TTP_Objects.append("n")
TTP_Objects.append(n)
TTP_ListOfObjects.append(list(TTP_Objects))

print("\nGenerate RSA modulus n=pq")
print("n =",n, "=",p,"*",q,"")


# TTP chooses real number "a", and makes it public.
a = random.randint(4, 10)
print("\nTTP Chooses real number a =",a)
print("(a indicates the number of rounds to perform the proof)")


# Add variable a to the lists, for the CSV file.
TTP_Objects[0] = flag
TTP_Objects[1] = "a"
TTP_Objects[2] = a
TTP_ListOfObjects.append(list(TTP_Objects))


# Create Dataframe, and save as CSV.
print("\n\nMake RSA n value, and a value public.")
TTP_Dataframe = pd.DataFrame(TTP_ListOfObjects, columns=["flag", "Variable", "VariableData"])
TTP_Dataframe.to_csv('C:/Users/.../TTP.csv',  index=False)  #header=False,


# Register Person A's Private Key
# Continually open Person A's Private Key file, and check whether flag has been changed.
print("\n\nLoading Person A's Private Key...")
print("(Please run the Person A script in another console.)")
personA_PrivateKey = sharedMethods.readFile("C:/Users/.../A_PrivateKey.csv", 1)
print("\nPerson A's Data Loaded")

# Retrieve person A's public key.
for i in range(len(personA_PrivateKey)):
    if personA_PrivateKey.Variable[i] == "personAPrivateKey":
        TTP_A_SecretKey = personA_PrivateKey.VariableData[i]

# Register Person B's private keys
print("\n\nLoading Person B's Data...")
print("(Please run the Person B script in another console.)")
personB_PrivateKey = sharedMethods.readFile("C:/Users/.../B_PrivateKey.csv", 1)
print("\nPerson B's Data Loaded")

# Retrieve person B's public key.
for i in range(len(personB_PrivateKey)):
    if personB_PrivateKey.Variable[i] == "personBPrivateKey":
        TTP_B_SecretKey = personB_PrivateKey.VariableData[i]

print("\n\nRegister Person A's and Person B's private keys")
print("A Secret Key:", TTP_A_SecretKey)
print("B Secret Key:", TTP_B_SecretKey)
