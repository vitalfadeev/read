import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name="read",
     version='0.1',
     scripts=['read/read.py'] ,
     author="Vitaly Fadeev",
     author_email="vital.fadeev@gmail.com",
     description="Read various data sources: file.sqlite3, dump.xml, dump.xml.bz2, file.txt, file.json, file.json.bz2, http://",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/vitalfadeev/read",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
