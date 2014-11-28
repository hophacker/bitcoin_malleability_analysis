Data analysis of transaction malleability
=========================================


Files
-----
**TxIn.log** : CSV file 
containing  signature scripts with *OP_PUSHDATA1*, *OP_PUSHDATA2*, *OP_PUSHDATA4* (abbr. *OP_X*) inside from block height *0* to *320,000* dumped with this  [bitcoin client](https://github.com/hophacker/bitcoin_malleability). It contains *13828* rows of data. 



**result.txt**: CSV file containing signature scripts which improperly used the length field of *OP_X*. 

|OP_CODE|Rows |
|-------|-----|
|OP_PUSHDATA1|735|
|OP_PUSHDATA2|13077|
|OP_PUSHDATA4|0|
|Total|13812|

**find_mal.py**(by Scott zhang scott.likai.zhang@gmail.com ): python script transferring *TxIn.log* to *result.txt* by excuting `python find_mal.py > result.txt`

**analyze.py**(by Jianxiang Peng pjx911@gmail.com): data analysis for *results.txt* 



