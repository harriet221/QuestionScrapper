import requests
from bs4 import BeautifulSoup
import csv

url_list = []
def getUrls():
  return url_list
  
# topic version
def getTopics():
  url = "https://www.eslconversationquestions.com/english-conversation-questions/topics/"
  
  response = requests.get(url)
  
  soup = BeautifulSoup(response.content, "html.parser")
  
  topics = soup.find("article", class_="mv-content-wrapper").find("div", class_="entry-content").find_all("p")[1:-1]
  
  topic_list = []
  i = 1
  
  for topic in topics:
    url = topic.find("a")["href"]
    topic_data = {
      "id": i,
      "topic": topic.text,
      "url": url
    }
    topic_list.append(topic_data)
    i += 1
    url_list.append(url)
  
  # print(topic_list)
  
  file = open("topics.csv", "w")
  writer = csv.writer(file)
  writer.writerow(topic_list[0].keys()) # id, topic, url
  for t in topic_list:
    writer.writerow(t.values())
  