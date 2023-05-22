from model import Hashmap
import os
import hashlib
import click

@click.command()
@click.argument('dir')
def scan_directory(dir):
    hash_map = Hashmap(200)
    duplicates = []
    for root, dirnames, files in os.walk(dir):
        for file_name in files:
            path = os.path.join(root, file_name)
            file_hash = get_hash(path)

            if file_hash in hash_map:
                
                duplicates.append([file_hash, path])
            else:
                hash_map.add(file_hash, path)

    if duplicates:
        click.echo("Duplicate files found:")
        for file_path in duplicates:
            click.echo(file_path)
    else:
        click.echo("No duplicate files found.")


def get_hash(file_path):
    chunk_size = 4096
    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()
    
# dir = './files'
# unique_files, duplicate_files = scan_directory(dir)

# print("Unique files:")
# for file_name, path in unique_files:
#     print(f"file name {file_name}, file path {path}")

# print("\nDuplicate files:")
# for file_path in duplicate_files:
#     print(file_path)

if __name__ == '__main__':
    scan_directory()
