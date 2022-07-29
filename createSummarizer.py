from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def createSummarizer(article):
    return summarizer(article, max_length=130, min_length=30, do_sample=False)
