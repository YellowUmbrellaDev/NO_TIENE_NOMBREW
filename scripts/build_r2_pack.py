import os
import hashlib
import boto3
import urllib.parse
from pathlib import Path

# Configuraciones base de Cloudflare S3
ENDPOINT = os.environ.get('AWS_ENDPOINT_URL')
ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET = os.environ.get('BUCKET_NAME')
CDN_BASE = os.environ.get('CDN_URL').rstrip('/')

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def create_toml(filepath, filename, relative_path, url, sha256, side):
    toml_path = filepath.with_suffix('.pw.toml') if filepath.suffix else filepath.with_name(f"{filepath.name}.pw.toml")
    toml_content = f"""name = "{filename}"
filename = "{filename}"
side = "{side}"

[download]
url = "{url}"
hash-format = "sha256"
hash = "{sha256}"
"""
    with open(toml_path, "w", encoding="utf-8") as f:
        f.write(toml_content)
    return toml_path

def main():
    s3 = boto3.client('s3',
        endpoint_url=ENDPOINT,
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name='auto'
    )

    folders_to_process = {
        'config': 'both',
        'shaderpacks': 'client',
        'resourcepacks': 'client',
        'mods': 'both'
    }

    allowed_raw_extensions = ['.txt', '.json', '.cfg', '.properties', '.zip', '.jar', '.glsl', '.vsh', '.fsh', '.csh', '.lang']

    for target_dir, side in folders_to_process.items():
        base_path = Path(target_dir)
        if not base_path.exists():
            continue

        for root, _, files in os.walk(base_path):
            for file in files:
                filepath = Path(root) / file
                
                # Omitir .pw.toml que ya están creados por modrinth/curseforge
                if file.endswith('.pw.toml'):
                    continue

                if filepath.suffix in allowed_raw_extensions or target_dir == 'config':
                    print(f"Procesando: {filepath}")
                    
                    # 1. Hashing
                    file_hash = calculate_sha256(filepath)

                    # 2. Generar Object Key y subir a R2
                    # Ejemplo: modpack/config/xaero/default.json
                    posix_path = filepath.as_posix()
                    object_key = f"modpack/{posix_path}"
                    
                    try:
                        s3.upload_file(str(filepath), BUCKET, object_key)
                        print(f"Subido a R2: {object_key}")
                    except Exception as e:
                        print(f"Error subiendo {filepath}: {e}")
                        continue

                    # 3. Crear archivo TOML de Packwiz
                    url_encoded_path = urllib.parse.quote(object_key)
                    final_url = f"{CDN_BASE}/{url_encoded_path}"
                    create_toml(filepath, file, posix_path, final_url, file_hash, side)
                    
                    # 4. Eliminar el archivo original para que Packwiz no lo tome duplicado o como loose file
                    os.remove(filepath)

if __name__ == "__main__":
    main()
