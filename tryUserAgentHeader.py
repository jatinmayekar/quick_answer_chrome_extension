import urllib.request

url = 'https://www.inc.com/nick-hobson/25-years-ago-steve-jobs-saved-apple-from-collapse-its-a-lesson-for-every-tech-ceo-today.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

req = urllib.request.Request(url, headers=headers)
try:
    response = urllib.request.urlopen(req)
    html = response.read()
    print(html)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
