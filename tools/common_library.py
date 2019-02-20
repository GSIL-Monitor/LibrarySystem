import os
import sys
import pickle
import jieba
from tqdm import tqdm_notebook,tqdm
import random
import warnings
import re
# from sklearn.metrics import *
import unittest
import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt
import copy
import seaborn as sns
from dateutil.parser import parse
import re
import json
import random
import requests
import traceback
from datetime import datetime, timedelta, timezone
import pymysql
import zmail
from sqlalchemy import create_engine
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *
from sklearn.preprocessing import *
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.ensemble import (RandomTreesEmbedding, RandomForestClassifier,
                              GradientBoostingClassifier)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
warnings.filterwarnings("ignore")