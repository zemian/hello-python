import random, sys
capitalsByState = {
'Alabama' : 'Montgomery',
'Alaska' : 	'Juneau',
'Arizona' : 'Phoenix',
'Arkansas' : 'Little Rock',
'California' : 'Sacramento',
'Colorado' : 'Denver',
'Connecticut' : 'Hartford',
'Delaware' : 'Dover',
'Florida' : 'Tallahassee',
'Georgia' : 'Atlanta',
'Hawaii' : 'Honolulu',
'Idaho' : 'Boise',
'Illinois' : 'Springfield',
'Indiana' : 'Indianapolis',
'Iowa' : 'Des Moines',
'Kansas' : 'Topeka',
'Kentucky' : 'Frankfort',
'Louisiana' : 'Baton Rouge',
'Maine' : 'Augusta',
'Maryland' : 'Annapolis',
'Massachusetts' : 'Boston',
'Michigan' : 'Lansing',
'Minnesota' : 'Saint Paul',
'Mississippi' : 'Jackson',
'Missouri' : 'Jefferson City',
'Montana' : 'Helena',
'Nebraska' : 'Lincoln',
'Nevada' : 'Carson City',
'New Hampshire' : 'Concord',
'New Jersey' : 'Trenton',
'New Mexico' : 'Santa Fe',
'New York' : 'Albany',
'North Carolina' : 'Raleigh',
'North Dakota' : 'Bismarck',
'Ohio' : 'Columbus',
'Oklahoma' : 'Oklahoma City',
'Oregon' : 'Salem',
'Pennsylvania' : 'Harrisburg',
'Rhode Island' : 'Providence',
'South Carolina' : 'Columbia',
'South Dakota' : 'Pierre',
'Tennessee' : 'Nashville',
'Texas' : 'Austin',
'Utah' : 'Salt Lake City',
'Vermont' : 'Montpelier',
'Virginia' : 'Richmond',
'Washington' : 'Olympia',
'West Virginia' : 'Charleston',
'Wisconsin' : 'Madison',
'Wyoming' : 'Cheyenne'
}

all_capitals = list(capitalsByState.values())
max_questions = len(capitalsByState)
if len(sys.argv) > 1:
	max_questions = int(sys.argv[1])
question_num = 0
correct_count = 0
states = list(capitalsByState.keys())
random.shuffle(states)
for state in states[:max_questions]:
	question_num += 1

	capital = capitalsByState[state]
	random.shuffle(all_capitals)
	choices = all_capitals[0:4] + [capital]
	random.shuffle(choices)

	print(f"Question #{question_num}. What's the capital of {state}?")
	print(f"  Choices: {', '.join(choices)}")
	answer = input(f"  Type your answer here: ")

	if answer.lower() == capital.lower():
		print("  Correct")
		correct_count += 1
	else:
		print(f"  Wrong! The correct answer is {capital}")
score_percentange = int( (correct_count / max_questions) * 100 )
print(f"Done. You scored {score_percentange}% on your quiz")
