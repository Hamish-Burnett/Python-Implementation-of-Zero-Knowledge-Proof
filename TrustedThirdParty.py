# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""

# Trusted Third Party (TTP)

import pandas as pd
import time
import random

print("Trusted Third Party")

# Generate flag for identification number in the CSV file.
flag = 1



TTP_Objects = []
TTP_ListOfObjects = []

# TTP calculates RSA modulus n=pq. Keep p, and q private, and make n public.
p = 101
q = 757
n = p*q

# Add them to a list, and add that list to another list containing all items.
TTP_Objects.append(flag)
TTP_Objects.append("n")
TTP_Objects.append(n)
TTP_ListOfObjects.append(list(TTP_Objects))

print("\nGenerate RSA modulus n=pq")
print("n =",n, "=",p,"*",q,"")



# TTP chooses real number "a", and makes it public.
a = random.randint(4, 10)
#a = 1
print("\nTTP Chooses real number a =",a)



# Add variable a to the lists, for the CSV file.
TTP_Objects[0] = flag
TTP_Objects[1] = "a"
TTP_Objects[2] = a
TTP_ListOfObjects.append(list(TTP_Objects))

# Create Dataframe, and save as CSV.
print("\n\nMake RSA n value, and a value public.")
TTP_Dataframe = pd.DataFrame(TTP_ListOfObjects, columns=["flag", "Variable", "VariableData"])
TTP_Dataframe.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/TTP.csv',  index=False)  #header=False,



# Register Person A's Private Key

# Continually open Person A's Private Key file, and check whether flag has been changed.
print("\n\nLoading Person A's Private Key...")
print("(Please run the Person A script in another console.)")
variablesUpdated = False
while variablesUpdated == False:

    # Read Person A's Public Key file
    personA_PrivateKey = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/A_PrivateKey.csv")
    
    # Check whether flag has been updated.
    for i in range(len(personA_PrivateKey)):
        if personA_PrivateKey.flag[i] == 1:
            variablesUpdated = True
    time.sleep(0.5)

print("\nPerson A's Data Loaded")

# Retrieve person A's public key.
for i in range(len(personA_PrivateKey)):
    if personA_PrivateKey.Variable[i] == "personAPrivateKey":
        TTP_A_SecretKey = personA_PrivateKey.VariableData[i]





# Register Person B's private keys
print("\n\nLoading Person B's Data...")
print("(Please run the Person B script in another console.)")
variablesUpdated = False
while variablesUpdated == False:

    # Read Person B's Public Key file
    personB_PrivateKey = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/B_PrivateKey.csv")
    
    # Check whether flag has been updated.
    for i in range(len(personB_PrivateKey)):
        if personB_PrivateKey.flag[i] == 1:
            variablesUpdated = True
    time.sleep(0.5)

print("\nPerson B's Data Loaded")


# Retrieve person B's public key.
for i in range(len(personB_PrivateKey)):
    if personB_PrivateKey.Variable[i] == "personBPrivateKey":
        TTP_B_SecretKey = personB_PrivateKey.VariableData[i]


print("\n\nRegister Person A's and Person B's private keys")
print("A Secret Key:", TTP_A_SecretKey)
print("B Secret Key:", TTP_B_SecretKey)

