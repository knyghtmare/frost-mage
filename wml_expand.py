#!/usr/bin/env python3
import os
import subprocess
import sys

# Directory to start walking from (current dir by default)
start_dir = sys.argv[1] if len(sys.argv) > 1 else "."

# Path to your preprocessor script
preprocessor_script = "./wml_syntax_expander.py"

if not os.path.isfile(preprocessor_script):
    print(f"Error: {preprocessor_script} not found in current directory.")
    sys.exit(1)

for root, dirs, files in os.walk(start_dir):
    for file in files:
        if file.endswith(".cwml"):
            input_path = os.path.join(root, file)
            # Output path: same name but with .wml extension
            output_path = os.path.splitext(input_path)[0] + ".cfg"
            print(f"Processing {input_path} -> {output_path}")
            # Run preprocessor; original .cwml remains untouched
            subprocess.run([sys.executable, preprocessor_script, input_path, output_path])
