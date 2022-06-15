import requests
import re
import numpy as np
def getnamefromlink(linklist):
    allName = []
    for link in linklist:
        res = requests.get(link,verify=False, timeout=10)
        allNamein = re.findall(r'"views-field-field-first-name">\s*(.*?)\s*</a>', res.text)
        allName.extend([" ".join(re.split(' +', name)) for name in allNamein])
    allName = np.unique(allName)
    return allName

def create_possible_arxiv_name(name):
    result = re.search(r'\((.*?)\)',name)
    name = name.split("(")[0]
    name = name.lstrip().rstrip()
    val = re.split(' +', name)
    allpossible =  ["^"+r" +[a-zA-Z]*\W* *".join([val[0], val[-1]])+"$","^"+r" *[a-zA-Z]*\W* +".join([val[0][0]+"\.", val[-1]])+"$"]
    
    if result is not None:
        allpossible.extend(["\W*[a-zA-Z]*\W*"+result.group(1)])
    return allpossible

def findlocalindex(df_today, namedict):
    localindex = []
    localname = []
    for i, x in enumerate(df_today['authors'].values):#
        hasmatched=False
        nameall = []
        for name in namedict.keys():
            for namein in namedict[name]:
                mat = re.compile(namein, re.IGNORECASE)
                for y in x:
                    if mat.search(y) != None:
                        hasmatched=True
                        nameall.append(name)

        if hasmatched:
            localindex.append(i)
            localname.append(np.unique(nameall))
    return localindex, localname
