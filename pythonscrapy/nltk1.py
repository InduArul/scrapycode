from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tokenize import sent_tokenize, word_tokenize
document  = """The new system will be used to manage Sembcorp's global businesses and assets across 14 countries the company has utilities operations in.,SINGAPORE: Sembcorp launched its new global asset management system on Friday (Mar 31), enabling the use of predictive analytics in its utilities plant operations.,The new system will be used to manage Sembcorp's global businesses and assets in countries the company has utilities operations in.,Launched across the Group's operations in Singapore, India, Oman, the UAE and UK in 2016, it consolidates operational data on a real-time basis to ensure optimal plant performance, the company said. Its functions include benchmarking plant performance data and providing automated alerts of abnormal occurrences. ,The system, which is housed with the Sembcorp Technology & Innovation Centre on Jurong Island, also aims to reduce unplanned outages by early detection of equipment problems and maximise efficiency by identifying and enhancing existing processes, Sembcorp added. ,Speaking at the launch event, Parliamentary Secretary for Trade and Industry Low Yen Ling urged companies to adopt digital technology to transform their operations, citing opportunities in manufacturing and infrastructure sectors to increase operational efficiency, raise labour productivity and strengthen overall competitiveness.,Ms Low said that harnessing digital opportunities "will also create good job opportunities for Singaporeans working as system architects, data analysts and project engineers".,Sembcorp Industries Group President and CEO Tang Kin Fei said it was "exceptionally important for companies to leverage the full potential of technological solutions" in the current digital era.,The launch of the new system is part of Sembcorp's continued investment in platforms and partnerships that enable the group to "strengthen (its) technological edge and stay globally competitive", Mr Tang added. ,It looks like the email address you entered is not valid.,CopyrightÂ© Mediacorp 2019. Mediacorp Pte Ltd. All rights reserved."""
#print (ne_chunk(pos_tag(word_tokenize(sentence))))
sentences  = sent_tokenize(document )

data = []
for sent in sentences:
    data = data + pos_tag(word_tokenize(sent))
 
for word in data: 
    if 'NNP' in word[1]: 
        print(word)
    
