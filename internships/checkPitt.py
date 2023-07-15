# This script checks the README.md for "Summer 2024 Tech Internships by Pitt CSC & Simplify" on Github against my personal list of companies I want to apply to. Feel free to adapt for your own purposes!

# First, import the necessary modules
import requests  # requests module for making HTTP requests
import re  # re module for using regular expressions

# This function takes a url to a markdown file and a list of names, and returns a list of table rows where any of the names appear.
def check_names_in_md_file(url, names):
    # Make a GET request to the provided URL
    response = requests.get(url)
    # Get the text content from the response
    raw_md = response.text

    # Use a regular expression to search for a markdown table in the text. A markdown table starts with a header row and at least one row of data.
    table = re.search(r'\| Name \| Location \| Notes \|\n\| ---- \| -------- \| ----- \|\n((?:\|.+\|\n)+)', raw_md)

    # If no table is found, return an empty list
    if not table:
        return []
    
    # Extract the content of the table
    table = table.group(1)
    # Split the table into rows
    rows = table.split('\n')[:-1]  # Exclude the last split, as it's an empty string

    found_rows = []  # Initialize the list of found rows

    # Iterate over the rows
    for row in rows:
        # Extract the name from each row
        name = re.search(r'\|\s(.+?)\s\|', row)
        # If a name is found, compare it to the list of names
        if name:
            for listed_name in names:
                # If the listed name is found within the name in the row (ignoring case), add the row to the list of found rows
                if listed_name.lower() in name.group(1).lower():
                    found_rows.append(row)

    # Return the list of found rows
    return found_rows

# List of names to search for in the markdown table
names = [
    "LinkedIn", "Meta", "Google", "Alphabet", "Apple", "Amazon", "Microsoft", "Nvidia", "Airbnb", 
    "Stripe", "Pinterest", "Facebook", "Lyft", "DoorDash", "Box", "Twitter", "Dropbox", "Tesla", 
    "Salesforce", "Palantir", "Asana", "Uber", "Robinhood", "Roblox", "Databricks", "Plaid", "Coinbase", 
    "Atlassian", "Quora", "Cruise", "Waymo", "Two Sigma", "Instabase", "Twitch", "Wish", "Rippling", 
    "Flexport", "Snowflake", "Square", "Docusign", "Samsara", "Match", "Okta", "Benchling", "Twist", 
    "Genentech", "Schrodinger", "Discord", "Slack", "Snap", "Yelp"
] 

# URL of the markdown file to check
url = "https://raw.githubusercontent.com/pittcsc/Summer2024-Internships/dev/README.md"

# Call the function with the provided URL and list of names
found_rows = check_names_in_md_file(url, names)

# If any rows were found, print them. Otherwise, print a message indicating that no names were found.
if found_rows:
    print("Rows found in the table:")
    for row in found_rows:
        print(row)
else:
    print("No names from the list found in the table.")
