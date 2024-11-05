import subprocess

def uninstall_package():
    subprocess.run(["pip", "uninstall", "git+https://github.com/jpgallegoar/Spanish-F5"], check=True)

def install_package():
    subprocess.run(["pip", "install", "--upgrade", "git+https://github.com/jpgallegoar/Spanish-F5"], check=True)

# Install the package on startup
install_package()

# Start the Gradio app
subprocess.run(["f5-tts_infer-gradio"])

