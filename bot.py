def question():
	print('Ваш вопрос: ')
	question = input()
	return question

def findAnswer(str):
	dataset = []
	with open('dialogues.txt', encoding='utf-8') as f:
		content = f.read()
	blocks = content.split('\n')
	for block in blocks:
		replicas = block.split('\\')
		pair = [replicas[0], replicas[1]]
		dataset.append(pair)
	
	X_text = []
	y = []

	for question, answer in dataset:  # Вопросы в хтекст, ответы в у
		X_text.append(question)			# Прошел по dataset первое значение в хтекст
		y += [answer]					# следующее в у

	count = 0	
	

	for q in X_text:
		if q == str:
			print('Ответ бота: ' + y[count])
			break
		count += 1
		if count == len(X_text):   # Если прошелся по всем ответам и не нашел то
			addQA(tryAnswer(), str) # вызываем добавляем ответ на такой вопрос

def addQA(answer1, question1):
	a = f"\n{question1}\{answer1}"
	with open('dialogues.txt', "a", encoding='utf-8') as f:
		f.write(a)

def tryAnswer():
	print('Бот еще не сталкивался с таким вопросом, что он должен ответить на него?: ')
	tryAns = input()
	return tryAns

k = 0
while k < 20:
	findAnswer(question())
	k += 1
