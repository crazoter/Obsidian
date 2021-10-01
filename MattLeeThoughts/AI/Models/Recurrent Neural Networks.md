#ML #NLP 

[Essentials of Deep Learning : Introduction to Long Short Term Memory](https://www.analyticsvidhya.com/blog/2017/12/fundamentals-of-deep-learning-introduction-to-lstm/)

RNN architecture and idea
![[The-architecture-of-RNN.png]]

####  Flaw: Short-term memory
Reason = **Vanishing Gradient.** 
- For a [[Feed-forward Neural Network]], the weight updating that is applied on a particular layer is a multiple of the learning rate, the error term from the previous layer and the input to that layer. 

Thus, the error term for a particular layer is somewhere a product of all previous layers’ errors. When dealing with activation functions like the sigmoid function, the small values of its derivatives (occurring in the error function) gets multiplied multiple times as we move towards the starting layers. As a result of this, the gradient almost vanishes as we move towards the starting layers, and it becomes difficult to train these layers.

A similar case is observed in Recurrent Neural Networks. RNN remembers things for just small durations of time, i.e. if we need the information after a small time it may be reproducible, but once a lot of words are fed in, this information gets lost somewhere. This issue can be resolved by applying a slightly tweaked version of RNNs – the Long Short-Term Memory Networks.

seq2seq using RNN: [https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)

By design, a RNN takes two inputs at each time step: an input (in the case of the encoder, one word from the input sentence), and a hidden state.

1. Break your text into tokens (tokenize)

2. Convert the tokens into word embeddings (These turn words into vector spaces that capture a lot of the meaning/semantic information of the words (e.g. king - man + woman = queen)).

3. Encoder will have a n number of RNNs. The first RNN will only take in embedding[0] and output a hidden state (context).

3. The decoder will take the output of the encoders and run it through an architecture similar to the encoder.