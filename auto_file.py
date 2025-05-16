# The goal of this program is to:
# - Open a file.
# - Read and import the file, line by line.
# - Create a file per name or a directory per name.

import os

def import_file() -> list[str]:
    """Open a given file and return a list of the contents with blank lines removed"""
    imported_list = []

    with open("names.txt", "r") as file: # can change this to be a variable given to the function to define other files.
        for line in file:
            if line.strip() != "": # checks for blank entries and excludes them.
                imported_list.append(line.strip())
    
    return imported_list


def create_parent_dir() -> None:
    """Creates a directory for the ease of file management post creation, can also be used to create multiple"""
    PATH = "names" # this can be changed to make the function take an argument to create multiple dirs if needed. 

    if not os.path.exists(PATH): # if the given dir name doesn't exist the next line creates it.
        os.makedirs(PATH)


def create_dir(import_file :list[str], parent_dir :str) -> None:
    """creates a directory for each line of import_file in the directory given in parent_dir"""
    for line in import_file:

        if not os.path.exists(line):
            os.makedirs("names/" + line, exist_ok=True)


def create_file(import_file :list[str]) -> None:
    """Creates a file with the name on each line of the given list, does not return anything"""
    for line in import_file: # repeats for each name in imported_list

        file_path = os.path.join("names", line) # this returns a file path using the correct seperator. Makes this work on windows AND linux.
        open(file_path, "x") # this creates a file in the folder above.


def user_choice(parent_dir :str) -> None:
    """gets user input to determine the creation of directories or files."""
    choice = input("1 for Directories only, 2 for files only: ").strip().lower()

    if choice == "1":
        create_dir(import_file() , parent_dir)        

    elif choice == "2":
        create_file(import_file())
    
    else:
        print("choice is invalid. 1 or 2 are valid choices.")



def main() -> None:
    print("Main is now running:")

    create_parent_dir()
    user_choice("names")
    

    print("Main has finished running.")

if __name__ == "__main__":
    main()
