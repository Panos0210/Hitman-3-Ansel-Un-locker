changes = [
    {'old_hex': b'\x83\xF8\x0F\x75\x1C\x0F\x54', 'new_hex': b'\x83\xF8\x0F\xEB\x1C\x0F\x54'},
    # Add more entries as needed
]

file_path = r'C:\Program Files (x86)\Steam\steamapps\common\HITMAN 3\Retail\HITMAN3.exe'

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

replace_hex_codes(file_path, changes)
