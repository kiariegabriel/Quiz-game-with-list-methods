questions=['What\'s the capital city of Kenya? ', 'What\'s the largest county in Kenya? ']
answers=['Nairobi','Turkana']
count=0
for i in range(len(questions)):
	ans=input(questions[i])
	if ans.lower()==answers[i].lower():
		count+=1
		print('Correct! You got question ', i+1, ' of 2 correct')
	else:
		print('Wrong. The answer is ', answers[i],'. You got question ', i+1,' of 2 wrong.')
print('You got ', count, ' out of 2 questinon(s) right!')