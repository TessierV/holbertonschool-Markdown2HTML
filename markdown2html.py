#!/usr/bin/env python3

""" EX: 0 Write a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
Requirements:
If the number of arguments is less than 2: print in STDERR Usage:
./markdown2html.py README.md README.html and exit 1
If the Markdown file doesn’t exist: print in STDER
Missing <filename> and exit 1
Otherwise, print nothing and exit 0 """

import sys
import os
import markdown2


def convert_markdown_to_html(markdown_file, output_file):
    with open(markdown_file, 'r') as md_file:
        markdown_content = md_file.read()
        html_content = markdown2.markdown(markdown_content)

    with open(output_file, 'w') as html_file:
        html_file.write(html_content)


def main():
    usage = "Usage: ./markdown2html.py <MarkdownFile> <OutputFile>"

    if len(sys.argv) < 3:
        print(usage_message, file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print(f"Missing <{markdown_file}>", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)


if __name__ == "__main__":
    main()
