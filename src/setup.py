import boto3
import anthropic
import os
import json
from datetime import datetime

def create_s3_bucket(project_name, region="us-east-1"):
    """Create an S3 bucket for the project on AWS."""
    s3 = boto3.client("s3", region_name=region)
    bucket_name = f"{project_name}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    print(f"🪣 Creating S3 bucket: {bucket_name}...")
    
    s3.create_bucket(Bucket=bucket_name)
    
    print(f"✅ S3 bucket created: {bucket_name}")
    return bucket_name

def create_local_folders(project_name):
    """Create local folder structure for the project."""
    folders = [
        f"{project_name}/src",
        f"{project_name}/logs",
        f"{project_name}/config",
        f"{project_name}/tests",
    ]
    
    print(f"📁 Creating local folder structure...")
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"   Created: {folder}")
    
    return folders

def generate_config_with_ai(project_name, bucket_name):
    """Use Claude to generate a smart config file for the project."""
    client = anthropic.Anthropic()
    
    print(f"🤖 Using Claude to generate config file...")
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Generate a JSON config file for an AWS project called "{project_name}".
                
Include these fields:
- project_name
- s3_bucket (use "{bucket_name}")
- region (use "us-east-1")
- environment (use "development")
- created_at (use today's date)
- logging (object with level and log_file fields)
- tags (object with project and owner fields)

Return only the JSON, nothing else."""
            }
        ]
    )
    
    config = message.content[0].text
    return config

def save_config(project_name, config):
    """Save the generated config to the project folder."""
    config_path = f"{project_name}/config/config.json"
    
    with open(config_path, "w") as f:
        f.write(config)
    
    print(f"✅ Config saved to {config_path}")

def print_summary(project_name, bucket_name, folders):
    """Print a summary of everything that was created."""
    print("\n" + "="*50)
    print("🚀 PROJECT SETUP COMPLETE")
    print("="*50)
    print(f"Project Name : {project_name}")
    print(f"S3 Bucket    : {bucket_name}")
    print(f"Folders      : {len(folders)} created")
    print(f"Config       : {project_name}/config/config.json")
    print("="*50)

def main():
    print("=== AWS Project Setup Automator ===\n")
    
    project_name = input("Enter your project name: ").strip().lower().replace(" ", "-")
    
    # Step 1: Create S3 bucket
    bucket_name = create_s3_bucket(project_name)
    
    # Step 2: Create local folders
    folders = create_local_folders(project_name)
    
    # Step 3: Generate config with Claude
    config = generate_config_with_ai(project_name, bucket_name)
    
    # Step 4: Save config
    save_config(project_name, config)
    
    # Step 5: Print summary
    print_summary(project_name, bucket_name, folders)

if __name__ == "__main__":
    main()
    