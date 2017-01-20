
Question Answering base on IR
Requirement : 

    Window or Unix/Linux environment
    Python 2.7
    nltk
    StanfordNERTagger :
        Download : http://nlp.stanford.edu/software/CRF-NER.shtml#Download
        Install JDK version >= 8
        Setting Environment variables for Window :
            Environment variable for CLASSPATH : path\to\stanford-ner\stanford-ner.jar
            Environment variable for STANFORD_MODELS : path\to\stanford-ner\classifiers
        Setting Environment variables for Unix : Open terminal type : gedit ~/.bashrc then move to the end of file and add :
            export CLASSPATH=path/to/stanford-ner/stanford-ner.jar
            export STANFORD_MODELS=path/to/stanford-ner/classifiers
    sklearn
    googleapiclient : pip install --upgrade google-api-python-client
    BeautifulSoup
    plotly


