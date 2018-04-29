

class text_transition_matrix(object):
	"""
	dynamic class to handle 

	"""
	def __init__(self, sentence=None):
		"""
		constructor

		:param sentence: Text with which to seed the transition matrix.
		Assumed to be a single sentence
		:type sentence: str

		"""
		self.word_list = ['.']
		self.prob_dict = {'.': [0, 1, 1]}

		if sentence is not None:
			self.add_sentence(sentence)


	def add_sentence(self, sentence):
		"""
		method to add a new sentence to the aggregate text corpus of the transition matrix


		:param sentence: sentence to add to the transition matrix.
		Assumed to be a single sentence
		:type sentence: str

		"""
		sentence = sentence.replace('.', '')
		words = sentence.split(' ') + ["."]

		for i in range(len(words) - 1):
			if words[i] in self.word_list and words[i+1] in self.word_list:
				self.prob_dict[words[i]][2 + self.prob_dict[words[i+1]][0]] += 1
				self.prob_dict[words[i]][1] += 1 

			elif words[i] not in self.word_list and words[i+1] in self.word_list:
				for word in self.word_list:
					self.prob_dict[word] += [0]

				self.word_list.append(words[i])

				self.prob_dict[words[i]] = [len(self.word_list)-1, 1] + [0] * len(self.word_list)
				self.prob_dict[words[i]][2 + self.prob_dict[words[i+1]][0]] = 1

			elif words[i] in self.word_list and words[i+1] not in self.word_list:
				for word in self.word_list:
					self.prob_dict[word] += [0]

				self.word_list.append(words[i+1])
				self.prob_dict[words[i+1]] = [len(self.word_list)-1, 0] + [0] * len(self.word_list)

				self.prob_dict[words[i]][-1] = 1
				self.prob_dict[words[i]][1] += 1 

			elif words[i] not in self.word_list and words[i+1] not in self.word_list:
				for word in self.word_list:
					self.prob_dict[word] += [0, 0]

				self.word_list.append(words[i])
				self.word_list.append(words[i+1])
				
				self.prob_dict[words[i]] = [len(self.word_list)-2, 1] + [0] * len(self.word_list)
				self.prob_dict[words[i]][-1] = 1

				self.prob_dict[words[i+1]] = [len(self.word_list)-1, 0] + [0] * len(self.word_list)

	def get_probs(self, word):
		"""
		
		:param word: some word in the text corpus (else returns 0)
		:type word: str

		:return: mapping associating every other word in the text corpus to the probability that it will follow 'word'
		e.g. for word = 'hello'
		returns {'there': 0.5, 'world': 0.5}
		to indicate that the probability of world following hello is 50% amd there following hello is 50% 

		:rtype: dict

		"""
		if word not in self.word_list:
			return [0] * len(self.word_list)
		else:
			return [x / float(self.prob_dict[word][1]) for x in self.prob_dict[word][2:]]




# sentence = "Hello there Dylan! What's Hello up there?"
# TM = text_transition_matrix(sentence)
# print(TM.word_list)
# print(TM.prob_dict)
# print(TM.get_probs("Hello"))


