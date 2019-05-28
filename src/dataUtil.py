import jieba
import jieba.posseg as pseg
from gensim.models import word2vec
import gensim
import logging
def getW2Vdata():
	with open('../input/w2vdata.txt','w') as w2vdata:
		with open('../input/train.txt', 'r') as trainf:
			for line in trainf:
				if len(line.strip()) != 0:
					items = line.strip().split('\t')
					w2vdata.write(" ".join(jieba.cut(items[1],cut_all=False)))
					w2vdata.write("\n")

def trainW2V():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	sentences = word2vec.Text8Corpus("../input/w2vdata.txt")       #your data
	model = word2vec.Word2Vec(sentences, window=6, size=250)
	model.save(u"W2V525.model")
	print(model.similarity("刘翔","博尔特"))
 
def testW2V():
	model =  gensim.models.Word2Vec.load("W2V525.model")
	print(model.similarity("我","你"))
	for e in model.most_similar(positive=['丑陋'], topn=10):
		print(e[0], e[1])

def testSegmentation(sentence):
	for word, tag in pseg.cut(sentence):
		print(word + " " + tag )

if __name__ == '__main__':
	#trainW2V()
	#testW2V()
	testSegmentation("李飞")