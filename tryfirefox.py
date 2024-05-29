from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import requests

def scrape_article_text(url):
    req = Request(
        url=url, 
        headers={'User-Agent': 'Mozilla/6.0'}
    )
    html = urlopen(req).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    #print(text)

    return text


#url = "https://apnews.com/article/israel-palestinians-hamas-war-news-05-27-2024-7b743a848ef8bfbe69a9659a4a5dd047"
#scrape_article_text(url)

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json['url']
    article_text = scrape_article_text(url)
    #print(article_text)
    #return jsonify({'article_text': article_text})

    chaturl = "http://localhost:11434/api/chat"
    data = {
    "model": "llama3",
    "messages": [
        {
            "role": "system",
            "content": 
                'Given the title and link to an article, provide a short, terse, and precise answer to the question or topic posed in the title. '
                'Extract only the core information necessary to directly address the topic. Ensure the answer is concise and clear inp point structured format. '
                'Example Response: '
                'Title: "25 Years Ago, Steve Jobs Saved Apple From Collapse - It is a Lesson for Every Tech CEO Today" '
                'Core Answer: '
                'Steve Jobs saved Apple by streamlining the product line, securing a $150 million partnership with Microsoft, '
                'focusing on customer experience, and unifying company goals.' 
        },
        {
            "role": "user",
            "content": 'Hi, the current tab URL is: ' + url + 'and the article text is: ' + article_text
        }
    ],
    "stream": False
    }

    response = requests.post(chaturl, json=data)
    response_output = response.json()['message']['content']
    print(response_output)
    return jsonify({'output': response_output})

if __name__ == '__main__':
    app.run()