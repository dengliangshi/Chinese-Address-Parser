# Chinese Address Parser
This moudle is responsible for parsing chinse address based on a lexicon of chinese place name. Default, a given chinese address will be parsed into five parts, i.e. third level address.

## Usage
```
from address_parser import Address_Parser

ap = Address_Parser()
address = u'黑龙江省哈尔滨市南岗区西大直街92号'
print ap.parse(address)

address = u'上海市黄浦区西凌家宅路90弄33号'
print ap.parse(address)

address = u'丰台区南三环西路16号'
print ap.parse(address)

address = u'美国加利福尼亚州'
print ap.parse(address)
```
Output
```
[u'中国', u'黑龙江省', u'哈尔滨市', u'南岗区', u'西大直街92号']

[u'中国', u'上海市', u'上海市', u'黄浦区', u'西凌家宅路90弄33号']

[u'中国', u'北京市', u'北京市', u'丰台区', u'南三环西路16号']

[u'UNKNOWN', u'', u'', u'', u'美国加利福尼亚州']
```

## Acknowledge
The original lexicon of chinese place name is here: [https://github.com/cnluzhang/chinaddress](https://github.com/cnluzhang/chinaddress)

## License
MIT License
