import os
import github as Github
import time
import datetime


Access_token="token"
g = Github.Github(Access_token)
print(g.get_user())

endtime=time.time()
starttime=endtime-86400

#query = "language:python"
for i in range(5):
    strtimestr=datetime.datetime.utcfromtimestamp(starttime).strftime('%Y-%m-%d')
    endtimestr=datetime.datetime.utcfromtimestamp(endtime).strftime('%Y-%m-%d')

    query=f"ai language:python created:{strtimestr}..{endtimestr}"
    print(query)
    endtime-=86400
    starttime-=86400
#query="ai language:python created:2020-04-01..2020-04-02"

    result=g.search_repositories(query)

    print(result.totalCount)

    print(dir(result))

    for repository in result:
        print(f"{repository.url}")
        print(dir(repository))
        print(repository.clone_url)
        os.system(f"git clone {repository.clone_url} storage/{repository.owner.login}/{repository.name}")
        break