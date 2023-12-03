import requests
def send_to_wechat(message):
    # 这里需要替换为你的 Server酱 API 密钥
    server_chan_key = 'xxxxxxxxxxxxxxxxx'
    url = f"https://sc.ftqq.com/{server_chan_key}.send"
    data = {'text': 'GitHub Trending Today', 'desp': message}
    requests.post(url, data=data)