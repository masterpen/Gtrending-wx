from bs4 import BeautifulSoup
import requests

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

def markdown_output(url,p_content,language,stars,stars_today):
    sample_md = (
        f"- **地址:** [{url}]({url})\n"
        f"- **内容:** {p_content}\n"
        f"- **编程语言:** {language}\n"
        f"- **Star 数:** {stars}\n"
        f"- **今天的 Star 数:** {stars_today}\n\n"
    )
    return sample_md
def get_trending_repos():
    url = "https://github.com/trending"
    markdown_list=[]
    try:
        response = requests.get(url, proxies=proxies)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 处理响应
    except requests.exceptions.RequestException as e:
        # 错误处理
        print(e)
    

    # 这里的选择器需要根据页面的实际结构来定制
    repos = soup.select('.Box .Box-row')
    for i in repos:
        
        # 1. 获取 href
        # 假设所有的仓库链接都在具有特定类名的 h2 标签内
        h2_tag = i.find('h2', class_='h3 lh-condensed')
        a_tag = h2_tag.find('a') if h2_tag else None
        href_value = a_tag['href'] if a_tag else '未找到'


        # 2. 获取 <p> 标签中的内容
        p_tag = i.select_one('p.col-9.color-fg-muted.my-1.pr-4')
        p_content = p_tag.get_text(strip=True) if p_tag else '未找到'

        # 3. 获取编程语言、star 数，今天的 star 数
        div_tag = i.select_one('div.f6.color-fg-muted.mt-2')
        if div_tag:
            # 获取编程语言
            language = div_tag.find(itemprop="programmingLanguage")
            language = language.get_text(strip=True) if language else '未找到'

            # 获取 star 数
            stars = div_tag.find('a', href=lambda x: x and '/stargazers' in x)
            stars = stars.get_text(strip=True) if stars else '未找到'

            # 定位到包含 SVG 的 span 标签
            span_tag = div_tag.find('span', class_='d-inline-block float-sm-right')

            # 找到 SVG 标签
            svg_tag = span_tag.find('svg') if span_tag else None

            # 获取 SVG 标签之后的今日stars
            stars_today = svg_tag.next_sibling.strip() if svg_tag and svg_tag.next_sibling else '未找到'


        markdown_list.append(markdown_output(url+href_value,p_content,language,stars,stars_today))

    # 将所有 Markdown 文本合并为一个字符串
    final_markdown = '\n'.join(markdown_list)    
    return final_markdown

