Note: This project is still a work-in-progress and I expect to make API changes soon.

# Using the classifier
## Importing
If your files are in the same directory as learner.py, `from learner import Learner` should do the trick.

## Training data
The first thing to do is to tag all your training data. Training data should be provided as a list of tuples. The tuples should take the form (class, text).

## Creating the Learner
At the moment, all training data is provided on creation of the object. Creating the object with Learner(training_data) will create a trained object.

## Classifying
Calling my_learner.classify(text_to_classify) will return a tuple with the presumed class and a number used in determine class. This will be later be changed to return the class.

## Testing
If you call my_learner.test(testing_data) with testing data formatted in the same way as training data, it will return the success percentage as a decimal (e.g. 50% = 0.5).
