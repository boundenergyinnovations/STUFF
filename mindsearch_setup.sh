#!/bin/bash

# Function to execute a command and wait for it to finish
execute_command() {
    echo "About to execute: $1"
    read -p "Do you want to proceed? (y/n): " choice
    case "$choice" in 
        y|Y ) 
            echo "Executing: $1"
            eval "$1"
            local exit_status=$?
            if [ $exit_status -ne 0 ]; then
                echo "Command failed with exit status $exit_status"
                read -p "Do you want to continue with the next command? (y/n): " continue_choice
                if [[ ! $continue_choice =~ ^[Yy]$ ]]; then
                    exit $exit_status
                fi
            else
                echo "Command completed successfully"
            fi
            ;;
        n|N ) 
            echo "Skipping this command"
            ;;
        * ) 
            echo "Invalid input, skipping this command"
            ;;
    esac
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Main script execution
main() {
    # Check for required commands
    for cmd in git conda pip; do
        if ! command_exists "$cmd"; then
            echo "Error: $cmd is not installed or not in PATH. Please install it and try again."
            exit 1
        fi
    done

    # Initialize conda for the script
    if [ -f "$HOME/miniconda3/etc/profile.d/conda.sh" ]; then
        . "$HOME/miniconda3/etc/profile.d/conda.sh"
    else
        echo "Warning: Conda initialization file not found. You may need to activate conda manually."
    fi

    # Clone the repository
    execute_command "conda create -n mindsearch python=3.11 -y  && conda activate mindsearch"

    # Change directory to Fooocus
    execute_command "git clone https://github.com/InternLM/MindSearch && cd MindSearch"

    # Create conda environment
    execute_command "pip install -r requirements.txt"

    echo "Script execution completed"
}

# Run the main function
main
