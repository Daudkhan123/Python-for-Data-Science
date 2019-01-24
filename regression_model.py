from sklearn import tree


#[Height, weight, shoe size]
X = [[181, 80, 44], [166, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'female', 'male', 'female', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()
clf.fit(X, Y)
predict = clf.predict([[190, 75, 40]])
print('Decision tREE')
print(predict)
