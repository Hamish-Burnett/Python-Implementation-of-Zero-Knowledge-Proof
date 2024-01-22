# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""
# Person A

import time
import pandas as pd
import random
import sharedMethods

global continueProof
continueProof = True

print("Person A")

# Perform Setup, and exchange relevant keys.
print("\n\nSetup Phase:")
# Load Data from Trusted Third Party file.
print("\nLoading Trusted Third Party Data...")
print("(Please run the TTP script in another console.)")
TTP_Data = sharedMethods.readFile("C:/Users/.../TTP.csv", 1)
print("\nTTP Data Loaded")

# Retrieve RSA n value.
for i in range(len(TTP_Data)):
    if TTP_Data.Variable[i] == "n":
        RSA_n = TTP_Data.VariableData[i]
print("\n\nRetrieve TTP RSA n value: ",RSA_n)


# Choose the secrets of person A.
personASecret = 3
print("\n\nGenerate private key:",personASecret)

# Calculate public key for person A
personAPublicKey = pow(personASecret, 2) % RSA_n
print("Generate public key:",personAPublicKey)

# Generate a dataframe for the public and private keys, and generate a CSV file.
flag = 1
A_PublicKey = sharedMethods.createDataFrameWithFlag(flag, "personAPublicKey", personAPublicKey)
A_PublicKey.to_csv('C:/Users/.../A_PublicKey.csv',  index=False)  #header=False,

A_PrivateKey = sharedMethods.createDataFrameWithFlag(flag, "personAPrivateKey", personASecret)
A_PrivateKey.to_csv('C:/Users/.../A_PrivateKey.csv',  index=False)  #header=False,


# Obtain Person B's public key file.
print("\n\nLoading Person B's Data...")
print("(Please run the Person B script in another console.)")
personB_PublicKey = sharedMethods.readFile("C:/Users/.../B_PublicKey.csv", 1)
print("\nPerson B's Data Loaded")

# Retrieve person B's public key.
for i in range(len(personB_PublicKey)):
    if personB_PublicKey.Variable[i] == "personBPublicKey":
        B_PublicKey = personB_PublicKey.VariableData[i]
print("\nRetrieve Person B's public key:",B_PublicKey)



print("\n\nSetup Complete")
print("\n\n\n\nInitiating Challenges to Prove that Person A knows a secret.\n")

# Method to perform process of proof, which is repeated 'a' times. 
def performProof(): 
    global currentRoundSuccessful
    global continueProof
    currentRoundSuccessful = False
    continueProof = True

    flag = 0
    
    # Person A selects committment m, such that m <_ n-1. 
    randNumUpperBound = RSA_n - 1
    m = random.randint(0, randNumUpperBound)
    print("Person A selects committment m, such that m <_ n-1.")
    print("Committment is:",m)
    
    # Person A calculates witness w=m^2 (mod n), and sends to B
    w = pow(m, 2) % RSA_n
    print("\n\nPerson A calculates witness w=m^2 (mod n), and sends to Person B")
    print("Witness:",w)
    
    # Create CSV file containing this information. Flag is used to indicate the current stage of the proof.
    flag = 1
    A_Handshake = sharedMethods.createDataFrameWithFlag(flag, "witness", w)
    A_Handshake.to_csv('C:/Users/.../Handshake.csv',  index=False)  #header=False,
    
    
    print("\n\nLoading Person B's Reply...")
    Handshake = sharedMethods.readFile("C:/Users/.../Handshake.csv", 2) 
    BChallenge = -1

    for i in range(len(Handshake)):           
        if Handshake.Variable[i] == "challenge":
            BChallenge = Handshake.VariableData[i]
    print("Person B's Reply Loaded")
    print("\nRetrieve challenge from person B:",BChallenge)
    
    
    # Respond to Challenge - Person A calculates response r = m*personAPublicKey^c (mod n)
    r = pow(personASecret, BChallenge)
    r = (m * r) % RSA_n
    
    # Create CSV with the reply to Person B.
    flag = 3
    A_Handshake = sharedMethods.createDataFrameWithFlag(flag, "response", r)
    A_Handshake.to_csv('C:/Users/.../Handshake.csv',  index=False)  #header=False,
    
    print("\n\nRespond to challenge, by calculating r = m*personAPublicKey^c (mod n)")
    print("Response:",r)
    print("Send to Person B")
    
    # Outcome of whether the proof was successful.
    print("\n\nLoading Person B's Reply...")
    variablesUpdated = False
    currentRoundSuccessful = False
    continueProof = True
    
    Handshake = sharedMethods.readFile("C:/Users/.../Handshake.csv", 4)
    for i in range(len(Handshake)):
        # Retrieve the data about the success of the current round, and then retrieve data about whether to repeat the process.
        if Handshake.Variable[i] == "validityOfResponse":  
            currentRoundSuccessful = Handshake.VariableData[i]
        elif Handshake.Variable[i] == "continueProof":
            continueProof = Handshake.VariableData[i]
    
    # Check if the Proving Process needs to be repeated.
    print("Person B's Reply Loaded")
    if continueProof == True:
        print("\nCurrent Round Passed")
        print("Proceed to Next Round")

# Repeat the process of proving knowledge of success, while continueProof is set to True.
i = 1
while continueProof == True:
    print("********Round",i,"********") 
    performProof()
    i += 1
    print("\n\n\n\n")
   
# Print final verdict about the success of the proof.
sharedMethods.finalVerdict(currentRoundSuccessful)