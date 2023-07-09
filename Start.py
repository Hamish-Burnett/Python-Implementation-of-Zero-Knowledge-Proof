# -*- coding: utf-8 -*-
"""
@author: Hamish Burnett
"""
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




# Create an empty file for all files. Empty files are used to overwrite previous files,
# to ensure that the program uses current variables, that have been generated in this
# instance of running the program.
flag = 0
A_Handshake = createDataFrameWithFlag(flag, "", "")
A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/A_PrivateKey.csv',  index=False)  #header=False,
A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/A_PublicKey.csv',  index=False)  #header=False,
A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/B_PrivateKey.csv',  index=False)  #header=False,
A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/B_PublicKey.csv',  index=False)  #header=False,
A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/Handshake.csv',  index=False)  #header=False,
A_Handshake.to_csv('C:/Users/Burnett_Hamish/OneDrive - Department of Education and Training/Documents/Deakin_University/Projects/ZeroKnowknowledgeProtocol-CSV/TTP.csv',  index=False)  #header=False,


print("Empty Files Generated")
print("Please Launch PersonA.py, PersonB.py, or TrustedThirdParty.py")