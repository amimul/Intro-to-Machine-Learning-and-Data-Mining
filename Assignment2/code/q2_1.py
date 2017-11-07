'''
Question 2.1 Skeleton Code

Here you should implement and evaluate the k-NN classifier.
'''

import data
import numpy as np
# Import pyplot - plt.imshow is useful!
import matplotlib.pyplot as plt

class KNearestNeighbor(object):
    '''
    K Nearest Neighbor classifier
    '''

    def __init__(self, train_data, train_labels):
        self.train_data = train_data
        self.train_norm = (self.train_data**2).sum(axis=1).reshape(-1,1)
        self.train_labels = train_labels

    def l2_distance(self, test_point):
        '''
        Compute L2 distance between test point and each training point

        Input: test_point is a 1d numpy array
        Output: dist is a numpy array containing the distances between the test point and each training point
        '''
        # Process test point shape
        test_point = np.squeeze(test_point)
        if test_point.ndim == 1:
            test_point = test_point.reshape(1, -1)
        assert test_point.shape[1] == self.train_data.shape[1]

        # Compute squared distance
        train_norm = (self.train_data**2).sum(axis=1).reshape(-1,1)
        test_norm = (test_point**2).sum(axis=1).reshape(1,-1)
        dist = self.train_norm + test_norm - 2*self.train_data.dot(test_point.transpose())
        return np.squeeze(dist)

    def query_knn(self, test_point, k):
        '''
        Query a single test point using the k-NN algorithm

        You should return the digit label provided by the algorithm
        '''

        while(1):
            dist = self.l2_distance(test_point)
            index = dist.argsort()[:k]

            vote = [0 for x in range(10)]
            for i in range(len(index)):
                major_class = int(np.squeeze(self.train_labels[index[i]]))
                vote[major_class] +=1
            m = max(vote)
            index_of_max = [i for i, j in enumerate(vote) if j == m]

            # result_index, value = max(enumerate(vote), key=operator.itemgetter(1))
            if len(index_of_max) == 1:
                digit = index_of_max[0]
                break
            else:
                k -=1

        return digit

def cross_validation(knn, k_range=np.arange(1,15)):
    for k in k_range:
        # Loop over folds
        # Evaluate k-NN
        # ...
        pass

def classification_accuracy(knn, k, eval_data, eval_labels):
    '''
    Evaluate the classification accuracy of knn on the given 'eval_data'
    using the labels
    '''
    pass

def main():
    train_data, train_labels, test_data, test_labels = data.load_all_data('data')
    knn = KNearestNeighbor(train_data, train_labels)

    answer = knn.query_knn(test_data[0], 1);
    print("Predicted: %s"  %answer)
    # print(answer.shape)
    print("In fact: %s" %test_labels[0])

    test = np.reshape(test_data[0], (8,8))
    plt.imshow(test, cmap='gray')
    plt.show()
    # print (train_data.shape)

    # Example usage:
    # predicted_label = knn.query_knn(test_data[0], 1)

if __name__ == '__main__':
    main()