import subprocess
import platform

def install_packages(package_file):
    """Installs packages listed in a file using the appropriate package manager."""

    try:
        with open(package_file, 'r') as f:
            packages = [line.strip() for line in f]  # Read packages from file
    except FileNotFoundError:
        print(f"Error: File '{package_file}' not found.")
        return

    os_name = platform.system()

    if os_name == "Linux":
        # Determine package manager (apt or yum)
        if subprocess.call(['which', 'apt'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            package_manager = "apt"
        elif subprocess.call(['which', 'yum'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            package_manager = "yum"
        else:
            print("Error: No supported package manager found (apt or yum).")
            return
    elif os_name == "Darwin":  # macOS
        if subprocess.call(['which', 'brew'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            package_manager = "brew"
        else:
            print("Error: Homebrew (brew) not found.")
            return
    else:
        print(f"Error: Unsupported operating system: {os_name}")
        return

    print(f"Using package manager: {package_manager}")

    for package in packages:
        print(f"Installing {package}...")
        try:
            if package_manager == "apt":
                subprocess.check_call(['sudo', 'apt', 'install', '-y', package])
            elif package_manager == "yum":
                subprocess.check_call(['sudo', 'yum', 'install', '-y', package])
            elif package_manager == "brew":
                subprocess.check_call(['brew', 'install', package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")

if __name__ == "__main__":
    install_packages("packages.txt")