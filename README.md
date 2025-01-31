# Affine Encryption and Decryption

This is an encrypting/decrypting tool for an Affine cipher. Given a key $ k = (\alpha, \beta) $ where $0 \leq \alpha, \beta \leq 25$ (and $gcd(\alpha, \beta) = 1$), we can encrypt some $x$ (inputted as a character, converted to an integer) via:

$$
E(x) = (\alpha \cdot x + \beta) \mod 26
$$

And decrypt it using:

$$
D(x) = \alpha^{-1} \cdot (x - \beta) \mod 26
$$

Where $ \alpha^{-1} $ is the modular inverse of $ \alpha $ modulo 26.
