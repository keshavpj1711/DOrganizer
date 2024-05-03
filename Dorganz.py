# Precautions 
# while using this script make sure the download folder itself exists

# Work Around 
# You can easily add more and more categories as much as you like 
# The script itself is pretty easy to understand 
# So adding more folders and file extensions should not be a problem
# Basic logic of the script is properly mentioned in the comments

# Enjoy your day!!

# This module helps us to to os level tasks which can also be done as a user.
import os

# Asking for your username
username = "nightfury"

# Defining folder paths
download_folder = f"/home/{username}/Downloads"
image_folder = f"{download_folder}/images"
video_folder = f"{download_folder}/videos"
audio_folder = f"{download_folder}/audio"
zips_folder = f"{download_folder}/zips"
document_folder = f"{download_folder}/documents"
others_folder = f"{download_folder}/others"

# Creating folders if missing 
def create_if_missing(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        # print(f"Folder Created: {folder_path}")

# Calling the functions
create_if_missing(image_folder)
create_if_missing(video_folder)
create_if_missing(audio_folder)
create_if_missing(zips_folder)
create_if_missing(document_folder)
create_if_missing(others_folder)

# Looping through files in download folder
for filename in os.listdir(download_folder):
    
    # Getting the files path
    filepath = os.path.join(download_folder, filename)

    # Checking file types and sorting
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif", ".webp", ".cr2", ".crw", ".nef", ".pef", "heif", ".psd", ".ai")):     
        # Moving image files
        os.rename(filepath, os.path.join(image_folder, filename))

    elif filename.endswith((".mp4", ".avi", ".mkv", ".mov", ".flv", ".webm", ".f4v", ".wmv", ".avchd")):
        os.rename(filepath, os.path.join(video_folder, filename))

    elif filename.endswith((".pdf", ".docx", ".txt", ".xml", ".pptx", ".xlsx", ".csv")):
        os.rename(filepath, os.path.join(document_folder, filename))

    elif filename.endswith((".mp3", ".wav", ".flac", ".aac", ".wma")):
        os.rename(filepath, os.path.join(audio_folder, filename))

    elif filename.endswith((".rar", ".iso", ".zip", ".7z", ".gz", ".bz2", ".bz")):
        os.rename(filepath, os.path.join(zips_folder, filename))

    
    # Logic for pushing items to other folder
    else:
        if os.path.isdir(filepath):
            # print(f"This is a folder: {filepath}")
            pass

        else:
            # So if the the filename is a regular file it goes to others_folder
            # But if the filename is a folder its untouched
            os.rename(filepath, os.path.join(others_folder, filename))            

    # print("Files Organized")