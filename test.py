# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')

from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi

import re

def pinyin2hanzi(pinyin):

    dagparams = DefaultDagParams()
    hmmparams = DefaultHmmParams()

    pa = re.compile("[^aoeiuv]?h?[iuv]?(ai|ei|ao|ou|er|ang?|eng?|ong|a|o|e|i|u|ng|n)?")
    ans = []
    while len(pinyin) != 0:
        ma = pa.match(pinyin)
        subPinyin = ma.group()
        ans.append(subPinyin)
        findLen = len(subPinyin)
        pinyin = pinyin[findLen:]
    print (ans)
    result = dag(dagparams, ans)
    #result = viterbi(hmmparams,ans)
    candinate = []
    for item in result:
        candinate.append(''.join(item.path))
    return candinate

if __name__ == "__main__":
    while 1:
        pinyin = raw_input()
        ans = pinyin2hanzi(pinyin)
        for a in ans:
            print (a)



