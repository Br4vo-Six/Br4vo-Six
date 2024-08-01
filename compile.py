import markdown

""" This is a simple python script that "compiles" the markdown to html
"""

with open('content/problem.md', 'r') as f:
    problem = markdown.markdown(f.read())
with open('content/solution.md', 'r') as f:
    solution = markdown.markdown(f.read())
with open('content/architecture.md', 'r') as f:
    arch = markdown.markdown(f.read())
with open('content/team.md', 'r') as f:
    team = markdown.markdown(f.read())

# Read the HTML template
with open('template/index.template.html', 'r') as f:
    template = f.read()

# Insert the HTML content into the template
html_page = template.replace('{{ problem }}', problem).replace('{{ solution }}', solution).replace('{{ architecture }}', arch).replace('{{ team }}', team)

# Write the final HTML to a file
bundlepath = "./compiled"
if not os.path.exists(bundlepath):
    os.makedirs(bundlepath)
with open('./compiled/index.html', 'w') as f:
    f.write(html_page)
