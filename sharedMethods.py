# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""

import time
import random
import pandas as pd

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

# Use the given parameters, to read a data frame.
def readFile(filePath, flag):
    variablesUpdated = False
    # Open the file, and check whether the flag has been changed. If it has, continue on.
    while variablesUpdated == False:
    
        # Read the TTP file.
        dataFile = pd.read_csv(filePath)
        # Check whether flag has been updated.
        for i in range(len(dataFile)):
            if dataFile.flag[i] == flag:
                variablesUpdated = True
                
        # Use a random number, so that the two people do not use this method at the same time.
        time.sleep(random.randint(1,3))
    # Return the dataFile that has been opened, back to the main script.
    return dataFile

# Print out the final verdict of the Proof.
def finalVerdict(currentRoundSuccessful):
    if currentRoundSuccessful == False:
        print("Proof has failed.")
        print("Person A has failed to prove their secret.") 
    else:
        print("Proof has succeeded.")
        print("Person A has successfully proved knowledge of the secret.")
