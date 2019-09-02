class Frame:
	def __init__(self, input_item):
		self.input = input_item
		self.digit_1 = 0
		self.digit_2 = 0
		self.bonus_1 = 0
		self.bonus_2 = 0

		self.parse_input()

	def __repr__(self):
		return "{}".format([self.input, 
			self.digit_1, self.digit_2, self.bonus_1, self.bonus_2])

	def is_strike(self):
		return self.input == 'X'

	def is_spare(self):
		return self.input.endswith('/')

	def parse_input(self):

		def to_score(ch):
			if ch == 'X' or ch == '/':
				return 10
			else:
				return int(ch)

		clean_input = self.input
		clean_input = clean_input.replace('-', '0')
		clean_input = clean_input.replace('S', '')
		#print("debug: parsing {}".format(clean_input))
		
		self.digit_1 = to_score(clean_input[0])
		if len(clean_input) == 2:
			self.digit_2 = to_score(clean_input[1])
			if clean_input[1] == '/':
				self.digit_2 = 10 - self.digit_1
		elif len(clean_input) == 3:
			self.digit_2 = to_score(clean_input[1])
			self.bonus_1 = to_score(clean_input[2])

	def score(self):
		return self.digit_1 + self.digit_2 + self.bonus_1 + self.bonus_2

def bowling_score(score_input):
	frame_list = []
	input_list = score_input.split(' ')
	for input_item in input_list:
		frame = Frame(input_item)
		frame_list.append(frame)

	# Calculate bonus points
	list_size = len(frame_list)
	for i in range(list_size):
		frame = frame_list[i]
		next_frame = None
		if i + 1 < list_size:
			next_frame = frame_list[i + 1]

		next2_frame = None
		if i + 2 < list_size:
			next2_frame = frame_list[i + 2]

		if frame.is_spare() and next_frame:
			frame.bonus_1 = next_frame.digit_1
		
		if frame.is_strike() and next_frame:
			frame.bonus_1 = next_frame.digit_1
			if next_frame.is_strike() and next2_frame:
				frame.bonus_2 = next2_frame.digit_1
			else:
				frame.bonus_2 = next_frame.digit_2
	
	total_score = 0
	for frame in frame_list:
		#print("debug: frame={}, score={}".format(frame, frame.score()))
		total_score += frame.score()
	return total_score

def test(actual_score, expected_score):
	if actual_score == expected_score:
		print("PASSED: {}".format(actual_score))
	else:
		print("FAILED: Got {} but expected: {}".format(actual_score, expected_score))

test(bowling_score('9/ 9/ X X X 9/ 7/ 6- 6/ XX6'), 203)
test(bowling_score('9/ X 5/ 81 8/ X X 8/ S8/ 63'), 178)
test(bowling_score('9- X X X X X X 7/ 8/ S81'), 221)
