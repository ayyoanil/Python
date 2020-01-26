import urllib.request
import requests
from bs4 import BeautifulSoup
import operator

WORDCOUNT_URL = r'https://crawler-test.com/content/word_count_100_words'
TEST_URL = r'https://crawler-test.com/links/page_with_external_links'
#TEST_IMAGE = TEST_URL + '/images/hires_bad.png'

def downloadImage(img_url):
    filename = "img.jpg"
    urllib.request.urlretrieve(img_url, filename)

def crawlWebPage(page_url):
    print(page_url)
    response = requests.get(page_url)
    sourceCode = response.text
    parsedContent = BeautifulSoup(sourceCode)
    for link in parsedContent.findAll('a'):
        print(link.get('href'))

def removeSpecialSymbols(string):
    symbols = "!@#$%^&*()_+{}:\"<>?,./;'[]-='"
    word = string;
    for i in range(0, len(symbols)):
        word = word.replace(symbols[i], "")
    return word   
        
    
    
class WordCounter():

    def setURL(self, url):
        self.req_url = url

    def CollectWords(self):
        wordList = [];
        sourceCode = requests.get(self.req_url).text
        parsedContent = BeautifulSoup(sourceCode)
        for wordelement in parsedContent.findAll('div',{'class':'large-12'}):
            for child in wordelement:
                sentence = child.string
                if sentence is not None:
                    words = sentence.lower().split()
                    for each_word in words:
                        word = removeSpecialSymbols(each_word)
                        wordList.append(word)
        return wordList;

    def countWords(self):
        wordList = self.CollectWords();
        wordCount = {};
        for word in wordList:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
        for key, val in sorted(wordCount.items(), key = operator.itemgetter(1)):
            print(key, val)
            
        



                        


counter = WordCounter()
counter.setURL(WORDCOUNT_URL)
counter.countWords()
            
        
#crawlWebPage(TEST_URL)
#downloadImage(TEST_IMAGE)
