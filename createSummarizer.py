import os
import openai

openai.api_key = "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"


def createSummarizer(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

