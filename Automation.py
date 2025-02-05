import os
import shutil
from colorama import Fore, Style

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk"],
    "Others": []
}

def organize_files(directory):
    """Sorts files into categories based on their extensions."""
    if not os.path.exists(directory):
        print(Fore.RED + "⚠️ Directory not found!" + Style.RESET_ALL)
        return

    # Create category folders if they don’t exist
    for category in FILE_CATEGORIES.keys():
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)

    # Move files to respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                print(Fore.GREEN + f"✅ Moved {filename} to {category}" + Style.RESET_ALL)
                moved = True
                break
        
        if not moved:  
            shutil.move(file_path, os.path.join(directory, "Others", filename))
            print(Fore.YELLOW + f"⚠️ Moved {filename} to Others" + Style.RESET_ALL)

    print(Fore.CYAN + "\n🎉 File organization complete!" + Style.RESET_ALL)

def user_interface():
    """Interactive user menu."""
    print(Fore.BLUE + "\n📂 File Organizer - Automate Your File Sorting!" + Style.RESET_ALL)
    
    while True:
        print("\n1️⃣ Organize Files")
        print("2️⃣ Exit")
        
        choice = input(Fore.YELLOW + "Choose an option (1-2): " + Style.RESET_ALL)

        if choice == "1":
            folder_path = input(Fore.GREEN + "Enter the folder path to organize: " + Style.RESET_ALL)
            organize_files(folder_path)
        elif choice == "2":
            print(Fore.MAGENTA + "🚀 Exiting File Organizer. Have a clean day!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ Invalid choice! Try again." + Style.RESET_ALL)

# Run the program
user_interface()
