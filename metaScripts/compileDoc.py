# Python Script to grab content from a file
# and compile it using the provided template
# and save it to the output file.

# Arguments:
# - Input File
# - Template File
# - Output Directory

import os
import sys
import argparse
import html





def parse_args():
    parser = argparse.ArgumentParser(description='Compile a document from a template and content file.')
    parser.add_argument('content', help='The content file to compile.')
    parser.add_argument('template', help='The template file to use.')
    parser.add_argument('output', help='The output directory to save the compiled document.')
    return parser.parse_args()

def returnHtml(path):
    with open(path,'r',encoding='utf-8') as file:
        data = file.read()
    # Sanitize it
    # data =  html.escape(data)
    return data

def compileDocument(templatePath, outputPath, keys):
    # Parse the template

    # Read the template file
    with open(templatePath, 'r', encoding='utf-8') as templateFile:
        template = templateFile.read()

    # Now open the template doc, search for keys
    # and replace with the file content of the
    # path in the keys dictionary
    for key, path in keys.items():
        # Get the content of the file
        content = returnHtml(path)
        # Replace the key with the content
        template = template.replace(f'{{{key}}}', content)





    # Write the compiled document to the output file
    with open(outputPath, 'w') as outputFile:
        outputFile.write(template)

def main():
    args = parse_args()

    keys = {
        'HEADER': 'templates/HEADER.html',
        'FOOTER': 'templates/FOOTER.html',
        'BODY': args.content,
    }

    compileDocument(args.template, args.output,keys)

if __name__ == '__main__':
    main()
