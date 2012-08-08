import json
import requests

token = {'public_token': "m8cjz7_DBE2BB80DC99CBEDC5986881570177", 'public_auth': "1234567"}

document_route = "http://api.daqtak.com/document/"

return_options = ["raw_text",
                  "clean_text",
                  "word_count",
                  "raw_word_frequencies",
                  "word_frequencies",
                  "sentence_count",
                  "tokenize",
                  "tokenize_unique",
                  "simple_bigrams",
                  "simple_trigrams",
                  "sentences",
                  "tokenize_sentences",
                  "stemmed",
                  "stemmed_unique",
                  "pos",
                  "language_information"]

#process a document
f = open('documents/my_document.txt','r')
my_document = f.read()

for option in return_options:

    post_data = {'document_tag': 'my_document',
                 'document': my_document,
                 'return': option}
    
    post_data.update(token)
    r = requests.post(document_route, data = post_data)
    output = r.json
    o = open("output/{}.txt".format(option), 'w')
    o.write(str(output))
