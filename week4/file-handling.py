filename = input("Enter the filename to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"❌ Error: '{filename}' not found.")
    exit()
except IOError:
    print(f"❌ Error: Could not read '{filename}'.")
    exit()

# Modify content of the file (example: convert to uppercase)
modified_content = content.upper()

# Write to a new file
new_filename = "modified_" + filename
try:
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)
    print(f"✅ Modified content saved to '{new_filename}'.")
except IOError:
    print(f"❌ Error: Could not write to '{new_filename}'.")
