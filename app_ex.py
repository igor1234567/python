import argparse

import requests

parser = argparse.ArgumentParser()
parser.add_argument('filename', help=' the file to write ')
parser.add_argument('--format', default='html', help='json or html, by default html')
parser.add_argument('--url', default='https://www.google.com', help='enter a url')
args = parser.parse_args()
file = open(args.filename, 'w')
res = requests.get(args.url)


if args.format == 'html':
    file.write(str(res.content))
    #print(res.content)
else:
    file.write(res.json())











