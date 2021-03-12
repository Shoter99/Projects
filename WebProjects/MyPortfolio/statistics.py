import matplotlib.pyplot as plt
import numpy as np
from app import Questions
def loopThroughAnswers(gender):
	answers = []
	ans= []
	allAnswers = []
	for question in gender:
		allAnswers.append([question.q1, question.q2, question.q3, question.q4, question.q5, question.q6, question.q7, question.q8, question.q9, question.q10, question.q11])
	print(allAnswers)
	for i in range(11):
		for a in allAnswers:
			print('A= '+str(a)+str(i))
			ans.append(a[i])
		answers.append(sorted(ans))
		ans= []
	print(ans)
	print(answers)
	return answers
def displayAnswers(gender, name):
	i=0
	for ans in gender:
		i+=1
		plt.hist(ans)
		plt.xlabel(f"Odpowiedzi {name} na pytanie "+str(i))
		plt.show()
		plt.clf()

def wyniki():
	male = Questions.query.filter_by(gender="male").all()
	displayAnswers(loopThroughAnswers(male), "mężczyzn")
	female = Questions.query.filter_by(gender="female").all()
	displayAnswers(loopThroughAnswers(female), "kobiet")
	return redirect(url_for("ankieta"))
wyniki()