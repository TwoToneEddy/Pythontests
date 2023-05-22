
import json
file = open("/home/lee/TestProgramming/Pythontests/chatgpt/questionTemplate.json")

jdata = json.load(file)

with open('/home/lee/TestProgramming/Pythontests/chatgpt/barclaysspec.txt', 'r') as file:
    question = file.read().replace('\n', '')

jdata['messages'][0]['content'] = question

json_object = json.dumps(jdata, indent = 4)


f = open("/home/lee/TestProgramming/Pythontests/chatgpt/question.json", "w")
f.write(json_object)
f.close()