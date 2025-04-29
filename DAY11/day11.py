from sklearn.pipeline import * 
from sklearn.naive_bayes import * 
from sklearn.cluster import *  
from sklearn.covariance import *  
from sklearn.cross_decomposition import *  
from sklearn.datasets import *  
from sklearn.decomposition import *  
from sklearn.ensemble import *  
from sklearn.feature_extraction import *  
from sklearn.feature_extraction.text import *  
from sklearn.feature_selection import *  
from sklearn.gaussian_process import *  
from sklearn.linear_model import *  
from sklearn.manifold import *  
from sklearn.metrics import *  
from sklearn.mixture import *  
from sklearn.model_selection import *  
from sklearn.neighbors import *  
from sklearn.neural_network import *  
from sklearn.preprocessing import *  
from sklearn.svm import *  
from sklearn.tree import *  
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from yellowbrick.classifier import ConfusionMatrix, ROCAUC
data = load_breast_cancer()
X=data.data
y =  data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
cm = ConfusionMatrix(LogisticRegression(max_iter=10000), classes=["Benign", "Malignant"])
cm.fit(X_train, y_train)
cm.score(X_test, y_test)
cm.show()

roc = ROCAUC(LogisticRegression(max_iter=10000), classes=["Benign", "Malignant"])
roc.fit(X_train, y_train)
roc.score(X_test, y_test)
roc.show()
