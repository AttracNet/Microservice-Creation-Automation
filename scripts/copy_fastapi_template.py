import argparse
import shutil
import os
import json
import subprocess

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config

def write_config(file_path, config):
    with open(file_path, 'w') as file:
        json.dump(config, file, indent=2)

def create_github_repo(org_name, repo_name, visibility, description, initialize_readme):
    cmd = f"gh repo create {org_name}/{repo_name} --{visibility} --description '{description}' --{initialize_readme} --enable-issues=false --enable-actions=false --enable-wiki=false"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def ask_for_user_input(dest_directory, microservice_name):
    # Read existing or create a new JSON configuration file in the destination directory
    config_file = os.path.join(dest_directory, 'config.json')
    try:
        config = read_config(config_file)
    except FileNotFoundError:
        config = {}

    # Gather user input for microservice details
    org_name_input = input("Is the Org name: AttracNet? (y/n)").lower()
    org_name = True if org_name_input == 'y' else input("Enter organization name:  ")

    repo_name_input = input(f"Is the repository name: {microservice_name}? (y/n)  ").lower()
    repo_name = microservice_name if repo_name_input == 'y' else input("Enter repository name: ")  # Default value if user doesn't provide input

    visibility_input = input("Do you want the repo set to public? (y/n) ").lower()
    visibility = True if visibility_input == '--public' else False

    description = input("Enter repository description:  ")

    initialize_readme_input = input("Initialize README (true/false): ").lower()
    initialize_readme = '--add-readme' if initialize_readme_input == 'true' else False  # Default value if user doesn't provide input

    enable_automation_input = input("Enable GitHub automation (true/false): ").lower()
    enable_automation = True if enable_automation_input == 'true' else False  # Default value if user doesn't provide input

    set_remote_input = input("Setup remote repo for new microservice? (y/n)  ").lower()
    set_remote = True if set_remote_input == 'y' else False

    # Update the configuration file
    config['organization'] = org_name
    config['repository'] = repo_name
    config['visibility'] = visibility
    config['description'] = description
    config['initialize_readme'] = initialize_readme
    config['enable_automation'] = enable_automation
    config['source'] = dest_directory
    config['remote'] = set_remote

    # Save the updated configuration
    write_config(config_file, config)

    # Optionally, create the GitHub repo if automation is enabled
    if enable_automation:
        repo_url = create_github_repo(org_name, repo_name, visibility, description, initialize_readme)
        config['repo_url'] = repo_url
        write_config(config_file, config)
        print(f"GitHub repository created: {repo_url}")

def copy_template(src_dir, dest_dir, force=False):
    try:
        # If the destination directory already exists and force flag is not set, raise an error
        if os.path.exists(dest_dir) and not force:
            raise FileExistsError(f"Destination directory '{dest_dir}' already exists. Use -f or --force to override.")

        # Copy the template using shutil.copytree with the ignore parameter
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)

        print(f"Microservice template copied to {dest_dir}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Copy FastAPI template to a new microservice.")
    parser.add_argument("new_microservice_name", help="Name for the new microservice")
    parser.add_argument("-f", "--force", action="store_true", help="Force copy even if the destination directory exists")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the new microservice name and force flag
    new_microservice = args.new_microservice_name
    force_copy = args.force

    # Define source and destination directories
    source_directory = "../templates/fastapi_template"
    destination_directory = f"../microservices/{new_microservice}"

    # Get the absolute paths based on the current script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_directory = os.path.abspath(os.path.join(script_dir, source_directory))
    destination_directory = os.path.abspath(os.path.join(script_dir, destination_directory))

    # Call the function to copy the template
    copy_template(source_directory, destination_directory, force_copy)

    # Ask for user input to complete JSON config file
    ask_for_user_input(destination_directory, new_microservice)

    print("Finishing up template copy and other setup. Exiting setup script.\n")
    print("New microservice created successfully!\n\n")
