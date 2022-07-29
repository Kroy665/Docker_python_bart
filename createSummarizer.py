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

