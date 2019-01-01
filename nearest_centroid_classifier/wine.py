
import numpy as np
from matplotlib import pyplot as plt

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. 
    """
    data = np.genfromtxt(csv_filename, delimiter=";", skip_header=1)   
    return data[:,:-1]
    
def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. 
    """
    train_size = int(len(dataset) * 0.9)
    return dataset[:train_size], dataset[train_size+1:]
    
def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    return sum(data) / len(data)
    
def experiment(ww_train, rw_train, ww_test, rw_test, verbose = True):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    ww_model = compute_centroid(ww_train)
    rw_model = compute_centroid(rw_train)
    
    correct = 0
    for ww in ww_test: 
        if euclidean_distance(ww,ww_model) < euclidean_distance(ww,rw_model):
            correct += 1        
    for rw in rw_test: 
        if euclidean_distance(rw,ww_model) >= euclidean_distance(rw,rw_model):
            correct += 1
    total = len(ww_test) + len(rw_test)
    if verbose: 
        print("Total:{} Correct:{} Accuracy:{}".format(total, correct, correct/total))
    return correct/total
    
def learning_curve(ww_training, rw_training, ww_test, rw_test):
    """
    Perform a series of experiments to compute and plot a learning curve.
    """
    
    np.random.shuffle(ww_training)
    np.random.shuffle(rw_training)
    max_examples = max(len(ww_training), len(rw_training))

    accuracies = \
    [experiment(ww_training[:i], rw_training[:i], ww_test, rw_test, \
                   verbose=False) for i in range(1, max_examples-1)]
    
    plt.plot(range(1,max_examples-1), accuracies)

def cross_validation(ww_data, rw_data, k):
    """
    Perform k-fold crossvalidation on the data and print the accuracy for each
    fold. 
    """    
    part_size_w = len(ww_data) // k
    part_size_r = len(rw_data) // k

    accuracies = []

    partitions_w = []
    partitions_r = []

    for i in range(k-1):
        partitions_w.append(ww_data[i*part_size_w:(i+1)*part_size_w])
        partitions_r.append(rw_data[i*part_size_r:(i+1)*part_size_r])

    partitions_r.append(rw_data[(i+1)*part_size_r:])   
    partitions_w.append(ww_data[(i+1)*part_size_w:])

    for i in range(k):
        test_r = partitions_r[i]
        test_w = partitions_w[i]

        train_r = np.vstack(partitions_r[:i] + partitions_r[i+1:])
        train_w = np.vstack(partitions_w[:i] + partitions_w[i+1:])
        
        acc = experiment(train_w, train_r, test_w, test_r)
        accuracies.append(acc)
    return sum(accuracies) / len(accuracies)
            
                                   
    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')

  
    k = 10
    acc = cross_validation(ww_data, rw_data,k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
    