#ML #data-augmentation

#### Page 1

> 5 Techniques to work with Imbalanced Data in Machine Learning (p. 1) 

---
#### Page 2

> 1.) Upsampling Minority Class: (p. 2) 

> Upsampling or Oversampling refers to the technique to create artificial or duplicate data points or of the minority class sample to balance the class label. (p. 2) 

---
#### Page 3

> 7 Over Sampling techniques to handle Imbalanced Data Deep dive analysis of various oversampling techniques towardsdatascience.com (p. 3) 

See more at [[imbalanced-learn.org-over_sampling]].

```pdf
{"url": "/Papers/pdfs/Archived/Imbalanced Data in Machine Learn.pdf", "page": 3,
"rect": [0,0,0,0]
}
```

> 2.) Downsampling Majority Class: (p. 3) 

> Downsampling or Undersampling refers to remove or reduce the majority of class samples to balance the class label. There are various undersampling techniques implemented in the imblearn package (p. 3) 

---
#### Page 4

> Under-sampling methods - Version 0.8.0 The imblearn.under_sampling provides methods to under-sample a dataset. The… imbalanced-learn.org (p. 4) 

```pdf
{"url": "/Papers/pdfs/Archived/Imbalanced Data in Machine Learn.pdf", "page": 4,
"rect": [0,0,0,0]
}
```

> 3.) Generate Synthetic Data: (p. 4) 

> Undersampling techniques are not recommended as it removes (p. 4) 

> data points. (p. 4) 

> The idea is to generate synthetic data points of minority class samples in the nearby region or neighborhood of minority class samples. (p. 4) 

---
#### Page 5

> Follow [Imblearn documentation](https://imbalanced-learn.org/stable/combine.html) for the implementation of above-discussed SMOTE techniques: (p. 5) 

> 4.) Combine Oversampling and Undersampling Techniques: (p. 5) 

> The idea is to first use an oversampling technique to create duplicate and artificial data points and use undersampling techniques to remove noise or unnecessary generated data points. (p. 5) 

> Follow Imblearn documentation for the implementation of Smote-Tomek and Smote-ENN techniques. (p. 5) 

---
#### Page 6

> The undersampling technique removes the majority class data points which results in data loss, whereas upsampling creates artificial data points of the minority class. During the training of machine learning, one can use class_weight parameter to handle the imbalance in the dataset. (p. 6) 

> Decision Trees and Random Forest should be preferred over other machine learning algorithms as they tend to perform well on imbalanced data. (p. 6) 

---
