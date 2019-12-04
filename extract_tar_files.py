# pip install patool
import patoolib as pt
import os

# Change directory to where your file is
os.chdir("C:\\Users\\your_user\\Desktop")
print(os.listdir())
# Extract .tar file into "unpack" folder
pt.extract_archive("your_file.tar", outdir="unpack")
print(os.listdir("unpack"))