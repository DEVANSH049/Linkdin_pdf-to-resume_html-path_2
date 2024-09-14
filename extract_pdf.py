import pdfplumber
import re

# Define section titles that could appear in the resume
section_titles = ['name', 'contact', 'Top skills', 'certificate', 'summary', 'experience', 'education', 'projects', 'publications']

# Regex patterns for dates, position, and location in experience
date_pattern = r'([A-Za-z]+\s\d{4})\s*-\s*(Present|\w+\s\d{4})'
location_pattern = r'\b([A-Z][a-z]+,\s*[A-Z][a-z]+)\b'

def extract_sections(text, section_titles):
    sections = {}
    section_regex = r'(?i)(' + '|'.join([re.escape(title) for title in section_titles]) + r')\b'
    section_positions = [(match.group(1), match.start()) for match in re.finditer(section_regex, text)]
    section_positions.append(("END", len(text)))
    
    for i in range(len(section_positions) - 1):
        section_title = section_positions[i][0].strip().lower()
        start_pos = section_positions[i][1]
        end_pos = section_positions[i+1][1]
        section_content = text[start_pos:end_pos].strip()
        sections[section_title] = section_content
    
    return sections

def extract_experience_data(experience_text):
    experience_blocks = re.split(date_pattern, experience_text)
    experiences = []
    
    for i in range(1, len(experience_blocks), 3):
        date_range = experience_blocks[i].strip() + ' - ' + experience_blocks[i+1].strip()
        text_block = experience_blocks[i+2]
        lines = text_block.strip().split('\n')
        role = lines[0].strip() if len(lines) > 0 else ""
        company = lines[1].strip() if len(lines) > 1 else ""
        location_match = re.search(location_pattern, text_block)
        location = location_match.group(0) if location_match else "Unknown"
        description = "\n".join(lines[2:]).strip() if len(lines) > 2 else ""
        
        experiences.append({
            'date_range': date_range,
            'role': role,
            'company': company,
            'location': location,
            'description': description
        })
    
    return experiences

def parse_resume(resume_text):
    sections = extract_sections(resume_text, section_titles)
    if 'experience' in sections:
        sections['experience'] = extract_experience_data(sections['experience'])
    
    return sections

def extract_pdf_sections(file_path):
    with pdfplumber.open(file_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    
    parsed_resume = parse_resume(full_text)
    return parsed_resume
