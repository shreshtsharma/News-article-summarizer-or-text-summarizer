import nltk
from nltk.corpus import stopwords
from string import punctuation
from heapq import nlargest
# nltk.download('stopwords')
def summarize(text):
    stops=list(stopwords.words('english'))
    stops

    # TOKENIZING SENTENCES

    # nltk.download('punkt')
    from nltk.tokenize import sent_tokenize
    sentences=sent_tokenize(text)
    # print(sentences)
    # TOKENIZING WORDS

    from nltk.tokenize import word_tokenize
    words=word_tokenize(text)
    # print(words)

    # MAKING WORD FREQUENCY TABLE

    word_frequency={}
    for word in words:
        if word.lower() not in stops:
            if word.lower() not in punctuation:
                if word.lower() not in word_frequency.keys():
                    word_frequency[word.lower()]=1
                else:
                    word_frequency[word.lower()]+=1

    # print(word_frequency)

    # NORMALIZING WORD FREQUENCIES 
    maxi=max(word_frequency.values())
    for key in word_frequency.keys():
        word_frequency[key]/=maxi

    sentence_importance = {}

    for sent in sentences:
        words=sent.split()
        for word in words:
            if word.lower() in word_frequency:
                if sent not in sentence_importance:
                    sentence_importance[sent]=word_frequency[word.lower()]
                else:
                    sentence_importance[sent]+=word_frequency[word.lower()]
                    
                    

    maximum=max(sentence_importance.values())

    for key in sentence_importance:
        sentence_importance[key]/=maximum


    sentences_selected=int(len(sentences)*0.2)
    final_sentences=nlargest(sentences_selected,sentence_importance,key=sentence_importance.get)


    summary=' '.join(final_sentences)
    return summary

    
# TESTING
text = """
There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on.
The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.).
The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query.
Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document.
Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic).
This problem is called multi-document summarization. A related application is summarizing news articles.
Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization.
It consists in selecting a representative set of images from a larger set of images.
[3] A summary in this context is useful to show the most representative images of results in an image collection exploration system. 
Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions.
Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured."""

str="""The best crime stories come embedded in their very specific context: if you know the victim’s history, you can have an understanding of why he/she was killed. Also, it’s never just the one person who dies; very often, those that are left behind also experience a kind of dying.

Both history and geography are important indicators in Sudip Sharma’s atmospheric, beautifully-realised drama ‘Kohrra’ which is as much a murder mystery as an incisive reading of contemporary Punjab and the Punjabi psyche: an NRI who is back home to get married, is found dead in the fields; his best friend has gone missing. The investigation by two local cops Balbir (Suvinder Vicky) and Garundi (Barun Sobti) puts into motion an inexorable unravelling– of family politics, buried shame, male ego, unresolved childhood trauma, unrequited passion, corroded love, hidden sexual identities, intergenerational enmity, and, yes, over-weaning patriarchy. It’s a lot, but Sharma (‘Pataal Lok’, ‘Udta Punjab’, ‘NH10’) and his two writers Gunjit Chopra and Diggi Sisodia keep a firm handle on it all, and give us one of the best web series of the year.

One of the most impressive elements of the six-part series is the way the village becomes the site from where everything flows. The names, a mix of desi and videshi, immediately speak of provenance: Steve Dhillon (Manish Chaudhary) who lived in London for several years is now back in his ‘pind’; his estranged brother Manna (Varun Badola) never had to make a name-change to merge with the ‘goras’, because he has remained a son of the soil. Steve’s dead son is called Paul, and his stepson Liam: you wouldn’t know who was British-India, and who pure British, until you set eyes on them. The coming back home for an ‘arranged marriage’ after young men have presumably sowed their oats is such a commonplace occurrence that it doesn’t raise any eyebrows, even if the bridegroom’s brutal killing splits everything wide open.

"""
summary=summarize(str)

print(summary)
