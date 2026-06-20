import os

from dotenv import load_dotenv

try:
    load_dotenv()
except RuntimeError:
    raise RuntimeError(
        f"env not loaded"
    )

file_directory = os.getenv("FILE_DIRECTORY")
file_upload_permissions = os.getenv("FILE_UPLOAD_PERMISSIONS")
file_upload_folder = os.getenv("FILE_UPLOAD_FOLDER")
file_parse_permissions = os.getenv("FILE_PARSE_PERMISSIONS")
file_parse_folder = os.getenv("FILE_PARSE_FOLDER")