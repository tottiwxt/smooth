import requests
import json


def cut_sentence(sentence):
	url = 'http://10.110.96.169:10142/crf?user_name=mobile_danmu&password=lizhenyu20190520&raw_sentence='+sentence
	r = requests.get(url)
	result = r.text
	print(result)
	word_nodes = json.loads(result)
	#print(word_nodes)
	cut_result = []
	if(word_nodes["return_state"]==1):
		for word_info in word_nodes["word_nodes"]:
			#print(word_info["word_info"]["word"])
			cut_piece = []
			word = word_info["word_info"]["word"]
			tag = word_info["word_info"]["pos"]
			cut_result.append(tag)
	return cut_result

print(cut_sentence("将序列比对到基因组"))