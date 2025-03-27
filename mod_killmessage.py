import os
import shutil

# Paths
XSuit_file = "/storage/emulated/0/DARK_EFFECT/TXT/all x-suit.txt"
Outfits_file = "/storage/emulated/0/DARK_EFFECT/TXT/outfits.txt"
Original_binary = "/storage/emulated/0/DARK_EFFECT/ORGINAL/0027fc08.uasset"
Modified_folder = "/storage/emulated/0/DARK_EFFECT/MODIFIED/"

# Function to display colorful text using toilet
def display_banner(text):
    os.system(f'toilet -f term -F gay "{text}"')

# Function to load and parse X-Suits or Outfits
def load_items(file_path):
    items = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                name, hex_value = line.split(':', 1)
                items[name.strip()] = hex_value.strip()
    return items

# Function to display items and let the user choose
def choose_item(items, prompt):
    os.system(f'toilet -f term -F gay "{prompt}"')
    for i, name in enumerate(items.keys(), 1):
        print(f"[{i}] {name}")
    choice = int(input("Enter your choice: ")) - 1
    return list(items.keys())[choice], list(items.values())[choice]

# Function to replace hex values in the binary file
def replace_hex_in_file(file_path, old_hex, new_hex):
    with open(file_path, 'rb') as file:
        data = file.read()
    data = data.replace(bytes.fromhex(old_hex), bytes.fromhex(new_hex))
    
    modified_file = os.path.join(Modified_folder, os.path.basename(file_path))
    with open(modified_file, 'wb') as file:
        file.write(data)

    os.system('toilet -f term -F gay "Modification Complete!"')
    print(f"Modified file saved to: {modified_file}")

# Main menu
def main_menu():
    os.system('clear')
    os.system('toilet -f term -F border --gay "   𝗞𝗜𝗟𝗟 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 𝗧𝗢𝗢𝗟 " | pv -qL 9500')
    os.system('toilet -f term -F gay "𝟭] 𝗠𝗢𝗗 𝗞𝗜𝗟𝗟 𝗠𝗘𝗦𝗦𝗔𝗚𝗘"')
    os.system('toilet -f term -F gay "𝟮] 𝗤𝗨𝗜𝗧"')
    return input("𝐄𝐧𝐭𝐞𝐫 𝐲𝐨𝐮𝐫 𝐜𝐡𝐨𝐢𝐜𝐞: ")

# Main function
def main(): 
    while True:
        choice = main_menu()
        if choice == '1':
            # Load X-Suits
            xsuits = load_items(XSuit_file)
            xsuits = {k.replace(" (4-Star)", ""): v for k, v in xsuits.items()}
            
            # Let user choose X-Suit
            xsuits_name, xsuits_hex = choose_item(xsuits, "𝑪𝒉𝒐𝒐𝒔𝒆 𝒂𝒏 𝑿-𝑺𝒖𝒊𝒕:")
            
            # Load Outfits
            outfits = load_items(Outfits_file)
            
            # Let user search or list all outfits
            search = os.system('toilet -f term -F gay "Choose Replacing outfit"')
            if search:
                filtered_outfits = {k: v for k, v in outfits.items() if search.lower() in k.lower()}
                if not filtered_outfits:
                    os.system('toilet -f term -F gay "No Matching Outfits Found!"')
                    continue
                outfit_name, outfit_hex = choose_item(filtered_outfits, "Choose a replacement outfit:")
            else:
                outfit_name, outfit_hex = choose_item(outfits, "Choose a replacement outfit:")
            
            # Replace hex values in the binary file
            replace_hex_in_file(Original_binary, xsuits_hex, outfit_hex)
        elif choice == '2':
            os.system('toilet -f term -F gay "Exiting..."')
            break
        else:
            os.system('toilet -f term -F gay "Invalid choice! Try again."')

if __name__ == "__main__":
    main()