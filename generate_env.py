# Code to generate .env file with environment variables
import os

# REPLACE WITH YOUR OWN VALUES BEFORE RUNNING THIS SCRIPT!
env_content = {
    "CANVAS_DOMAIN": "your_canvas_domain.instructure.com",  # e.g., "myinstitution.instructure.com"
    "CANVAS_TOKEN": "your_canvas_api_token"           # e.g., "1234567890abcdef1234567890abcdef"
}

with open(".env", "w") as env_file:
    for key, value in env_content.items():
        env_file.write(f"{key}={value}\n")


print("Generated .env file with the following content:")
for key, value in env_content.items():
    print(f"  {key}={value}")