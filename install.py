#!/usr/bin/env python3
"""
Apollog Installation Script

This script helps users install Apollog and initialize a new project.
"""

import os
import sys
import subprocess
import argparse

def run_command(command, description=None):
    """Run a shell command and print its output."""
    if description:
        print(f"\n{description}...")
    
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(e.stderr)
        return False

def install_package(dev_mode=False):
    """Install the Apollog package."""
    if dev_mode:
        cmd = "pip install -e ."
        desc = "Installing Apollog in development mode"
    else:
        cmd = "pip install ."
        desc = "Installing Apollog"
    
    return run_command(cmd, desc)

def initialize_project(destination="."):
    """Initialize a new Apollog project."""
    cmd = f"apollog init --destination {destination}"
    desc = f"Initializing new Apollog project in {destination}"
    
    return run_command(cmd, desc)

def main():
    parser = argparse.ArgumentParser(description="Install Apollog and initialize a new project")
    parser.add_argument("--dev", action="store_true", help="Install in development mode")
    parser.add_argument("--init", action="store_true", help="Initialize a new project after installation")
    parser.add_argument("--destination", default=".", help="Directory where to initialize the project")
    
    args = parser.parse_args()
    
    # Install the package
    if not install_package(args.dev):
        sys.exit(1)
    
    # Initialize a new project if requested
    if args.init:
        if not initialize_project(args.destination):
            sys.exit(1)
    
    print("\nInstallation completed successfully!")
    
    if not args.init:
        print("\nTo initialize a new project, run:")
        print("  apollog init")
    
    print("\nTo deploy a stack, run:")
    print("  apollog deploy --config examples/config.yaml")
    
    print("\nFor more information, see the README.md file or visit:")
    print("  https://github.com/Bhavinrathava/Apollog")

if __name__ == "__main__":
    main()
