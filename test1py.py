import webbrowser
import os

# Create the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Greeting</title>
</head>
<body>
    <h1>Hi my friend</h1>
</body>
</html>
"""

# Save the HTML content to a local file
file_path = os.path.abspath("greeting.html")
with open(file_path, "w") as file:
    file.write(html_content)

# Open the HTML file in the default web browser
webbrowser.open(f"file://{file_path}")
