import text_reader_sub
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "exception detected"

if __name__ == "__main__":
    url = "https://grader.mathworks.com/courses/39818-mat188-2022f-pra-all-sections/problems/872528-loading-and-previewing-tabular-data/solutions/new"
    fileobject = open("html.txt", 'w')
    fileobject.write(getHTMLText(url))

header_list = ['a', 'body', 'script', 'title', 'span']
for val in header_list:
  read = text_reader_sub.reading(val)
  read.get_text()
