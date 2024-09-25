import streamlit as st

# Define the encryption function
def encrypt(ptext, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    cipher = ''
    for char in ptext:
        if char in letters:
            i = (letters.index(char) + key) % len(letters)
            cipher += letters[i]
        else:
            cipher += char
    return cipher

# Define the decryption function
def decrypt(ctext, key):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    for char in ctext:
        if char in letters:
            i = (letters.index(char) - key) % len(letters)
            plaintext += letters[i]
        else:
            plaintext += char
    return plaintext

# ---- Streamlit Application ---
st.title("Caesar Cipher")

# Encryption section
st.header("Encryption")
ptext = st.text_input("Enter the Plaintext", "", key="encrypt_text")
key = st.text_input("Enter Shift Key Value (0-255)", "", key="encrypt_key")

if st.button("Encrypt"):
    if ptext and key:
        try:
            key = int(key)
            if 0 <= key <= 255:
                ciphertext = encrypt(ptext, key)
                st.success(f"Cipher Text: {ciphertext}")
            else:
                st.error("Key must be between 0 and 255.")
        except ValueError:
            st.error("Please enter a valid integer for the key.")
    else:
        st.error("Please enter both text & key.")

# Decryption section
st.header("Decryption")
ctext = st.text_input("Enter the Ciphertext", "", key="decrypt_text")
dkey = st.text_input("Enter Shift Key Value (0-255)", "", key="decrypt_key")

if st.button("Decrypt"):
    if ctext and dkey:
        try:
            dkey = int(dkey)  # Convert to integer
            if 0 <= dkey <= 255:
                plaintext = decrypt(ctext, dkey)
                st.success(f"Plain Text: {plaintext}")
            else:
                st.error("Key must be between 0 and 255.")
        except ValueError:
            st.error("Please enter a valid integer for the key.")
    else:
        st.error("Please enter both ciphertext & key.")
