# About the Affine Cipher: Encryption and Decryption

This script is an encrypting/decrypting tool for an Affine cipher. Given a key $k = (\alpha, \beta)$ where $0 \leq \alpha, \beta \leq 25$ (and $\gcd(\alpha, \beta) = 1$), we can encrypt some $x$ (inputted as a character, converted to an integer) via:

$$
E(x) = (\alpha \cdot x + \beta) \mod 26
$$

And decrypt it using:

$$
D(x) = \alpha^{-1} \cdot (x - \beta) \mod 26
$$

Where $\alpha^{-1}$ is the modular inverse of $\alpha\mod 26$.

# Python Script
## Running the Python Script
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the Python script using the following command:
  ~~~
  python affine.py
  ~~~
4. The script will prompt you for an alpha and a beta to function as a key for your cipher.
5. The script will then ask whether you want to encrypt or decrypt a message, with respect to the key.
6. Input either the plaintext or the ciphertext, according to whether you want to encrpyt or decrypt.
