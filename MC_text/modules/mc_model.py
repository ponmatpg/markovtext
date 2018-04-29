# Markov Chain Text Generator ?

import transition_matrix as t_m

class mc_model(object):
	def __init__(self, text):

		self.tm = t_m.text_transition_matrix(text)

		sentences = list(text.split('.'))

		for i in range(1, len(sentences)):
			(self.tm).add_sentence(sentences[i])

		sentences = [list(sent.split(' ')) for sent in sentences]

		self.start_words_dict = {}
		self.start_words_dict_length = 0

		for sent in sentences:
			self.start_words_dict_length += 1

			if sent[0] in self.start_words_dict.keys():
				self.start_words_dict[sent[0]] +=1
			else:
				self.start_words_dict[sent[0]] = 1

	def add_text(self, text):
		"""

		:param text:  text to be added to the model 
		:type text: str

		"""
		sentences = text.split('.')

		for sent in sentences:
			self.start_words_dict_length += 1

			if sent[0] in self.start_words_dict.keys():
				self.start_words_dict[sent[0]] +=1
			else:
				self.start_words_dict[sent[0]] = 0

		for i in range(len(sentences)):
			(self.tm).add_sentence(sentences[i])

	def generate_text(self, sentences=1):
		"""
		
		:param sentences: number of sentences of text to generate 
		:type sentences: int

		"""

		import numpy.random as npr
		text = []

		for i in range(sentences):
			start_words = list(self.start_words_dict.keys())
			start_words_probs = [self.start_words_dict[word] / float(self.start_words_dict_length) for word in start_words]
			sent_gen = [npr.choice(a=start_words, p=start_words_probs)]

			chosen_word = ''
			while chosen_word != '.':
				chosen_word = npr.choice(a=(self.tm).word_list, p=(self.tm).get_probs(sent_gen[-1]))
				sent_gen += [chosen_word]
			text += [' '.join(sent_gen).replace(' .', '.')]

		return (' '.join(text))


















