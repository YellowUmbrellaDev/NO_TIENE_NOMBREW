import os

for root, _, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith(('.toml', '.json', '.cfg', '.txt', '.md', '.properties', '.glsl', '.vsh', '.fsh', '.csh', '.lang')):
            path = os.path.join(root, f)
            with open(path, 'rb') as file:
                content = file.read()
            
            # Replace CRLF with LF
            if b'\r\n' in content:
                content = content.replace(b'\r\n', b'\n')
                with open(path, 'wb') as file:
                    file.write(content)
                print(f"Fixed CRLF in {path}")
