import os

# Define the repository structure
repo_structure = {
    "docs": "Course materials, lecture slides, and supporting documentation.",
    "code": "Scripts, notebooks, and implementations of data mining algorithms.",
    "data": "Datasets for practice and project work.",
    "projects": "Contributions from student groups, including reports, presentations, and posters.",
    "resources": "Links to textbooks, research papers, and online tools for data mining.",
}

# Base directory for the repository
repo_name = "data-mining-project-repo"
base_path = os.path.join(os.getcwd(), repo_name)

# Create the repository structure
try:
    for folder, description in repo_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        # Create a README.md file in each folder to describe its purpose
        readme_path = os.path.join(folder_path, "README.md")
        with open(readme_path, "w") as readme_file:
            readme_file.write(f"# {folder}\n\n{description}\n")

    print(f"Repository structure created successfully at: {base_path}")
except Exception as e:
    print(f"An error occurred: {e}")
