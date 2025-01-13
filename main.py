import os
import shutil
from termcolor import cprint

def find_winamp_folder():
    roaming_path = os.path.join(os.getenv('APPDATA'), 'Winamp')
    if os.path.exists(roaming_path):
        return roaming_path
    return None

def copy_and_remove_folder(source_path, destination_path):
    try:
        shutil.copytree(source_path, destination_path)
        shutil.rmtree(source_path)
        cprint("Winamp folder successfully moved.", "green")
    except Exception as e:
        cprint(f"Error while processing Winamp folder: {e}", "red")

def fixing_func():
    winamp_folder = find_winamp_folder()
    if winamp_folder:
        project_folder = os.path.dirname(os.path.abspath(__file__))
        destination_folder = os.path.join(project_folder, 'Winamp')

        cprint(f"Winamp folder found at: {winamp_folder}", "yellow")
        cprint(f"Moving to directory: {destination_folder}", "yellow")

        copy_and_remove_folder(winamp_folder, destination_folder)
    else:
        cprint("No Winamp folder found in AppData\\Roaming.", "red")

def main():
    cprint("Welcome to Winamp Fixer", "blue")
    while True:
        cprint("Do you want to fix your Winamp? (y/n)", "blue")
        confirm_fix = input().strip().lower()
        if confirm_fix == "y":
            cprint("The fixing process has started...", "yellow")
            fixing_func()
            break
        elif confirm_fix == "n":
            cprint("Exiting program.", "blue")
            break
        else:
            cprint("Invalid input. Please enter 'y' or 'n'.", "red")

if __name__ == "__main__":
    main()
