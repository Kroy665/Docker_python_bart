
import requests
from transformers import pipeline

def getUnsplashPic(prompt):
    url = "https://api.unsplash.com/search/photos?page=1&orientation=portrait&query="+ prompt

    payload={}
    headers = {
    'Authorization': 'Client-ID MRuy_-8Fd3HWnYXZjfVQr4dqopl0FB4ZFckUENqIKLk',
    'Cookie': 'ugid=8748bbbe8d9f2e9d6d16d067443d9f305525369'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()['results'][0]['urls']['small']
    
def getFillMask(prompt):
    unmasker = pipeline('fill-mask', model='roberta-base')
    return unmasker(prompt)
    