import re
import nltk
import numpy as np
import platform

def getAnswerTypeIndex(filename):
    f = open(filename)
    if (platform.system() == 'Windows'):
        lines = f.read().split('\n')
    else:
        lines = f.read().split('\r\n')
    answer_types = {}
    for line in lines:
        answer_types[line.split(' ')[1]] = int(line.split(' ')[0])
        answer_types[int(line.split(' ')[0])] = line.split(' ')[1]
    f.close()
    return answer_types

def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!\']", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip()

def getPOSTag(sentences):
    tags = nltk.pos_tag(nltk.word_tokenize(sentences))
    tags_sequence = ""
    for tag in tags:
        tags_sequence += tag[1] + " "
    return tags_sequence
def token(s):
    return s.split()

def feature_extraction(question,CV_Unigram,CV_UniPOS):
    if (type(question) is str):
        question_POSTag = getPOSTag(question)
        arr_feature = CV_Unigram.transform(question).toarray()
        arr_feature += CV_UniPOS.transform(question_POSTag).toarray()
    else:
        question_POSTag = [getPOSTag(q) for q in question]
        arr_feature = np.array(CV_Unigram.transform(question).toarray())
        arr_feature = np.hstack((arr_feature,np.array(CV_UniPOS.transform(question_POSTag).toarray())))
    return np.array(arr_feature)
