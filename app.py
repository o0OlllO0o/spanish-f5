import subprocess

def install_package():
    subprocess.run(["pip", "install", "--upgrade", "git+https://github.com/jpgallegoar/Spanish-F5", "--no-cache-dir"], check=True)


# Install the package on startup
install_package()

# Start the Gradio app
subprocess.run(["f5-tts_infer-gradio"])

