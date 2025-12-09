(i) what is the TF-IDF measure:

    It meausres what terms are most valuble for representing the content of a report or document within a larger collection. the point is calculate how much a word is used locally(in a document) but also how rare it is in the collection of documents. you have the parameters TF(local -> amount inside the document), and IDF(global-> rarity amongst all docs). this makes it possible to turn documents into vectors in a vector space. "stop words" like the, as, in, etc are ignored as they are almost never important to the content of the doc

(ii) how to use TF-IDF for:
– document similarity:
How similiar two documents are, is decided by the cosine simularity(measures the cosine of the angle between to vectors). For example, the result of 1(0*, points in the same direction) means they are very much related in terms of content/features, while 0 (90*) means they are unrelated, and so on(180 degrees-> in opposite direction).

        The magnitude, or length of the vector is based on the length of the document, while the direction of the vector is represnting its orientation(in terms of content)
        this way we can identify the similiarity between 2 documents with cosiderable difference in length as the method looks att difference in angle-> orientation

    – classify text:
        the vectors from a collection fo documents are fed into a machine learning algorithm to train a predictive model using the known category labels. To classify new, unseen text, the new documents are transformed into TF-IDF vectors using the same transformer (vocabulary and IDF weights) derived from the training set and use the trained model to predict their categories. the document reccomends Multinomial Naïve Bayes. then apply the model on new vectors to verify their categories
