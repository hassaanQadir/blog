# This script checks the README.md for "Summer 2024 Tech Internships by Pitt CSC & Simplify" on Github against my personal list of companies I want to apply to. Feel free to adapt for your own purposes!

# First, import the necessary modules
import requests  # requests module for making HTTP requests
import re  # re module for using regular expressions

# This function takes a url to a markdown file and a list of names and a list of names for exact matching, 
# and returns a list of table rows where any of the names appear.
def check_names_in_md_file(url, names, exactNames):
    # Make a GET request to the provided URL
    response = requests.get(url)
    # Get the text content from the response
    content = response.text
    
    # Use a regular expression to search for a markdown table in the content
    table = re.search(r'\| Company \| Role \| Location \| Application/Link \| Date Posted \|\n\| --- \| --- \| --- \| :---: \| :---: \|\n((?:\|.+\|\n)+)', content)

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
        for listed_name in names:
            # If the listed name is found within the row (ignoring case), add the row to the list of found rows
            if listed_name.lower() in row.lower():
                found_rows.append(row)
                break  # Break out of the inner loop once a match is found for this row
    
    
    # does the exact same thing as above but only returns rows if there is an exact match for the name
    for row in rows:
        name = re.search(r'\|\s\*\*\[(.+?)\]\(', row)
        if name:
            for listed_name in exactNames:
                if re.search(r'^\b' + re.escape(listed_name.lower()) + r'\b$', name.group(1).lower()):
                    found_rows.append(row)

    # Return the list of found rows
    return found_rows

# List of names to search for in the markdown table
names = [
    "Meta", "Google", "Alphabet", "Apple", "Amazon", "Microsoft", "Nvidia", "Airbnb", 
    "Stripe", "Pinterest", "Facebook", "Lyft", "DoorDash", "Box", "Twitter", "Dropbox", "Tesla", 
    "Salesforce", "Palantir", "Asana", "Uber", "Robinhood", "Roblox", "Databricks", "Plaid", "Coinbase", 
    "Atlassian", "Quora", "Cruise", "Waymo", "Two Sigma", "Instabase", "Twitch", "Wish", "Rippling", 
    "Flexport", "Snowflake", "Square", "Docusign", "Samsara", "Match", "Okta", "Benchling", "Twist", 
    "Genentech", "Schrodinger", "Discord", "Slack", "Snap", "Yelp"
] 

# List of names to search for in the markdown table but only matching on exact matches
exactNames = ["LinkedIn"]

# URL of the markdown file to check
url = "https://raw.githubusercontent.com/SimplifyJobs/Summer2024-Internships/dev/README.md"

# Call the function with the provided URL and list of names and list of names for exact matching
found_rows = check_names_in_md_file(url, names, exactNames)

# If any rows were found, print them. Otherwise, print a message indicating that no names were found.
if found_rows:
    print("Rows found in the table:")
    for row in found_rows:
        print(row)
else:
    print("No names from the list found in the table.")
