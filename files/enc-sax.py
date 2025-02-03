import base64
import os
import hashlib
from colorama import init, Fore, Style
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Inisialisasi colorama untuk pewarnaan teks
init(autoreset=True)

def clear_screen():
    # Membersihkan layar sesuai dengan OS
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.RED + Style.BRIGHT + """
▓█████  ███▄    █  ▄████▄    ██████  ▄▄▄      ▒██   ██▒
▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▒██    ▒ ▒████▄    ▒▒ █ █ ▒░
▒███   ▓██  ▀█ ██▒▒▓█    ▄ ░ ▓██▄   ▒██  ▀█▄  ░░  █   ░
▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒  ▒   ██▒░██▄▄▄▄██  ░ █ █ ▒ 
░▒████▒▒██░   ▓██░▒ ▓███▀ ░▒██████▒▒ ▓█   ▓██▒▒██▒ ▒██▒
░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░▒▒ ░ ░▓ ░
 ░ ░  ░░ ░░   ░ ▒░  ░  ▒   ░ ░▒  ░ ░  ▒   ▒▒ ░░░   ░▒ ░
   ░      ░   ░ ░ ░        ░  ░  ░    ░   ▒    ░    ░  
   ░  ░         ░ ░ ░            ░        ░  ░ ░    ░  
                  ░                                    
""" + Fore.YELLOW + """
 MY CHANNEL : https://whatsapp.com/channel/0029VaZLpqf8aKvHckUi4f1z
 DEVELOPER  : tiktok.com/@anakkecil_s
""" + Style.RESET_ALL)

def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    return base64.b64encode(iv + ct_bytes).decode('utf-8')

def encrypt_py_file(input_file, key):
    try:
        # Membaca file .py sebagai byte
        with open(input_file, 'r') as f:
            code = f.read().encode()

        encrypted_code = aes_encrypt(code, key)
        encrypted_code_with_text = f"saxtya_{encrypted_code}_eternals"

        # Membuat file keluaran
        output_file = os.path.splitext(input_file)[0] + '_saxtya_enc.py'

        with open(output_file, 'w') as f:
            f.write('# This file has been encrypted using AES and base64 by saxtya\n\n')
            f.write(f'encrypted_code = "{encrypted_code_with_text}"\n')
            f.write(f'key = bytes.fromhex("{key.hex()}")\n\n')
            f.write("""
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def aes_decrypt(data, key):
    data = base64.b64decode(data.replace("saxtya_", "").replace("_eternals", ""))
    iv = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted

# Decrypt and execute the Python code
decrypted_code = aes_decrypt(encrypted_code, key)
exec(decrypted_code.decode('utf-8'))
""")
        print(Fore.GREEN + f'File {input_file} telah dienkripsi menjadi {output_file}')
    except Exception as e:
        print(Fore.RED + f'Gagal mengenkripsi file: {e}')

def main():
    clear_screen()
    banner()
    print(' ')
    input_file = input(Fore.YELLOW + 'MASUKKAN FILE YANG INGIN DIENKRIPSI: ' + Style.RESET_ALL)
    password = input(Fore.YELLOW + 'MASUKKAN PASSWORD FILE: ' + Style.RESET_ALL)
    
    # Membuat kunci enkripsi dari password
    key = hashlib.sha256(password.encode()).digest()
    encrypt_py_file(input_file, key)

if __name__ == "__main__":
    main()
