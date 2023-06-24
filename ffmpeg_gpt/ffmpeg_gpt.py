import openai

pre_preprompt = """
You are a bash and ffmpeg expert, you never make mistakes. 
Write a bash script that uses ffmpeg to perform the following actions.
Do not explain yourself, just write the script.
Be sure the script is working. 
If not specified, the input file is named input.mp4 and the output file is named output.mp4.
"""

preprompt_normal = (
    pre_preprompt
    + """
Here are the actions requested : 


"""
)

preprompt_rerun = """
The script you wrote is not working. Here is a full history with the original prompt, the script you wrote and the error message.
Fix your script, do not explain, do not apologize, just write a new script.


"""


def get_bash_script(prompt, model="gpt-4"):
    prompt = preprompt_normal + prompt

    res = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content


def rerun(prompt, script, stdout, model="gpt-4"):
    prompt = preprompt_rerun
    prompt += """
    Original prompt : 

    """
    prompt += prompt
    prompt += """
    Script you wrote :

    """
    prompt += script
    prompt += """
    Error message :

    """
    prompt += stdout

    res = openai.ChatCompletion.create(
        model=model, messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content
