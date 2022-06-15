from util import *
import requests
import re
import numpy as np
from datetime import datetime,timedelta
import arxivscraper
import pandas as pd
import sys

if __name__=="__main__":
    allName = getnamefromlink(["https://ccapp.osu.edu/people-mobile",'https://astronomy.osu.edu/people']) 
    if len(sys.argv)>1:
        if sys.argv[1] =="ASIAA":
            allName = getnamefromlinkASIAA(["https://www.asiaa.sinica.edu.tw/people/"]) 
    interested_date = datetime.today().strftime("%Y-%m-%d")
    print(interested_date)
    scraper = arxivscraper.Scraper(category='physics:astro-ph', date_from=interested_date,date_until="2100-01-27")
    output = scraper.scrape()
    delta2 = timedelta(days=5)
    created_date=(datetime.fromisoformat(interested_date)-delta2)#.strftime("%Y-%m-%d")
    cols = ( 'title', 'id', 'abstract', 'categories', 'doi', 'created', 'updated', 'authors', 'affiliation', 'url')
    df = pd.DataFrame(output,columns=cols)
    df_today = df[(np.array([datetime.fromisoformat(x) for x in df['created'].values])>created_date)&(df['updated']=="")]
    namedict = {}
    for name in allName:
        namedict[name] = create_possible_arxiv_name(name)
    localindex, localname = findlocalindex(df_today, namedict)
    local = df_today.iloc[localindex]
    local["Local Authors"]=[", ".join([y.title() for y in x]) for x in localname]
    local['title']=[x.title()for x in local['title'].values]
    local['authors']=[", ".join([y.title() for y in x]) for x in local['authors'].values]
    f = open("./html/main.html","w")
    f.write(local[['title', 'id', 'url','authors', 'Local Authors', ]].to_html(render_links=True, index=False))
    f.close()
