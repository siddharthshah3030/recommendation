
from sklearn import cross_validation as cv
train_data, test_data = cv.train_test_split("ratings", test_size=0.2)

import numpy as np
import pandas as pd
