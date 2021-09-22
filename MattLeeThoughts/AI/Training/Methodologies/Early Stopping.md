#AI #ML

Most of this work is from source 2.

#### Motivation
When training a large network, there will be a point during training when the model will stop generalizing and start learning the statistical noise in the training dataset.

This overfitting of the training dataset will result in an increase in generalization error, making the model less useful at making predictions on new data.

The challenge is to train the network long enough that it is capable of learning the mapping from inputs to outputs, but not training the model so long that it overfits the training data [2].

####  Early Stopping is a form of neural network regularization
 If regularization methods like weight decay that update the loss function to encourage less complex models are considered “_explicit_” regularization, then early stopping may be thought of as a type of “_implicit_” regularization, much like using a smaller network that has less capacity.
 
#### Assumptions
1. Model is stronger than problem
	1. More formally, model is "under constrained", meaning that it has more capacity than is required for the problem.

When training the network, a larger number of training epochs is used than may normally be required, to give the network plenty of opportunity to fit, then begin to overfit the training dataset.

#### Implementation Steps

#####  1. Monitoring model performance
1. Pick a subset of the training data to serve as the validation set.
2. You can validate the model against this set every n training epochs.
3. Plotting a graph of the loss may help identify a good trigger to use.

#####  2. Trigger to stop training
Triggers include:
-   No change in metric over a given number of epochs.
-   An absolute change in a metric.
-   A decrease in performance observed over a given number of epochs.
-   Average change in metric over a given number of epochs.

Loss may be a good metric.

#####  3. The choice of model to use.

At the time that training is halted, the model is known to have slightly worse generalization error than a model at a prior epoch.

Simple approach is greedy: every time the error on the validation set improves, save a copy of the model parameters. When the training algorithm terminates, we return these parameters instead.

##### 4. Prevent overfitting to the validation dataset

1. Do not repeat the early stopping procedure many times. This can be done by one of the 2 ways:
	1. Only use early stopping once after all other hyperparameters of the model have been chosen.
	2. [[K-fold Cross Validation]] using number of epochs as the hyperparam, or even to choose the type of early stopping trigger.

#### When to use
1. When the model has a lack of regularization (RNN models)
2. Model can overfit to the dataset (if it's too small)

#### When not to use
1. If the dataset is sufficiently large (such that model overfitting is not a concern), early stopping may not be necessary

#### Relation to [[K-fold Cross Validation]]
The k-fold cross-validation procedure is designed to estimate the generalization error of a model by repeatedly refitting and evaluating it on different subsets of a dataset.

Early stopping is designed to monitor the generalization error of one model and stop training when generalization error begins to degrade.

They are at odds because cross-validation assumes you don’t know the generalization error and early stopping is trying to give you the best model based on knowledge of generalization error.

Sources
 ===
1. https://stats.stackexchange.com/questions/283631/how-to-correctly-use-validation-and-test-sets-for-neural-network-training/330471#330471
2. https://machinelearningmastery.com/early-stopping-to-avoid-overtraining-neural-network-models/