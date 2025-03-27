import os

# List of weapons with their respective hex codes
weapons = {
    "Starsea Admiral - AKM": "fdf19f41",
    "Bunny Munchkin - AKM": "0ff29f41",
    "Decisive Day - AKM": "1af29f41",
    "Lightshift Temple (Divine Moon) - AKM": "21f29f41",
    "Lightshift Temple (Gold Feather) - AKM": "28f29f41",
    "Sandspring Dominion - AKM": "31f29f41",
    "Dracoguard - M16A4": "77f59f41",
    "Sweetheart Surge - M16A4": "7ef59f41",
    "Seraphic Beacon - M16A4": "85f59f41",
    "Drop the Bass - SCAR-L": "5bf99f41",
    "Bloodstained Nemesis - SCAR-L": "9ff99f41",
    "Radiant Citadel - SCAR-L": "a5f99f41",
    "Folly's Clasp - SCAR-L": "b4f99f41",
    "Serene Lumina - SCAR-L": "bbf99f41",
    "Fantastical Realm - SCAR-L": "c8f99f41",
    "Glacier - M416": "0efd9f41",
    "The Fool - M416": "1efd9f41",
    "Silver Guru - M416": "a9fd9f41",
    "Tidal Embrace - M416": "b1fd9f41",
    "Shinobi Kami - M416": "bafd9f41",
    "Sealed Nether - M416": "c2fd9f41",
    "Roaring Immolation - M416": "ccfd9f41",
    "Pumpkin Carol - Groza": "1a01a041",
    "Primordial Remnants - Groza": "2201a041",
    "Burning Godzilla - Groza": "2a01a041",
    "Forsaken Glace - AUG": "ee04a041",
    "Abyssal Howl - AUG": "fb04a041",
    "Nether Phantom - QBZ": "c608a041",
    "Fatal Foil - QBZ": "d608a041",
    "Empyrean Charm - QBZ": "df08a041",
    "GACKT MOONSAGA - M762": "c60ca041",
    "Noctum Sunder - M762": "fe0ca041",
    "Luminous Muse - M762": "080da041",
    "Skeletal Carver - M762": "120da041",
    "Platinum Skeleton - M762": "1a0da041",
    "Origin Lumen - FAMAS": "ec73a141",
    "Beam Blast - ACE32": "b77ba141",
    "Icicle Spike - ACE32": "c17ba141",
    "Mystic Kraken - ACE32": "c97ba141",
    "Foxie Moxie - ACE32": "d07ba141",
    "Glacier Hammer - UZI": "e033af41",
    "Cryofrost Shard - UMP45": "d837af41",
    "Void Souleater - UMP45": "f838af41",
    "Mecha Drake - Vector": "883baf41",
    "Auspicious Lion - PP-19 Bizon": "4143af41",
    "Devious Cybercat - P90": "b4c9b041",
    "Golden Talon - P90": "bac9b041",
    "Violet Volt - Kar98K": "5b76be41",
    "Thornmaker - Kar98K": "6776be41",
    "Cadence Maestro - M24": "e779be41",
    "Serpengleam - AWM": "cf7dbe41",
    "Graceful Trigger - SKS": "b081be41",
    "Icicle - Mini14": "4e89be41",
    "Ethereal Beauty - Mini14": "5e89be41",
    "Fortune Cat - Mini14": "6a89be41",
    "Gallant Jockey - Mini14": "6f89be41",
    "Drakreign - Mk14": "348dbe41",
    "Falling Blossom - SLR": "fe94be41",
    "Mageblaze - SLR": "0d95be41",
    "Scorching Blessing - AMR": "b3a0be41",
    "Silent Departed - AMR": "bfa0be41",
    "Atomic Trigger - S12K": "ddbfcd41",
    "Cosmic Beast - DBS": "c3c3cd41",
    "Sandsinger - DBS": "c9c3cd41",
    "Moondrop Eterna - M249": "58fadc41",
    "Malus Majesty - M249": "6dfadc41",
    "Data Kitten - DP-28": "5cfedc41",
    "Sky Huntress - MG3": "631ddd41"
}

