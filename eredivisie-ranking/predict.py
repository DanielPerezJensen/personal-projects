import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split


def main():


	df = pd.read_csv('eredivisie-ranking.csv')

	coi = ['tr_begin']

	x = np.array(df[coi])

	y = np.array(df['ranking_class'])

	clf = svm.SVC()

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

	clf.fit(x_train, y_train)

	accuracy = clf.score(x_test, y_test)

	print(accuracy)


if __name__ == "__main__":
	main()