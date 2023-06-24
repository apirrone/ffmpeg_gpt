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

### Set yout openai api key as an environment variable (put it in your .bashrc or equivalent for convenience)
```bash
export OPENAI_API_KEY=<your_api_key>
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