# Default paths
search_path = "/storage/emulated/0/DARK_PAK/UNPACK_REPACK/UNPACK/game_patch_3.7.0.19729/unpack/"
output_path = "/storage/emulated/0/DARK_PAK/UNPACK_REPACK/UNPACK/game_patch_3.7.0.19729/repack/"

# Display banner interface
def display_banner():
    print("================================")
    print("         MOD HIT EFFECT         ")
    print("================================")

# Display options
def display_options():
    print("1. BULK Mode")
    print("2. SEARCH AND MOD")
    print("3. CHANGE PATH")
    print("Choose Option (1/2/3):", end=" ")

# Function to change paths
def change_path():
    global search_path, output_path
    print("Enter the new file finding path:")
    new_search_path = input("🔍: ").strip()
    
    if not new_search_path.endswith('/'):
        new_search_path += '/'
    
    new_output_path = new_search_path.rsplit('/', 2)[0] + '/repack/'
    
    search_path = new_search_path
    output_path = new_output_path
    
    print("File finding path updated to:", search_path)
    print("Output path updated to:", output_path)

# Function to process BULK mode
def bulk_mode():
    print("Enter HEX pairs (Glacier hex,Camo hex) line by line. Enter 'q' to finish:")
    id_pairs = []
    while True:
        pair = input().strip()
        if pair.lower() == 'q':
            break
        try:
            original_id, replacement_id = pair.split(',')
            id_pairs.append((bytes.fromhex(original_id.strip()), bytes.fromhex(replacement_id.strip())))
        except ValueError:
            print("Invalid format! Use OLD_HEX,NEW_HEX")
    
    if not id_pairs:
        print("No HEX pairs provided!")
        return
    
    process_hex_replacements(id_pairs)

# Function to process SEARCH AND MOD mode
def search_and_mod():
    print("Enter search keyword:")
    keyword = input("🔍: ").strip().lower()
    
    matched_weapons = [weapon for weapon in weapons.keys() if keyword in weapon.lower()]
    
    if not matched_weapons:
        print("No matching skins found!")
        return
    
    for i, weapon in enumerate(matched_weapons, start=1):
        print(f"{i}. {weapon}")
    
    selected_indices = input("Select weapons (comma-separated): ").strip().split(',')
    
    try:
        selected_weapons = [matched_weapons[int(index) - 1] for index in selected_indices]
    except (IndexError, ValueError):
        print("Invalid selection!")
        return
    
    hex_pairs = []
    for weapon in selected_weapons:
        print(f"Enter Replacing Hex for: {weapon}")
        replacement_hex = input("🔍: ").strip()
        hex_pairs.append((bytes.fromhex(weapons[weapon]), bytes.fromhex(replacement_hex)))
    
    process_hex_replacements(hex_pairs)

# Function to process hex replacements
def process_hex_replacements(hex_pairs):
    global search_path, output_path
    os.makedirs(output_path, exist_ok=True)
    
    for root, _, files in os.walk(search_path):
        for file in files:
            file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_path, file)
            
            # Process only files with size exactly 3314 bytes
            if os.path.getsize(file_path) != 3314:
                continue
            
            try:
                with open(file_path, "rb") as f:
                    content = f.read()
                
                modified_content = content
                for old_hex, new_hex in hex_pairs:
                    modified_content = modified_content.replace(old_hex, new_hex)
                
                if modified_content != content:
                    with open(output_file_path, "wb") as f:
                        f.write(modified_content)
                    print(f"The file {file} has been extracted and modified")
            
            except Exception as e:
                print(f"Error processing {file}: {e}")
    
    print("🎉 Search and Replacement Completed, Modified Files Saved!")

# Main function
def main():
    global search_path, output_path
    while True:
        display_banner()
        display_options()
        
        choice = input("🔹 : ").strip()
        
        if choice == "1":
            bulk_mode()
        elif choice == "2":
            search_and_mod()
        elif choice == "3":
            change_path()
        else:
            print("Invalid option!")
        
        input("Press Enter to return to the main menu...")

if __name__ == "__main__":
    main()