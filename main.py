import os
import shutil

def find_winamp_folder():
    roaming_path = os.path.join(os.getenv('APPDATA'), 'Winamp')
    if os.path.exists(roaming_path):
        return roaming_path
    return None

def copy_and_remove_folder(source_path, destination_path):
    try:
        shutil.copytree(source_path, destination_path)
        shutil.rmtree(source_path)
        print("Winamp folder successfully moved.")
    except Exception as e:
        print(f"Error while processing Winamp folder: {e}")

def fixing_func():
    winamp_folder = find_winamp_folder()
    if winamp_folder:
        project_folder = os.path.dirname(os.path.abspath(__file__))
        destination_folder = os.path.join(project_folder, 'Winamp')

        print(f"Winamp folder found at: {winamp_folder}")
        print(f"Moving to directory: {destination_folder}")

        copy_and_remove_folder(winamp_folder, destination_folder)
    else:
        print("No Winamp folder found in AppData\\Roaming.")

def main():
    print("Welcome to Winamp Fixer")
    while True:
        print("Do you want to fix your Winamp? (y/n)")
        confirm_fix = input().strip().lower()
        if confirm_fix == "y":
            print("The fixing process has started...")
            fixing_func()
            break
        elif confirm_fix == "n":
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
