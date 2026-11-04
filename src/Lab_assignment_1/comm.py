import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")

model.save("glove50/glove_50_fast.wordvectors")

print("GloVe 50 model downloaded and saved.")