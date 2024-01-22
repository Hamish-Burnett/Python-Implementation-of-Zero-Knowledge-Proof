# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""
# Person B

import time
import pandas as pd
import random
import sharedMethods

global continueProof
continueProof = True

print("Person B")

# Perform Setup, and exchange relevant keys.
print("\n\nSetup Phase:")

print("\nLoading Trusted Third Party Data...")
print("(Please run the TTP script in another console.)")
# Obtain TTP Data from CSV file.
TTP_Data = sharedMethods.readFile("C:/Users/.../TTP.csv", 1)
print("\nTTP Data Loaded")

# Retrieve RSA n value and a value.
for i in range(len(TTP_Data)):
    if TTP_Data.Variable[i] == "n":
        RSA_n = TTP_Data.VariableData[i]
    elif TTP_Data.Variable[i] == "a":
        TTP_A = TTP_Data.VariableData[i]
        
print("\n\nRetrieve TTP RSA n value: ",RSA_n)
print("Retrieve TTP 'a' value (Number of times to perform the proof):",TTP_A)

# Choose the secrets of person B.
personBSecret = 7
print("\n\nGenerate private key:",personBSecret)

# Calculate public key for each person
personBPublicKey = pow(personBSecret, 2) % RSA_n
print("Generate public key:",personBPublicKey)


flag = 1
# Generate a dataframe for the public and private keys, and generate a CSV file.
B_PublicKey = sharedMethods.createDataFrameWithFlag(flag, "personBPublicKey", personBPublicKey)
B_PublicKey.to_csv('C:/Users/.../B_PublicKey.csv',  index=False)  #header=False,

B_PrivateKey = sharedMethods.createDataFrameWithFlag(flag, "personBPrivateKey", personBSecret)
B_PrivateKey.to_csv('C:/Users/.../B_PrivateKey.csv',  index=False)  #header=False,


# Obtain  file containing Person A's public key.
print("\n\nLoading Person A's Data...")
print("(Please run the Person A script in another console.)")
personA_PublicKey = sharedMethods.readFile("C:/Users/.../A_PublicKey.csv", 1)
print("\nPerson A's Data Loaded")

# Retrieve Person A's public key.
for i in range(len(personA_PublicKey)):
    if personA_PublicKey.Variable[i] == "personAPublicKey":
        A_PublicKey = personA_PublicKey.VariableData[i]
print("\n\nRetrieve Person A's public key:",A_PublicKey)

print("\n\nSetup Complete")
print("\n\n\n\nInitiating Challenges to Prove that Person A knows a secret.\n")

# Method to perform process of proof, which is repeated 'a' times. 
def performProof(): 
    global currentRoundSuccessful
    currentRoundSuccessful = False
    
    global continueProof
    continueProof = True
    
    flag = 0
    # Obtain Person A's witness from CSV file.
    print("Load Person A's Initial Proof Data...")
    variablesUpdated = False
    AWitness = -1
    Handshake = sharedMethods.readFile("C:/Users/.../Handshake.csv", 1)

    for i in range(len(Handshake)):
        if Handshake.Variable[i] == "witness":
            AWitness = Handshake.VariableData[i]
    print("Person A's Data loaded")
    print("Retrieve Person A's witness:",AWitness)
    
    
    # Choose random challenge c, and generate CSV file.
    challenge = random.randint(0, 1)  
    flag = 2
    Handshake = sharedMethods.createDataFrameWithFlag(flag, "challenge", challenge)
    Handshake.to_csv('C:/Users/.../Handshake.csv',  index=False)  #header=False,
    print("\n\nChoose challenge, as a random number being either 0 or 1.")
    print("Challenge is:",challenge)
    print("Send to Person A")
    
    # Obtain Response from Person A
    print("\n\nLoading Person A's Reply...")
    variablesUpdated = False
    AResponse = -1
    Handshake = sharedMethods.readFile("C:/Users/.../Handshake.csv", 3)
     
    for i in range(len(Handshake)):
        if Handshake.Variable[i] == "response":
            AResponse = Handshake.VariableData[i]
    print("\n\nRetrieve Reply from Person A:",AResponse)
    
    
    # Confirm AResponse is correct
    # Calculating AResponse^2 mod n, and compare against AWitness*APublicKey^challenge (mod n)
    calculateResponse = pow(AResponse, 2) % RSA_n
    verifyNumber = pow(A_PublicKey, challenge)
    verifyNumber = (AWitness * verifyNumber) % RSA_n
    print("\n\nConfirm that AResponse is correct.")
    print("Calculate calculateResponse = AResponse^2 mod n, and compare against verifyNumber = AWitness*APublicKey^challenge (mod n)")
    print("\ncalculateResponse:verifyNumber")
    print(calculateResponse, ":", verifyNumber)
    
    currentRoundSuccessful = False
    continueProof = True
    flag = 4
    # Perform comparison, and provide variables to determine the next stage of the proof,
    # being to either repeat the process of the proof, or ending the Proof process, and 
    # providing an answer as to whether Person A was successful at proving their secret.
    if calculateResponse == verifyNumber:
        currentRoundSuccessful = True
        global TTP_A
        TTP_A -= 1
        
        # Repeat the proof process
        if TTP_A > 0:
            print("\n\nCalculated response matches verifyNumber. Current round passed.")
            print("Minus 1 from TTP_A, Repeat Process")
            continueProof = True
            Handshake = sharedMethods.createDataFrameWithFlag(flag, "validityOfResponse", currentRoundSuccessful)
            listOfSuccessfulProof = [flag, "continueProof", continueProof]
            Handshake.loc[len(Handshake)] = listOfSuccessfulProof    
            Handshake.to_csv('C:/Users/.../Handshake.csv',  index=False)  #header=False,
            
        # End the proof process, with Person A successfully proving their secret.
        else:
            print("\n\nCurrent round passed.")
            print("Proceed to end.")
            currentRoundSuccessful = True
            continueProof = False
            Handshake = sharedMethods.createDataFrameWithFlag(flag, "validityOfResponse", currentRoundSuccessful)
            listOfSuccessfulProof = [flag, "continueProof", continueProof]
            Handshake.loc[len(Handshake)] = listOfSuccessfulProof
            Handshake.to_csv('C:/Users/.../Handshake.csv',  index=False)  #header=False,
    
    # Or end the proof process with Person A being unsuccessful at proving knowledge of the secret.
    else:
        print("\n\nCurrent round failed.")
        print("Proceed to end.")
        continueProof = False
        Handshake = sharedMethods.createDataFrameWithFlag(flag, "validityOfResponse", currentRoundSuccessful)
        listOfSuccessfulProof = [flag, "continueProof", continueProof]
        
        Handshake.loc[len(Handshake)] = listOfSuccessfulProof
        Handshake.to_csv('C:/Users/.../Handshake.csv',  index=False)  #header=False,
    
# Repeat the proof process while the variable continueProof is True.
i = 1
while continueProof == True:
    print("\n\n********Round",i,"********") 
    performProof()
    i += 1
    print("\n\n\n\n")
   
# Print out the final verdict of the Proof.
sharedMethods.finalVerdict(currentRoundSuccessful)