from modules import mc_model as mc

"""
generate text based on a speech by Alex Jones

"""


def run():
	f = open('/home/paul/Programming/python/MC_text/sampletxt/jones.txt', 'r')
	text = f.read()
	f.close()

	mcm = mc.mc_model(text)
	n = 5
	print(mcm.generate_text(n))


if __name__=="__main__":
	run()