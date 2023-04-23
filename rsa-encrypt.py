from math import gcd
from random import randint

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise Exception("Modular inverse does not exist.")
    else:
        return x % m

def encrypt_rsa(msg, n, e):
    if msg >= n:
        raise Exception("Message is too long for given public key.")
    return pow(msg, e, n)

# Example usage
n = 100356462393939275644261801235739258555903120510260117079532748046044777580556913666624385067860362189781953950167049236111624596754601584109126376567789749359110634033347771862045265201572066441103522259868053467404680636244434366256141873753956814936707101176251008812547487386794859987129642755321245550877
e = 65537
msg = 123456789
ciphertext = encrypt_rsa(msg, n, e)
print(ciphertext)
