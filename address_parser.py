#encoding=utf-8

# --------------------------------------------------------Libraries---------------------------------------------------------
# Standard library
import json
import codecs

# Third-party libraries


# user define module


# ------------------------------------------------------Global Variables----------------------------------------------------


# ----------------------------------------------------Class Address_Parser--------------------------------------------------
class Address_Parser(object):
    """This class is responsible for parsing chinese address based on a lexicon of chinese place name,
    """
    def __init__(self):
        self.load_lexicon()

    def load_lexicon(self):
        """Load in the lexicon from a json file whose data format likes: 
        {province: {city: [town, ...], ...}, ...}
        """
        with codecs.open('areas.json', 'r', encoding='utf-8') as input_file:
            self.lexicon = json.load(input_file)

    def longest_match(self, string, str_list):
        """Find out strings in a list which contains any successive foregoing characters of target string,
        and return the one contains most charaters of target string and the number of character.
        :Param(str) string: the target string.
        :Param(list) str_list: a list of strings.
        """
        target, index = '', 0
        max_len = max(map(len, str_list))
        for i in xrange(1, max_len):
            for item in str_list:
                if string[:i+1] in item:
                    index = i + 1
                    target = item
        return (index, target)

    def split(self, address, lexicon, level=1):
        """Split address into several parts using recursion method.
        :Param(str) address: the string of the address to be split.
        :Param(dict/list) lexicon: a dict or list of chinese place name.
        """
        (index, target) = self.longest_match(address, lexicon)
        if target:  # match palce name sucessfully.
            if isinstance(lexicon, dict):
                self.split(address[index:], lexicon[target], level+1)
                self.address[level] = target
                return True
            else:  # the end of a search path
                self.address[level] = target
                self.address[level+1] = address[index:]
                return True
        else:  # failed to match any place name at this level
            if isinstance(lexicon, dict):
                for (target, sub_lexicon) in lexicon.items():
                    if self.split(address, sub_lexicon, level+1):
                        self.address[level] = target
                        return True
                else: return False
            else:  # the end of a search path 
                self.address[level+1] = address[index:]
                return False

    def parse(self, address, level=5):
        """Parse chinese address into several parts and add the missing parts if possible.
        :Param(unicode) address: the chinses address to be parsed.
        :Param(int) level: the number of parts into which address should be parsed. 
            Default is 5, and final result like [country, province, city, town, detail],
            the part cannot be detected will be set as empty string. The first part will
            be set as 'UNKNOWN' if all the first four parts cannot be recognized.
        """
        self.address = dict.fromkeys(xrange(level), '')
        if address.startswith(u'中国'):
            address = address[2:]
        self.split(address, self.lexicon)
        # it is a chinese address and has been parsed sucessfully if the province has been detected
        if self.address[1]:
            self.address[0] = u'中国'
        else: # otherwise, this address must not been parsed sucessfully.
            self.address[0] = u'UNKNOWN'
        return [self.address[x] for x in xrange(level)]


if __name__ == '__main__':
    ap = Address_Parser()
    
    address = u'黑龙江省哈尔滨市南岗区西大直街92号'
    print ap.parse(address)

    address = u'上海市黄浦区西凌家宅路90弄33号'
    print ap.parse(address)

    address = u'丰台区南三环西路16号'
    print ap.parse(address)

    address = u'美国加利福尼亚州'
    print ap.parse(address)