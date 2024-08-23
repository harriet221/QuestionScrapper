# import subprocess
import getTopic
import getQuestion

# make csv file of topic list
# subprocess.run(["python", "getTopic.py"])
getTopic.getTopics()
url_list = getTopic.getUrls()

# make csv file of question list (only Adoption topic now)
# subprocess.run(["python", "getQuestion.py"])
for i in range(0, 3):
  getQuestion.getQuestions(url_list[i], i)