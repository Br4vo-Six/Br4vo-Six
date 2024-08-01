import markdown

""" This is a simple python script that "compiles" the markdown to html
"""

with open('problem.md', 'r') as f:
    problem = markdown.markdown(f.read())
with open('solution.md', 'r') as f:
    solution = markdown.markdown(f.read())
with open('architecture.md', 'r') as f:
    arch = markdown.markdown(f.read())
with open('team.md', 'r') as f:
    team = markdown.markdown(f.read())
# Convert markdown to HTML
html_content = markdown.markdown(text)

# Read the HTML template
with open('template/index.template.html', 'r') as f:
    template = f.read()

# Insert the HTML content into the template
html_page = template.replace('{{ problem }}', problem).replace('{{ solution }}', solution).replace('{{ architecture }}', arch).replace('{{ team }}', team)

# Write the final HTML to a file
with open('index.html', 'w') as f:
    f.write(html_page)
