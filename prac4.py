from  tensorflow.keras.preprocessing.text import Tokenizer

sentences=["rewari is a beautful city", 'we live here']
tokenize= Tokenizer(num_words=10,oov_token= "<OOV>")

tokenize.fit_on_texts(sentences)
print(tokenize.word_index)