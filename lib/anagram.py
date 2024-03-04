class Anagram:
    def __init__(self, word):
        self.word = word

    def check_anagram(self, word2):
        list1 = [*self.word]
        list2 = [*word2]
        
        if sorted(list1) == sorted(list2):
            return True
        else:
            return False

    def match(self, list):
        new_list = []
        i = 0

        while i < len(list):
            if self.check_anagram(list[i]):
                new_list.append(list[i])
            i+=1

        return new_list
    
test_anagram = Anagram("bread")

test_anagram.check_anagram("dreab")