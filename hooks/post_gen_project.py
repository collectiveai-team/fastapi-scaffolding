import os
import shutil


sources_targets = [
    ("./{{cookiecutter.api_module_name}}", "../{{cookiecutter.api_module_name}}"),
    ("./build/api", "../build/api"),
    (".vscode/launch.json", "../.vscode/launch.json"),
]


def move_files(source_dir, target_dir):
    if os.path.exists(source_dir):
        shutil.move(source_dir, target_dir)
        print(f"Moved {source_dir} to {target_dir}")
    else:
        print("No action needed.")
        print(f"Source: {source_dir} exists: {os.path.abspath(source_dir)}")

for source, target in sources_targets:
    move_files(source, target)

# Remove the empty directories
shutil.rmtree("../{{cookiecutter.project_slug}}")