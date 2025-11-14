import os

def create_structure(structure):
    """
    Creates folders and files based on a dictionary structure.
    """
   
    base_path=os.getcwd()

    for folder_name, files in structure.items():
        # 1. Create the folder path
        # Use os.path.join to ensure it works on Windows (\) and Mac (/)
        current_folder = os.path.join(base_path, folder_name)
        os.makedirs(current_folder, exist_ok=True)
        
        if folder_name:
            print(f"  📁 Created Folder: {folder_name}")

        # 2. Create the files inside that folder
        for file_name in files:
            file_path = os.path.join(current_folder, file_name)
            
            # Create the file and write some starter content
            with open(file_path, 'w') as f:
                if file_name.endswith('.py'):
                    f.write(f"# {file_name}\n# Created automatically\n\ndef main():\n    pass\n")
                elif file_name.endswith('.md'):
                    f.write(f"# {base_path}\nProject documentation.")
                else:
                    f.write("") # Create empty file
            
            print(f"    📄 Created File: {file_name}")

# --- CONFIGURATION ---

# 1. Name your project folder
PROJECT_NAME = "Personal_assistant"

# 2. Define your folders (keys) and files (values list)
# Use "" (empty string) for files that should be in the root folder
project_layout = {
    "":             ["main.py", "requirements.txt"],
    "data":         [],
    "notebooks":    ["calender.py"],
    "src":          ["utils.py", ],
    "tests":        ["test_main.py"]
}

# --- RUN ---
if __name__ == "__main__":
    create_structure(project_layout)
    print("\n✅ Setup Complete!")