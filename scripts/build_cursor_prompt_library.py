#!/usr/bin/env python3
import os
import json
import re

front_re = re.compile(r'^---\n(.*?)\n---\n', re.S)


def parse_front_matter(text):
    match = front_re.match(text)
    data = {}
    rest = text
    if match:
        front = match.group(1)
        rest = text[match.end():]
        # extract fields using regex
        name_m = re.search(r'^name:\s*(.*)', front, re.M)
        if name_m:
            data['name'] = name_m.group(1).strip()
        desc_m = re.search(r'^description:\s*(.*)', front, re.M)
        if desc_m:
            data['description'] = desc_m.group(1).strip()
        color_m = re.search(r'^color:\s*(.*)', front, re.M)
        if color_m:
            data['color'] = color_m.group(1).strip()
        tools_m = re.search(r'^tools:\s*(.*)', front, re.M)
        if tools_m:
            data['tools'] = [t.strip() for t in tools_m.group(1).split(',')]
    return data, rest


def read_agent(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    data, rest = parse_front_matter(text)
    if 'name' not in data:
        data['name'] = os.path.splitext(os.path.basename(file_path))[0]
    prompt = rest.strip()
    prompt = re.sub(r"root@.*$", "", prompt).rstrip()
    data['prompt'] = prompt
    data['path'] = file_path
    return data

agents = []
for root, dirs, files in os.walk('.'):
    for fname in files:
        if fname.endswith('.md') and fname != 'README.md':
            path = os.path.join(root, fname)
            agents.append(read_agent(path))

agents.sort(key=lambda x: x.get('name'))

output = {'prompts': agents}

os.makedirs('cursor', exist_ok=True)
with open('cursor/prompt_library.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(agents)} prompts to cursor/prompt_library.json")
