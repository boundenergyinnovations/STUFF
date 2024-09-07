import os
import re

def extract_md_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r'<<~MD\s*(.*?)\s*MD'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1).strip()
    return None

def process_directory(directory_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                content = extract_md_content(file_path)
                if content:
                    output_file.write(f"# Content from {filename}\n\n")
                    output_file.write(content)
                    output_file.write("\n\n")

def main():
    directory_path = input("Enter the directory path: ")
    output_file_path = input("Enter the output file path: ")
    
    if not os.path.exists(directory_path):
        print(f"Error: The directory '{directory_path}' does not exist.")
        return
    
    process_directory(directory_path, output_file_path)
    print(f"Extraction complete. Results written to {output_file_path}")

if __name__ == "__main__":
    main()
