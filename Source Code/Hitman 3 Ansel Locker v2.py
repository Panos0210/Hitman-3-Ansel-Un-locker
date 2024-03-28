import os

changes = [
    {'old_hex': b'\x83\xF8\x0F\xEB\x1C\x0F\x54', 'new_hex': b'\x83\xF8\x0F\x75\x1C\x0F\x54'},
    # Add more entries as needed
]

def find_hitman3_exe():
    drives = ['C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:']

    for drive in drives:
        for root, dirs, files in os.walk(drive):
            if 'HITMAN3.exe' in files:
                exe_path = os.path.join(root, 'HITMAN3.exe')
                if os.path.exists(exe_path):
                    return exe_path
    return None

def replace_hex_codes(file_path, changes):
    try:
        with open(file_path, 'rb') as file:
            content = bytearray(file.read())
            
            for change in changes:
                old_hex = change['old_hex']
                new_hex = change['new_hex']
                
                for i in range(len(content) - len(old_hex) + 1):
                    if all(content[i + j] == old_hex[j] for j in range(len(old_hex))):
                        content[i:i + len(old_hex)] = new_hex
            
        with open(file_path, 'wb') as file:
            file.write(content)
            
        print(f"Hex codes replaced successfully in {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_path = find_hitman3_exe()
    if file_path:
        print(f"HITMAN 3 executable found at: {file_path}")
        replace_hex_codes(file_path, changes)
    else:
        print("HITMAN 3 executable not found.")

if __name__ == "__main__":
    main()
