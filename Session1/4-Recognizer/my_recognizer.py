import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    Xlengths = test_set.get_all_Xlengths()
    for index in range(0, len(Xlengths)):
        X, lengths = Xlengths[index]
        best_score = float("-inf")
        best_word = None 
        logP = {}
        for word, model in models.items():
            try:
                score = model.score(X, lengths)
            except Exception as e:
                score = float("-inf")
            if score > best_score:
                best_score, best_word = score, word
            logP[word] = score
        guesses.append(best_word)
        probabilities.append(logP)
    return probabilities, guesses
