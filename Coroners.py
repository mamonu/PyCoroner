import urllib2
import subprocess
import re
import pandas
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk import Tree

# def download_file(download_url):
#     response = urllib2.urlopen(download_url)
#     file = open("document.pdf", 'wb')
#     file.write(response.read())
#     file.close()
#     print("Completed")
#
#
# download_file("http://www.courts.sa.gov.au/CoronersFindings/Lists/Coroners%20Findings/Attachments/698/MILERA-ASHFORD%20Bailey%20Trent%20Richard.pdf")
#

def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue
    return continuous_chunk



def get_ne_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    return chunked




data = []

with open ("docu.txt", "r") as myfile:
   data.append(myfile.read())

df = pandas.DataFrame(data)

pandas.set_option('max_colwidth',-1)






txt = str(df[0])

print txt

txt = txt.decode('utf-8').strip('\n\n')
txt = txt.rstrip('\n\n')


print txt