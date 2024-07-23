#!/bin/bash

# Function to print the 10th line
print_10th_line() {
    local filename="$1"
    
    : '
    This function takes a filename as an argument
    and prints the 10th line of the file.
    If the file contains fewer than 10 lines,
    nothing is printed.
    '

    # Check if the file exists
    if [[ ! -f "$filename" ]]; then
        echo "File not found!"
        return
    fi

    # Using sed to print the 10th line
    sed -n '10p' "$filename"
}

# Check if the filename is provided as an argument
if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Call the function with the provided filename
print_10th_line "$1"
