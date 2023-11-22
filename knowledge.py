import json
from textblob import TextBlob
from collections import defaultdict
import random

class KnowledgeBase(object):

    def __init__(self, uncommon_words, statements, limit=1000):
        self.by_keyword = defaultdict(list)
        self.no_keyword = list()
        self.uncommon_words = json.load(open(uncommon_words))
        self.keywords_for_statement = defaultdict(list)
        a = 0
        for i in open(statements):
            if random.random() > 0.1:
                continue
            chain = tuple(json.loads(i.strip()))
            statement = " ".join(chain).lower()
            blob = TextBlob(statement)
            found_keyword = False
            for word in blob.words:
                if word in self.uncommon_words:
                    self.by_keyword[word].append(chain)
                    self.keywords_for_statement[chain].append(word)
                    found_keyword = True
            if not found_keyword:
                self.no_keyword.append(chain)
            a += 1
            if a > limit:
                break

    def _uncommon_words(self, t):
        blob = TextBlob(t.lower())
        possibilities = []
        for word in map(str, blob.words):
            if word in self.by_keyword:
                possibilities.append(word)
        return possibilities
    
    def query(self, t):
        possibilities = self._uncommon_words(t)
        if possibilities:
            response_word = random.choice(possibilities)
            source = self.by_keyword[response_word]
            response = random.choice(source)
        else:
            response_word = None
            source = self.no_keyword
            response = random.choice(source)
            self.no_keyword.remove(response)            
        for word in self.keywords_for_statement[response]:
            self.by_keyword[word].remove(response)
            if not self.by_keyword[word]:
                del self.by_keyword[word]
        return response_word, response
        
