# study_AIs
📝 머신러닝 학습 자료

## 💻 데이터분석을 위한 기초문법
| 제목 | 작성소스 | 설명 | 비고 |
|---|---|---|---|
| concat | [numpys_concat](./codes/numpys.py) | numpy을 이용한 concat  | np.concatenate((, ), axis=)|
| concat | [pandas_concat](./codes/pandass.ipynb) | pandas를 이용한 concat  | pd.concat([ , ], axis=)|
| encoder, concat, Imbalanced Data Sampling | [pandas_encoder](./codes/sklearns.ipynb) | Encoding with One Hot Encoding & concat & Under/Over Sampling | oneHotEncoder.transform(df_[[' ']]).toarray()|

## 💻 데이터분석
| 제목 | 작성소스 | 설명 | 비고 |
|---|---|---|---|
| 지도학습-이진분류 데이터 분석 | [TitanicFromDisaster](./codes/MLs/Classifications/TitanicFromDisaster.ipynb) | 지도학습-이진분류  |LogisticRegression |
| 지도학습-이진분류 DecisionTreeClassifier 분석 | [TitanicFromDisaster_Tree](./codes/MLs/Classifications/TitanicFromDisaster_Tree.ipynb) | DecisionTreeClassifier  | plot_tree |
| 지도학습-이진분류 evaluation | [TitanicFromDisaster_evaluation](./codes/MLs/Classifications/TitanicFromDisaster_evaluation.ipynb) |  evaluation(평가) |mean_squared_error(MSE), classification_report,오차 행렬 (confusion_matrix) |
| 지도학습-다항분류 Pre-Process | [Pre-Process](./codes/MLs/Classifications/NSC_BND_M20_DecisionTreeClassifier_preprocess.ipynb) |  전처리 과정 | apply() 활용|
| 비지도학습 | [iris_KMeans](./codes/MLs/Clusterings/iris_KMeans.ipynb) | 비지도학습의 데이터 분석|KMeans, sum of square |
| 회귀분석 | [Regression](./codes/MLs/Regressions/BreastCancerWisconsin_Regression.ipynb) | 회귀분석 |LinearRegression, 서비스 배포 |
| 회귀분석 평가 | [Regression_evaluations](./codes/MLs/Regressions/BreastCancerWisconsin_Regression_evaluations.ipynb) | 회귀분석의 평가 |r2_score, MSE(mean_squared_error) |
| 회귀분석 평가 | [scaling_encoding](./codes/MLs/Classifications/TitanicFromDisaster_scaling_encoding.ipynb) | Scaling & Encoding |Encoding with One Hot Encoding, Scaling - MinMaxScaler |
| GridSearchCV | [GridSearchCV](./codes/MLs/Classifications/NSC_BND_M20_GridSearchCV.ipynb) | GridSearchCV |평가 score, best_score,classification_report |
| resampling | [resampling](./codes/MLs/Classifications/recurrenceOfSurgery_MachineLearning_Normal.ipynb) | resampling |resampling(Over, Under, Combine sampling) |
| for문_resampling | [for문_resampling](./codes/MLs/Classifications/recurrenceOfSurgery_UnderSampling.ipynb) | UnderSampling |fo문을 통한 UnderSampling과 hypertuning |




