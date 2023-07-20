import ipdb

class Anagram:
    def __init__ (self, word="the list"):
        self.word=word
        

    def match (self, alist):
        characters=[*self.word]
        new_list=[]
        for word in alist:
            if sorted(characters) == sorted([*word]):
                new_list.append(word)
        return new_list

        # ipdb.set_trace()
        
            
        
            
            
                