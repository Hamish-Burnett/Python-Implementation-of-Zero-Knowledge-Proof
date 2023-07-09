# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""


# Person B

import time
import pandas as pd
import random

print("Person B")

print("\n\nSetup Phase:")


print("\nLoading Trusted Third Party Data...")
print("(Please run the TTP script in another console.)")

# Obtain TTP Data from CSV file.
variablesUpdated = False
while variablesUpdated == False:

    # Read the TTP file.
    TTP_Data = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/TTP.csv")
    
    # Check whether flag has been updated, which indicates that content has been updated.
    for i in range(len(TTP_Data)):
        if TTP_Data.flag[i] == 1:
            variablesUpdated = True
    time.sleep(3)

print("\nTTP Data Loaded")

# Retrieve RSA n value and a value.
global TTP_A
for i in range(len(TTP_Data)):
    if TTP_Data.Variable[i] == "n":
        RSA_n = TTP_Data.VariableData[i]
    elif TTP_Data.Variable[i] == "a":
        TTP_A = TTP_Data.VariableData[i]

print("\n\nRetrieve TTP RSA n value: ",RSA_n)
print("Retrieve TTP 'a' value:",TTP_A)

# Choose the secrets of person B.
personBSecret = 7
print("\n\nGenerate private key:",personBSecret)


# Calculate public key for each person
personBPublicKey = pow(personBSecret, 2) % RSA_n
print("Generate public key:",personBPublicKey)


# Use the given parameters to create a data frame.
def createDataFrameWithFlag(flag, dataName, dataContents):
    A_Information = []
    A_Information.append(flag)
    A_Information.append(dataName)
    A_Information.append(dataContents)

    # Create Dataframe, and save as CSV.
    A_Key = pd.DataFrame(A_Information, index=["flag", "Variable", "VariableData"])
    A_Key = A_Key.T    
    return A_Key

flag = 1

# Generate a dataframe for the public and private keys, and generate a CSV file.
B_PublicKey = createDataFrameWithFlag(flag, "personBPublicKey", personBPublicKey)
B_PublicKey.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/B_PublicKey.csv',  index=False)  #header=False,

B_PrivateKey = createDataFrameWithFlag(flag, "personBPrivateKey", personBSecret)
B_PrivateKey.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/B_PrivateKey.csv',  index=False)  #header=False,













# Obtain Person A's public key.
print("\n\nLoading Person A's Data...")
print("(Please run the Person A script in another console.)")
variablesUpdated = False
while variablesUpdated == False:

    # Read Person A's Public Key file
    personA_PublicKey = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/A_PublicKey.csv")
    
    # Check whether flag has been updated, indicating that content has been updated.
    for i in range(len(personA_PublicKey)):
        if personA_PublicKey.flag[i] == 1:
            variablesUpdated = True
    time.sleep(2)
    
print("\nPerson A's Data Loaded")


# Retrieve person A's public key.
for i in range(len(personA_PublicKey)):
    if personA_PublicKey.Variable[i] == "personAPublicKey":
        A_PublicKey = personA_PublicKey.VariableData[i]

print("\n\nRetrieve Person A's public key:",A_PublicKey)

print("\n\nSetup Complete")



print("\n\n\n\nInitiating Challenges to Prove that Person A knows a secret.\n")

global currentRoundSuccessful
global continueProof
currentRoundSuccess = False
continueProof = True
    
# Method to perform process of proof, which is repeated 'a' times. 
def performProof():
    flag = 0
   
    # Obtain Person A's witness from CSV file.
    print("Load Person A's Initial Proof Data...")
    variablesUpdated = False
    AWitness = -1
    while variablesUpdated == False:    
        # Take the empty file, and update the flag when data is added. 
        # Then check in this script for an updated flag, and use the corrosponding updated data.
        Handshake = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv")
            
        # Retrieve person A's witness value.
        for i in range(len(Handshake)):
            if Handshake.flag[i] == 1:
                variablesUpdated = True
                flag = Handshake.flag[i]
                if Handshake.Variable[i] == "witness":
                    AWitness = Handshake.VariableData[i]
        time.sleep(3)
                
    print("Person A's Data loaded")
    print("Retrieve Person A's witness:",AWitness)
    
    
    
    # Choose random challenge c, and generate CSV file.
    challenge = random.randint(0, 1)
    # Commment out the above line, and use the following line, to provide a single challenge.
    #challenge = 0
    
    flag += 1
    Handshake = createDataFrameWithFlag(flag, "challenge", challenge)
    Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
    print("\n\nChoose challenge, as a random number being either 0 or 1.")
    print("Challenge is:",challenge)
    print("Send to Person A")
    
    
    
    print("\n\nLoading Person A's Reply...")
    # Obtain Response from Person A
    variablesUpdated = False
    AResponse = -1
    while variablesUpdated == False:  
        Handshake = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv")
    
        # Retrieve person A's witness value.
        for i in range(len(Handshake)):
            if Handshake.flag[i] != flag:
                flag = Handshake.flag[i]
                variablesUpdated = True
                if Handshake.Variable[i] == "response":
                    AResponse = Handshake.VariableData[i]
        time.sleep(3)
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
    
    
    global currentRoundSuccess
    global continueProof
    
    currentRoundSuccess = False
    #successfulProof = False
    continueProof = True
    flag += 1
    
    # Perform comparison, and provide variables to determine the next stage of the proof,
    # being to either repeat the process of the proof, or ending the Proof process, and 
    # providing an answer as to whether Person A was successful at proving their secret.
    if calculateResponse == verifyNumber:
        currentRoundSuccess = True
        global TTP_A
        TTP_A -= 1
        
        # Repeat the proof process
        if TTP_A > 0:
            print("\n\nCalculated response matches verifyNumber. Current round passed.")
            print("Minus 1 from TTP_A, Repeat Process")
            continueProof = True
            Handshake = createDataFrameWithFlag(flag, "validityOfResponse", currentRoundSuccess)
            listOfSuccessfulProof = [flag, "continueProof", continueProof]
            Handshake.loc[len(Handshake)] = listOfSuccessfulProof    
            Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
        
        # End the proof process, with Person A successfully proving their secret.
        else:
            print("\n\nCurrent round passed.")
            print("Proceed to end.")
            currentRoundSuccess = True
            continueProof = False
            Handshake = createDataFrameWithFlag(flag, "validityOfResponse", currentRoundSuccess)
            listOfSuccessfulProof = [flag, "continueProof", continueProof]
            Handshake.loc[len(Handshake)] = listOfSuccessfulProof
            Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
    
    # Or end the proof process with Person A being unsuccessful at proving knowledge of the secret.
    else:
        print("\n\nCurrent round failed.")
        print("Proceed to end.")
        continueProof = False
        Handshake = createDataFrameWithFlag(flag, "validityOfResponse", currentRoundSuccess)
        listOfSuccessfulProof = [flag, "continueProof", continueProof]
        
        Handshake.loc[len(Handshake)] = listOfSuccessfulProof
        Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
    


i = 1

# Repeat the proof process while the variable continueProof is True.
while continueProof == True:
    print("\n\n********Round",i,"********") 
    performProof()      # TTP_A
    i += 1
    print("\n\n\n\n")
   
    
# Print out the final verdict of the Proof.
if currentRoundSuccess == False:
    print("Proof has failed.")
    print("Person A has failed to prove their secret.") 
else:
    print("Proof has succeeded.")
    print("Person A has successfully proved knowledge of the secret.")
