import requests
url='https://gitee.com/api/v5/search/repositories?q=language:python&sort=stars'
headers={'Accept':'application/vnd.gitee.v3+json'}
r=requests.get(url,headers=headers)
print(f'Status code : {r.status_code}')
response_dict=r.json()
print(response_dict.keys())