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

keys = {
    'HEADER': 'templates/HEADER.html',
    'FOOTER': 'templates/FOOTER.html',
    'BODY': None
}

def parse_args():
    parser = argparse.ArgumentParser(description='Compile a document from a template and content file.')
    parser.add_argument('content', help='The content file to compile.')
    parser.add_argument('template', help='The template file to use.')
    parser.add_argument('output', help='The output directory to save the compiled document.')
    return parser.parse_args()

def parseTemplate(templatePath):
    # Searches the file for keys denoted by {{KEY}}
    # and substitutes them with the content of the
    # file specified by the key.
    with open(templatePath, 'r') as templateFile:
        template = templateFile.read()
        for key in keys:
            if key != 'BODY':
                template = template.replace('{{'+key+'}}', keys[key])
    return template

def compileDocument(contentPath, templatePath, outputPath):
    # Parse the template
    template = parseTemplate(templatePath)

    # Read the content file
    with open(contentPath, 'r') as contentFile:
        keys['BODY'] = contentFile.read()

    # Write the compiled document to the output file
    with open(outputPath, 'w') as outputFile:
        outputFile.write(template)

def main():
    args = parse_args()
    compileDocument(args.content, args.template, args.output)

if __name__ == '__main__':
    main()
