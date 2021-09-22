#AI #ML

Descript
 ===

The k-fold cross-validation procedure is designed to estimate the generalization error of a model by repeatedly refitting and evaluating it on different subsets of a dataset.

![[Pasted image 20210919102625.png]]

1. Cross-validation gives you an estimate how well will the model perform on average **given the fixed hyperparameters**.
	1. The result is only valid for you if you then use the same hyperparameters for the final, output model.
	2. Hyperparameters can include *anything* that is not kept fixed across the iterations. Such as:
		1. Anything related to the model architecture e.g.
			1. The (random) weights of a model if you're performing random initialization. See [link](https://stats.stackexchange.com/questions/352253/should-i-use-the-same-weight-initialization-for-each-fold-in-cross-validation).
			2. Whether or not the layers are frozen
		2. Anything related to the training of the model
			1. learning rate, weight decay, dropout ratios, number of epochs, batch size etc
2. Always keep a test set (independent of training / validation data) to identify the best final model

Use cases
 === 
 1. Usually not used for larger neural networks, because takes very long to train even 1 model, let alone 10 models using cross validation, and too many hyperparameters like # of epochs. ([src](https://stats.stackexchange.com/questions/283631/how-to-correctly-use-validation-and-test-sets-for-neural-network-training/330471#330471))