import json

file = open("/home/lee/TestProgramming/Pythontests/chatgpt/chatgptResponse.json")

data = json.load(file)
#print(data['choices'][0]['message']['content'])

file.close()

f = open("/home/lee/TestProgramming/Pythontests/chatgpt/batteryTester.json", "w")
f.write(data['choices'][0]['message']['content'])
f.close()