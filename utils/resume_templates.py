def generate_html_resume(data):
    html_template = """
    <html>
    <head><title>Resume</title></head>
    <body>
        <h1>{name}</h1>
        <h2>Contact</h2>
        <p>{contact}</p>
        <h2>Skills</h2>
        <p>{top_skills}</p>
        <h2>Experience</h2>
        <p>{experience}</p>
        <h2>Education</h2>
        <p>{education}</p>
        <h2>Projects</h2>
        <p>{projects}</p>
        <h2>Publications</h2>
        <p>{publications}</p>
    </body>
    </html>
    """
    return html_template.format(**data)
