import re

NAME_PATTERN = re.compile(r"Name:\s*(.+)", re.IGNORECASE)
EMAIL_PATTERN = re.compile(r"Email:\s*([\w.-]+@[\w.-]+\.\w+)", re.IGNORECASE)
PHONE_PATTERN = re.compile(r"Phone:\s*(\d{10})",re.IGNORECASE)
COLLAGE_PATTERN = re.compile(r"Collage:\s*(.+)",re.IGNORECASE)
SKILLS_PATTERN = re.compile(r"Skills: \s*(.+)",re.IGNORECASE)

def get_email(lines):
    for l in lines:
        match = re.search(EMAIL_PATTERN, l)
        if match:
            return match.group(1)
    return None

def get_phone(lines):
    for l in lines:
        match = re.search(PHONE_PATTERN,l)
        if match:
            return match.group(1)
    return None

def get_name(lines):
    for l in lines:
        match = re.search(NAME_PATTERN,l)
        if match:
            return match.group(1)
    return None

def get_collage(lines):
    for l in lines:
        match = re.search(COLLAGE_PATTERN,l)
        if match:
            return match.group(1)
    return None


def get_skills(lines):
    for l in lines:
        match = re.search(SKILLS_PATTERN,l)
        if match:
            return match.group(1)
    return None


