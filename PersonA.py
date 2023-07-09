# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""

# Person A

import time
import pandas as pd
import random


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



print("Person A")

print("\n\nSetup Phase:")



# Load Data from Trusted Third Party file.
print("\nLoading Trusted Third Party Data...")
print("(Please run the TTP script in another console.)")
variablesUpdated = False

# Open the TTP_Data file, and check whether the flag has been changed. If it has, continue on.
while variablesUpdated == False:

    # Read the TTP file.
    TTP_Data = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/TTP.csv")
    
    # Check whether flag has been updated.
    for i in range(len(TTP_Data)):
        if TTP_Data.flag[i] == 1:
            variablesUpdated = True
    time.sleep(2)

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
A_PublicKey = createDataFrameWithFlag(flag, "personAPublicKey", personAPublicKey)
A_PublicKey.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/A_PublicKey.csv',  index=False)  #header=False,

A_PrivateKey = createDataFrameWithFlag(flag, "personAPrivateKey", personASecret)
A_PrivateKey.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/A_PrivateKey.csv',  index=False)  #header=False,






# Obtain Person B's public key file.
print("\n\nLoading Person B's Data...")
print("(Please run the Person B script in another console.)")
variablesUpdated = False

# Check whether flag has been updated, indicating that new data is present.
while variablesUpdated == False:

    # Read Person B's Public Key file
    personB_PublicKey = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/B_PublicKey.csv")
    
    # Check whether flag has been updated.
    for i in range(len(personB_PublicKey)):
        if personB_PublicKey.flag[i] == 1:
            variablesUpdated = True
    time.sleep(2)
    
print("\nPerson B's Data Loaded")




# Retrieve person B's public key.
for i in range(len(personB_PublicKey)):
    if personB_PublicKey.Variable[i] == "personBPublicKey":
        B_PublicKey = personB_PublicKey.VariableData[i]

print("\nRetrieve Person B's public key:",B_PublicKey)

print("\n\nSetup Complete")

print("\n\n\n\nInitiating Challenges to Prove that Person A knows a secret.\n")


global currentRoundSuccessful
global continueProof
currentRoundSuccessful = False
continueProof = True
    
# Method to perform process of proof, which is repeated 'a' times. 
def performProof():    
    flag = 0
    
    # Person A selects committment m, such that m <_ n-1. 
    randNumUpperBound = RSA_n - 1
    m = random.randint(0, randNumUpperBound)
    
    # You can manually choose a number to be m, by commenting out the line above, and using the following line.
    # m = xyz
    
    print("Person A selects committment m, such that m <_ n-1.")
    print("Committment is:",m)
    
    # Person A calculates witness w=m^2 (mod n), and sends to B
    w = pow(m, 2) % RSA_n
    print("\n\nPerson A calculates witness w=m^2 (mod n), and sends to Person B")
    print("Witness:",w)
    
    # Create CSV file containing this information. Flag is used to indicate the current stage of the proof.
    flag += 1
    A_Handshake = createDataFrameWithFlag(flag, "witness", w)
    A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
    
    
    
    # Wait for Person's B Reply.
    print("\n\nLoading Person B's Reply...")
    variablesUpdated = False
    
    while variablesUpdated == False:
    
        # Obtain Challenge CSV file from person B
        Handshake = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv")
        
        # Retrieve RSA n value.
        for i in range(len(Handshake)):
            if Handshake.flag[i] == 2:
                flag = 2
                variablesUpdated = True
    
                if Handshake.Variable[i] == "challenge":
                    BChallenge = Handshake.VariableData[i]
        
        time.sleep(2)
    
    print("Person B's Reply Loaded")
    print("\nRetrieve challenge from person B:",BChallenge)
    
    
    
    
    # Respond to Challenge - Person A calculates response r = m*personAPublicKey^c (mod n)
    r = pow(personASecret, BChallenge)
    r = (m * r) % RSA_n
    
    # Create CSV with the reply to Person B.
    flag += 1
    A_Handshake = createDataFrameWithFlag(flag, "response", r)
    A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
    
    print("\n\nRespond to challenge, by calculating r = m*personAPublicKey^c (mod n)")
    print("Response:",r)
    print("Send to Person B")
    
    print("\n\nLoading Person B's Reply...")
    
    # Outcome of whether the proof was successful.
    global currentRoundSuccessful
    global continueProof
    
    
    variablesUpdated = False
    currentRoundSuccessful = False
    continueProof = True
    
    
    while variablesUpdated == False:
    
        # Obtain Subsequent data from person B
        Handshake = pd.read_csv("C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv")
        
        # Retrieve values that indicate the success of the proof.
        for i in range(len(Handshake)):
            if Handshake.flag[i] == 4:
                flag = 4
                variablesUpdated = True
                
                # Retrieve the data about the success of the current round, and then retrieve data about whether to repeat the process.
                if Handshake.Variable[i] == "validityOfResponse":  
                    currentRoundSuccessful = Handshake.VariableData[i]
                elif Handshake.Variable[i] == "continueProof":
                    continueProof = Handshake.VariableData[i]
                    
        time.sleep(2)
    
    print("Person B's Reply Loaded")
    
    
    # Check if the Proving Process needs to be repeated.
    if continueProof == True:
        print("\nCurrent Round Passed")
        print("Proceed to Next Round")
    
    
  
    
  
    
  
    
  
    
  
    
  
    
i = 1

# Repeat the process of proving knowledge of success, while continueProof is set to True.
while continueProof == True:
    print("********Round",i,"********") 
    performProof()
    i += 1
    print("\n\n\n\n")
   
    
# Print final verdict about the success of the proof.
print("\n\n")
if currentRoundSuccessful == False:
    print("Proof has failed.")
    print("Person A has failed to prove their secret.")
else:
    print("Proof has succeeded.")
    print("Person A has successfully proved knowledge of the secret.")
