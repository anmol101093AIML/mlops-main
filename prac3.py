import tensorflow_datasets as tfds
train_dataset=tfds.as_numpy(tfds.load("imdb_reviews",split="train"))
imdb_sentences=[]
for item in train_dataset:
    i=0
    if i<1:
        print(item['text'])
        i+=1
