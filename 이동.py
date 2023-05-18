import os
import shutil

# The directory where your XML files are currently stored.
source_dir = r"C:\Users\sh010\OneDrive - 고려대학교\바탕 화면\JAS\압축해제악보"

# The directory where you want to move your XML files to.
target_dir = r"C:\Users\sh010\OneDrive\문서\GitHub\opensheetmusicdisplay.github.io\demo"

# Get a list of all XML files in the source directory.
xml_files = [f for f in os.listdir(source_dir) if f.endswith('.xml')]

# For each XML file, move it to the new directory.
for file in xml_files:
    shutil.copy(os.path.join(source_dir, file), target_dir)

print(f"Successfully copied {len(xml_files)} XML files from {source_dir} to {target_dir}")