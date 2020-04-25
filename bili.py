import requests
import json
import time

url = 'https://oapi.dingtalk.com/robot/send?access_token=4982fc1deea6f59fc3d4f3a97b1d6e8e09ccd912039f1759d356eebacdd895da'
# 半佛，朱一旦，大骚,罗翔说刑法,毕导THU,何同学
bili_ids = ['37663924','437316738','390461123','517327498','254463269','163637592','488609381']
yesterday = time.time()-60*60*24*2  # 1天前

obj = {
    "msgtype": "text", 
    "text": {
        "content": 'B站:'+time.strftime('%Y-%m-%d',time.localtime(time.time())), 
    }
}
requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps(obj)
)



for bid in bili_ids:
    bili_url = 'https://api.bilibili.com/x/space/arc/search?mid='+bid+'&pn=1&ps=25&jsonp=jsonp'

    r = requests.get(bili_url)
    videos = r.json()['data']['list']['vlist']
    for video in videos:
        if(video['created']>yesterday):
            print(video['title'],video['description'],video['author'])
            print(video['created'])
            obj = {
                "msgtype": "link", 
                "link": {
                    "text": video['description']+'B站', 
                    "title": video['title'], 
                    "picUrl": 'http:'+video['pic'], 
                    "messageUrl": "https://www.bilibili.com/video/av%s" %(video['aid'])
                }
            }
            requests.post(url,
                headers={'Content-Type': 'application/json'},
                data=json.dumps(obj)
            )
