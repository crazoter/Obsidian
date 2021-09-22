![[Advanced Techniques for Fine-tuning Transformers _ by Peggy Chang _ Sep, 2021 _ Towards Data Science(2).PDF]]

---

#### Page 1

> Advanced Techniques for Fine-tuning Transformers (p. 1)

---
#### Page 3

> 1. Layer-wise Learning Rate Decay (LLRD) In Revisiting Few-sample BERT Fine-tuning, the authors describe layer-wise learning rate decay as �a method that applies higher learning rates for top layers and lower learning rates for bottom layers. This is accomplished by setting the learning rate of the top layer and using a multiplicative decay rate to decrease the learning rate layer-by-layer from top to bottom�. (p. 3)

> A similar concept called discriminative fine-tuning is also express in Universal Language Model Fine-tuning for Text Classification. �Discriminative fine-tuning allows us to tune each layer with different learning rates instead of using the same learning rate for all layers of the model� All these make sense as different layers in the Transformer model usually capture different kinds of information. Bottom layers often encode more common, general, and broad-based information, while the top layer closer to the output encodes information more localized and specific to the task on hand. (p. 3)

---
#### Page 4

> The first way is following the method described in Revisiting Few-sample BERT Fine- tuning. We choose a learning rate of 3.5e-6 for the top layer and use a multiplicative decay rate of 0.9 to decrease the learning rate layer-by-layer from top to bottom. It will result in the bottom layers ( embeddings and layer0 ) having a learning rate roughly close to 1e-6 . We do this in a function called roberta_base_AdamW_LLRD . (p. 4)

---
#### Page 6

> The second approach of implementing layer-wise learning rate decay (or discriminative fine-tuning) is to group layers into different sets and apply different learning rates to each. We will refer to this as grouped LLRD. (p. 6)

---
#### Page 8

> 2. Warm-up Steps For the linear scheduler that we used, we can apply warm-up steps. For example, applying 50 warm-up steps means the learning rate will increase linearly from 0 to the initial learning rate set in the optimizer during the first 50 steps (warm-up phase). After that, the learning rate will start to decrease linearly to 0. (p. 8)

---
#### Page 10

> 3. Re-initializing Pre-trained Layers (p. 10)

> to achieve better fine-tuning results, sometimes we need to discard some of these weights and re-initialize them during the fine-tuning process. So how do we do this? Earlier, we talked about different layers of the Transformer capturing different kinds of information. The bottom layers usually encode more general information. These are useful, and so we want to preserve these low-level representations. What we want to refresh are the top layers closer to the output. They are layers that encode information more specific to the pre-training task, and now we want them to adapt to ours. (p. 10)

---
#### Page 11

> every model and dataset is different. For our case, the optimal value for n is 5. You may start to experience deteriorating results if re-initializing more layers beyond the optimal point. (p. 11)

---
#### Page 12

> Stochastic Weight Averaging (SWA) is a deep neural network training technique presented in Averaging Weights Leads to Wider Optima and Better Generalization. (p. 12)

> 4. Stochastic Weight Averaging (SWA) Stochastic Weight Averaging (SWA) is a deep neural network training technique presented in Averaging Weights Leads to Wider Optima and Better Generalization. (p. 12)

> So, how does SWA work? As stated in this PyTorch blog, SWA comprises of two ingredients: First, it uses a modified learning rate schedule. For example, we can use the standard decaying learning rate strategy (such as the linear schedule that we are using) for the first 75% of training time and then set the learning rate to a reasonably high constant value for the remaining 25% of the time. Second, it takes an equal average of the weights of the networks traversed. For example, we can maintain a running average of the weights obtained at the end, within the last 25% of training time. After training is complete, we then set the weights of the network to the computed SWA averages. (p. 12)

---
