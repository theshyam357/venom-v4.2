from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Set the encryption key (must be the same as used for encryption)
encryption_key = "Join - @creativeydv Channel ON TG".encode('utf-8')[:16]

# Read the content of the encrypted file
file_to_decrypt = 'upgrade.py.enc'
with open(file_to_decrypt, 'rb') as f_enc:
    encrypted_data_base64 = f_enc.read()

# Base64 decode the encrypted data
encrypted_data = base64.b64decode(encrypted_data_base64)

# Create the AES cipher in ECB mode
cipher = AES.new(encryption_key, AES.MODE_ECB)

# Decrypt the data (make sure to unpad after decryption)
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

# Save the decrypted content to a file named 'upgrade.py'
with open('upgrade.py', 'wb') as f_dec:
    f_dec.write(decrypted_data)

print(f"File '{file_to_decrypt}' has been decrypted and saved as 'upgrade.py'.")
