Note: This project is still a work-in-progress and I expect to make API changes soon.

# Using the classifier
## Importing
For those unfamiliar with Python, if your files are in the same directory as learner.py, `from learner import Learner` should do the trick.

## Creating the Learner
Creating the object with `Learner()` will create an untrained Learner with default parameters. There is an 1 optional parameter that affects how the object handles a word pattern with only a single occurence in the corpus.

## Training data
The first thing to do is to tag all your training data. Training data should be provided as a list of tuples. The tuples should take the form (class, text). At the moment, it supports any hashable value for the class and only strings for the text, as it does some NLTK stuff to improve accuracy. Train the object with `my_learner.train(training_data)`.

## Classifying
Calling `my_learner.classify(text_to_classify)` will return the guessed class.

## Testing
If you call `my_learner.test(testing_data)` with testing data formatted in the same way as training data, it will return the success percentage as a decimal (e.g. 50% = 0.5).
