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

# Streamlit application layout
st.title("Caesar Cipher")

# Get user input for encryption
st.header("Encryption")
ptext = st.text_input("Enter the Plaintext", "")
key = st.text_input("Shift Key", min_value=0, step=1)

if st.button("Encrypt"):
    if ptext and key:
        ciphertext = encrypt(ptext, key)
        st.success(f"Cipher Text: {ciphertext}")
    else:
        st.error("Please enter both text & key.")

# Get user input for decryption
st.header("Decryption")
ctext = st.text_input("Enter the Ciphertext", "")
dkey = st.text_input("Shift Key for Decryption", min_value=0, step=1, key='decrypt_key')

if st.button("Decrypt"):
    if ctext and dkey:
        plaintext = decrypt(ctext, dkey)
        st.success(f"Plain Text: {plaintext}")
    else:
        st.error("Please enter both ciphertext & key.")
