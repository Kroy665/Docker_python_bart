

import openai

openai.api_key = "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"

def openAiFunc(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response['choices'][0]['text']

def openAiFunc2(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response['choices'][0]['text']




# test = openAiFunc("This is a test")
# print(test)
