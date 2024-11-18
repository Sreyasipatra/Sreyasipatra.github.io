import os
from datetime import datetime

# Define the directory containing your Markdown files
directory = "C:/Users/aniki/OneDrive/Desktop/sreyasi/content/posts"

# Function to create front matter
def create_front_matter(filename):
    title = filename.replace("-", " ").replace("_", " ").title()
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
    front_matter = f"""---
title: "{title}"
date: {date}
draft: false
tags: []
author: "Your Name"
showToc: true
TocOpen: false
hidemeta: false
comments: false
description: ""
canonicalURL: ""
disableHLJS: false
disableShare: false
hideSummary: false
searchHidden: false
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true
cover:
  image: ""
  alt: ""
  caption: ""
  relative: false
  hidden: false
editPost:
  URL: "https://github.com/<path_to_repo>/content/posts/{filename}"
  Text: "Suggest Changes"
  appendFilePath: true
---
"""
    return front_matter

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as file:
            content = file.read()
        
        # Create front matter based on the filename
        front_matter = create_front_matter(filename)
        
        # Combine front matter with the original content
        new_content = f"{front_matter}\n{content}"
        
        # Write the new content back to the file
        with open(filepath, "w") as file:
            file.write(new_content)

        print(f"Updated {filename}")

print("All files updated successfully!")
