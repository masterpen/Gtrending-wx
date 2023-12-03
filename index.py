from send import send_to_wechat
from trending import get_trending_repos
def handler (event, context):
    message = get_trending_repos()
    send_to_wechat(message)

def main():
    message = get_trending_repos()
    send_to_wechat(message)
if __name__ == "__main__":
    main()

