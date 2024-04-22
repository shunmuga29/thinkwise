import os

# The structure of the chapters and the number of sections in each
chapters_and_sections = {
    1: 10,
    2: 11,
    3: 9,
    4: 6,
    5: 6,
    6: 3,
    7: 5,
    8: 6,
}

# Loop through the chapters and sections to create files
for chapter, sections in chapters_and_sections.items():
    for section in range(1, sections + 1):
        filename = f"Chapter_{chapter}_Section_{section}.html"
        with open(filename, 'w') as file:
            # Optional: You can write initial HTML structure here
            file.write('')  # Creating an empty HTML file

print("HTML files created successfully.")
