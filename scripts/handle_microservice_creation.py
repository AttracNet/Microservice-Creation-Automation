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

# Read existing or create a new JSON configuration file
config_file = 'config.json'
try:
    config = read_config(config_file)
except FileNotFoundError:
    config = {}

# Gather user input for microservice details
org_name = input("Enter organization name: ")
repo_name = input("Enter repository name: ")
visibility = input("Enter visibility (public/private): ")
description = input("Enter repository description: ")
initialize_readme = input("Initialize README (true/false): ").lower() == 'true'
enable_automation = input("Enable GitHub automation (true/false): ").lower() == 'true'

# Update the configuration file
config['organization'] = org_name
config['repository'] = repo_name
config['visibility'] = visibility
config['description'] = description
config['initialize_readme'] = initialize_readme
config['enable_automation'] = enable_automation

# Save the updated configuration
write_config(config_file, config)

# Optionally, create the GitHub repo if automation is enabled
if enable_automation:
    repo_url = create_github_repo(org_name, repo_name, visibility, description, initialize_readme)
    config['repo_url'] = repo_url
    write_config(config_file, config)
    print(f"GitHub repository created: {repo_url}")
