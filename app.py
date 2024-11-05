import os
import subprocess
import time

def update_package():
    subprocess.run(["git", "pull"], check=True)
    subprocess.run(["pip", "install", "-e", "."], check=True)

# Update and install the package
update_package()

# Start the Gradio app
subprocess.run(["f5-tts_infer-gradio"])
