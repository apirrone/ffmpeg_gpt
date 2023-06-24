# ffmpeg_gpt

Using GPT to generate bash scripts that use ffmpeg commands to process videos.

## Installation
### From `pypi`
```bash
pip install ffmpeg_gpt
```

### From source
```bash
git clone https://github.com/apirrone/ffmpeg_gpt
cd ffmpeg_gpt
pip install .
```

## Usage examples
```bash
$ ffmpeg-gpt "flip the video input.mp4 vertically, and export all its frames in a directory named out"

Generated script: 
===========
#!/bin/bash

mkdir out
ffmpeg -i input.mp4 -vf "vflip" -q:v 1 out/frame%04d.jpg
===========
Do you want to run this script? ([Y]/n): 

```
