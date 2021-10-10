#snippets
Can be obtained from: https://docs.fast.ai/quick_start.html

> fastai's applications all use the same basic steps and code:
Create appropriate [`DataLoaders`](https://docs.fast.ai/data.core.html#DataLoaders)
Create a [`Learner`](https://docs.fast.ai/learner.html#Learner)
Call a _fit_ method
Make predictions or view results.

Vision
```Python
# This is an automatically generated template for Sublime Text snippets. For more information, see https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html
# Fields: ${1:this} is a ${2:snippet}
# Context: $SELECTION

#region SNIPPET
<snippet><content><![CDATA[
# IMPORTS
from fastai.vision.all import *
	
# PARAMETERS
VALID_PCT = 0.2
SEED = 42
IMG_SIZE = 224
EPOCHS = 1

# DATA
# untar_data: Download & Unzip PETS dataset. 
path = untar_data(URLs.PETS)/'images'
# https://docs.fast.ai/vision.data.html#ImageDataLoaders.from_name_func
dls = ImageDataLoaders.from_name_func(
	path, 
	get_image_files(path), 
	valid_pct=VALID_PCT, 
	seed=SEED,
	# The dataset is labelled s.t. for all cats, 1st char is upper
	label_func=lambda x: x[0].usupper(), 
	item_tfms=Resize(IMG_SIZE))

# TRAINING
# Learner(data, architecture, what to print during training)
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(EPOCHS)

# PREDICTION
img = PILImage.create('images/cat.jpg')
is_cat,_,probs = learn.predict(img)
print(f"Is this a cat?: {is_cat}.")
print(f"Probability it's a cat: {probs[1].item():.6f}")
]]></content>
<tabTrigger>fastai-basic-vision</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

Segmentation
```Python
#region SNIPPET
<snippet><content><![CDATA[
from fastai.vision.all import *

BATCH_SIZE = 8
EPOCHS = 8

path = untar_data(URLs.CAMVID_TINY)
dls = SegmentationDataLoaders.from_label_func(
    path, 
	bs=BATCH_SIZE, 
	fnames = get_image_files(path/"images"),
    label_func = lambda o: path/'labels'/f'{o.stem}_P{o.suffix}',
    codes = np.loadtxt(path/'codes.txt', 
	dtype=str)
)

learn = unet_learner(dls, resnet34)
learn.fine_tune(EPOCHS)

# Visualize how well it achieved its task, by asking the model to color-code each pixel of an image.
learn.show_results(max_n=6, figsize=(7,8))

# Plot the `k` instances that contributed the most to the validation loss
interp = SegmentationInterpretation.from_learner(learn)
interp.plot_top_losses(k=2)
]]></content>
<tabTrigger>fastai-basic-segm</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

NLP
```Python
#region SNIPPET
<snippet><content><![CDATA[
from fastai.text.all import *

dls = TextDataLoaders.from_folder(untar_data(URLs.IMDB), valid='test')
learn = text_classifier_learner(
	dls, AWD_LSTM, 
	drop_mult=0.5, 
	metrics=accuracy)

learn.fine_tune(2, 1e-2)

# Prediction
is_cat,_,probs = learn.predict("I really liked that movie!")
# ('pos', tensor(1), tensor([0.0041, 0.9959]))

]]></content>
<tabTrigger>fastai-basic-nlp</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

Tabular
```Python
# This is an automatically generated template for Sublime Text snippets. For more information, see https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html
# Fields: ${1:this} is a ${2:snippet}
# Context: $SELECTION
# File is saved using tabTrigger name.

#region SNIPPET
<snippet><content><![CDATA[
# Building models from plain _tabular_ data
from fastai.tabular.all import *

path = untar_data(URLs.ADULT_SAMPLE)

dls = TabularDataLoaders.from_csv(
	path/'adult.csv', 
	path=path, 
	y_names="salary",
    cat_names = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race'],
    cont_names = ['age', 'fnlwgt', 'education-num'],
    procs = [Categorify, FillMissing, Normalize])

learn = tabular_learner(dls, metrics=accuracy)
learn.fit_one_cycle(2)

]]></content>
<tabTrigger>fastai-basic-csv</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

> There is no pretrained model available for this task (in general, pretrained models are not widely available for any tabular modeling tasks, although some organizations have created them for internal use), so we don't use `fine_tune` in this case. Instead we use `fit_one_cycle`, the most commonly used method for training fastai models _from scratch_ (i.e. without transfer learning).

Collab (recommender systems)
```Python
#region SNIPPET
<snippet><content><![CDATA[
# Recommendation systems
	
# Collaborative filtering (CF) is a **technique used by recommender systems**. ... In the newer, narrower sense, collaborative filtering is a method of making automatic predictions (filtering) about the interests of a user by collecting preferences or taste information from many users (collaborating).
from fastai.collab import *
	
# [MovieLens dataset](https://doi.org/10.1145/2827872)
path = untar_data(URLs.ML_SAMPLE)
dls = CollabDataLoaders.from_csv(path/'ratings.csv')
learn = collab_learner(dls, y_range=(0.5,5.5))
learn.fine_tune(6)

# use the same `show_results` call we saw earlier to view a few examples of user and movie IDs, actual ratings, and predictions:
learn.show_results()

]]></content>
<tabTrigger>fastai-basic-collab</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

Additional clarifications:
fit_one_cycle: See https://fastai1.fast.ai/callbacks.one_cycle.html#What-is-1cycle? and https://sgugger.github.io/the-1cycle-policy.html

item-tfms and batch-tfms: https://forums.fast.ai/t/item-tfms-vs-batch-tfms/68990/4
item happens per item (likely on CPU)
batch happens in batches (likely on GPU)
tfms most likely refers to transforms

Choosing a good validation / test subset: https://colab.research.google.com/github/fastai/fastbook/blob/master/01_intro.ipynb#scrollTo=tsN2g-XAjd4g