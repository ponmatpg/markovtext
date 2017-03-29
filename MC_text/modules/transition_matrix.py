

class text_transition_matrix(object):
	def __init__(self, sentence):
		self.word_list = ['.']
		self.prob_dict = {'.': [0, 1, 1]}

		self.add_sentence(sentence)


	def add_sentence(self, sentence):
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
		if word not in self.word_list:
			return [0] * len(self.word_list)
		else:
			return [x / float(self.prob_dict[word][1]) for x in self.prob_dict[word][2:]]




# sentence = "Hello there Dylan! What's Hello up there?"
# TM = text_transition_matrix(sentence)
# print(TM.word_list)
# print(TM.prob_dict)
# print(TM.get_probs("Hello"))


