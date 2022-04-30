import json

#This is the <filterlist> from the main Python file, a compiled list of all scraped items
#As per discussion with Professor Madamanchi on 4/29, received permission to use filter instead of tree as solution

def read_json(filepath, encoding='utf-8'):
    """
    Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.
    Parameters:
        filepath (string): path to file
        encoding (string): optional name of encoding used to decode the file. The default is 'utf-8'.
    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """
    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


filterlist = read_json("./finalprojectJSON.json")
examplelist = ["Weapon Name", "Strength Requirement", "Dexterity Requirement", "Intelligence Requirement", "Faith Requirement"]

print(f"\nExample List:\n\n{examplelist}\n")
print("List from JSON File:\n")
for item in filterlist:
    print(item)