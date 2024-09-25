import streamlit as st

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

st.header("Encryption")
ptext = st.text_input("Enter the Plaintext", "")
key = st.text_input("Enter Shift Key Value (0-99)", "")

if st.button("Encrypt"):
    if ptext and key:
        try:
            key = int(key)
            if 0 <= key <= 99:
                ciphertext = encrypt(ptext, key)
                st.success(f"Cipher Text: {ciphertext}")
            else:
                st.error("Key must be between 0 and 99.")
        except ValueError:
            st.error("Please enter a valid integer for the key.")
    else:
        st.error("Please enter both text & key.")

st.header("Decryption")
ctext = st.text_input("Enter the Ciphertext", "")
dkey = st.text_input("Enter Shift Key Value (0-99)", "")

if st.button("Decrypt"):
    if ctext and dkey:
        try:
            keyd = int(dkey)
            if 0 <= dkey <= 99:
                plaintext = decrypt(ctext, keyd)
                st.success(f"Plain Text: {plaintext}")
            else:
                st.error("Key must be between 0 and 99.")
        except ValueError:
            st.error("Please enter a valid integer for the key.")
    else:
        st.error("Please enter both ciphertext & key.")
