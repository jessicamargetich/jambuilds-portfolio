#!/usr/bin/env python3
"""
Development server startup script for Jessica Margetich's portfolio website.
This script handles virtual environment setup and development server startup.
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python():
    """Check if Python 3 is available."""
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"Using Python: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"Error checking Python: {e}")
        return False

def setup_venv():
    """Set up virtual environment if it doesn't exist."""
    venv_path = Path("venv")
    if not venv_path.exists():
        print("Creating virtual environment...")
        try:
            subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
            print("Virtual environment created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            return False
    return True

def install_dependencies():
    """Install required dependencies."""
    pip_path = "venv/bin/pip" if os.name != "nt" else "venv\\Scripts\\pip.exe"
    requirements_file = "requirements.txt"

    if not Path(requirements_file).exists():
        print(f"Error: {requirements_file} not found.")
        return False

    try:
        print("Installing dependencies...")
        subprocess.run([pip_path, "install", "-r", requirements_file], check=True)
        print("Dependencies installed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        # Try alternative installation method
        try:
            print("Trying alternative installation...")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_file], check=True)
            print("Dependencies installed successfully (alternative method).")
            return True
        except subprocess.CalledProcessError as e2:
            print(f"Alternative installation also failed: {e2}")
            return False

def start_server():
    """Start the development server."""
    python_path = "venv/bin/python" if os.name != "nt" else "venv\\Scripts\\python.exe"

    # Check if virtual environment Python exists
    if not Path(python_path).exists():
        python_path = sys.executable
        print("Using system Python (virtual environment not available)")

    try:
        print("Starting development server...")
        print("Visit: http://localhost:8000")
        print("Press Ctrl+C to stop the server")
        subprocess.run([python_path, "app.py"])
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting server: {e}")
        return False
    except FileNotFoundError:
        print("Error: app.py not found in current directory")
        return False

def main():
    """Main development setup and server startup."""
    print("Jessica Margetich Portfolio - Development Server Setup")
    print("=" * 50)

    # Check current directory
    if not Path("app.py").exists():
        print("Error: Please run this script from the portfolio project directory")
        return 1

    # Check Python
    if not check_python():
        return 1

    # Setup virtual environment
    if not setup_venv():
        print("Continuing without virtual environment...")

    # Install dependencies
    if not install_dependencies():
        print("Warning: Could not install dependencies. You may need to install them manually:")
        print("pip install fastapi uvicorn jinja2 pyyaml python-multipart aiofiles")
        print("\nTrying to start server anyway...")

    # Start server
    start_server()
    return 0

if __name__ == "__main__":
    sys.exit(main())