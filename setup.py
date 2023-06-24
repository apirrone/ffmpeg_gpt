from os import path
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ffmpeg-gpt",
    version="0.1.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "openai==0.27.8"
    ],
    entry_points={
        "console_scripts": [
            "ffmpeg-gpt = ffmpeg_gpt:main",
        ]
    },
    author="Antoine Pirrone",
    author_email="antoine.pirrone@gmail.com",
    url="https://github.com/apirrone/ffmpeg_gpt",
    description="Use GPT to generate ffmpeg commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
