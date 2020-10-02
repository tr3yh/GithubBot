# Author: tr3yh
# Date: 20201002
# Description: Github scraper/downloader by keyword
# 
from github import Github
import os

ACCESS_TOKEN = 'ENTER YOUR ACCESS TOKEN HERE'
g = Github(ACCESS_TOKEN)

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
    print(f'Found {result.totalCount} repo(s)')
# -- Print the repos found and their star rating
    for repo in result:
        print(f'{repo.clone_url}, {repo.stargazers_count} stars')
        cmd = 'git clone ' + repo.clone_url
    # -- The following two lines download all git repos found.
        #print(cmd)
        #os.system(cmd)

if __name__ == '__main__':
# -- Enter one or more keywords for this search. If you use two, results will only be shown that have both keywords.
    keywords = input('Enter keyword(s)[e.g python, malware]: ')
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)
