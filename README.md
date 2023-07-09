# Python-Implementation-of-Zero-Knowledge-Proof
Several scripts have been developed to implement a demonstration of a Zero Knowledge Proof (ZKP), using the Feige-Fiat-Shamir Identifcation Protocol.

The implementation provided is a simplified version of the Feige-Fiat-Shamir Identification Protocol. This protocol is used to prove that Person A is who they say they are, without revealing any information about Person A.

The protocol consists of three parties, being the Trusted Third Party, Person A, and Person B.

The Trusted Third Party decides on the key details for how to perform the proof. The Trusted Third Party is independent of both the prover (person convincing the other person of their identity, or knowledge of a secret), and the verifier (person who is verifying that Person A is who they say they are, or knows a particular secret).

Person A (prover) wishes to prove their identity, or knowledge of a secret, without revealing any information. This could be achieved through providing small bits of information from an ID card provided by the Trusted Third Party. The bits of information will be able to prove that Person A is who they say they are, but the verifier (Person B), will not be able to obtain any information about the ID card, such as the card number.

Person B (verifier) verifies that Person A is who they say they are. The verifier checks the answers that Person A provides, and can determine whether Person A is genuinly Person A, or in the event of Person A proving knowledge of a Secret, that Person A knows a secret.

Although this is an Identification Protocol, this implementation is used to prove that Person A knows a Secret, and wishes to prove to Person B their knowledge of the Secret, without revealing what the Secret is.


Specifics about the Program:
This program was developed using Anaconda, and in the Spyder application, running Python 3.9. You may need to install several libraries, being the time, pandas, and random libraries.

There are four (4) scripts:
  Start.py: Run this program first.
  TrustedThirdParty.py: Performs the operation of the Trusted Third Party.
  PersonA.py: Runs the program of the prover.
  PersonB.py: Runs the program of the verifier.

The scripts need to be run in different consoles at the same time. The individual scripts communicate with each other through CSV files. When data is ready to be transferred to another script, a CSV file is made, containing the data. Other approaches were considered, such as using Environment variables, and Importing the variables from within the code. These approaches were not successful, and so the CSV approach was used.

There are two main sections in the Prover and Verifier scripts, being the Setup phase, and the Proving phase, which is a series of Handshakes that contain small amounts of the data. In the Setup phase, the RSA public and private keys (private key is the Secret in this implementation) remain the same, but the variables that are used in the Proving phase are random.

The inspiration to complete this project came from studying a unit of Cryptography. During the course of the unit, there was a small section in the textbook on Zero Knowledge Proofs. The Cryptography unit was largly focused on understanding the maths behind cryptography, and so this topic was largly not covered. I found this topic interesting, and after completing the unit, I decided to create a simple implementation of a Zero Knowledge Proof for fun, to see both how it works, and the process of proving something, without revealing any information about the thing to be proved.


********Warning********
This program is for educational purposes only. This implementation should not be used in real applications, and is just for education/demonstration, as it is insecure.

References: 

Applied Cryptography: Protocols, Algorithms and Source Code in C, 20th Anniversary Edition - Bruce Schneier
https://learning.oreilly.com/library/view/applied-cryptography-protocols/9781119096726/31_chap21.html#chap21

An Introduction to Cryptography, by Richard A. Mollin.
