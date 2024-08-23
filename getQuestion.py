import requests
from bs4 import BeautifulSoup
import csv

# question version
def getQuestions(url, n):
  
  # url = "https://www.eslconversationquestions.com/adoption/"
  
  response = requests.get(url)
  
  soup = BeautifulSoup(response.content, "html.parser")
  
  topic = soup.find("article", class_="category-topics").find("header")
  questions = soup.find("article", class_="category-topics").find("div", class_="entry-content").find_all("p")[:-1]
  
  topicName = topic.text[:-1]
  
  question_list = []
  i = 1
  for question in questions:
    adoptionQ = question.text
    
    question_data = {
      "id":i,
      "topic":topicName,
      "question":adoptionQ
    }
    question_list.append(question_data)
    i += 1
  
  # print(question_list)
  
  filename = f"questionSample{n+1}.csv"
  file = open(filename, "w")
  writer = csv.writer(file)
  writer.writerow(question_list[0].keys()) # id, topic, question
  for q in question_list:
    writer.writerow(q.values())