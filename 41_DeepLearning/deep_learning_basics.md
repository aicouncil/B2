# Digit Classification with a Neural Network using Keras

This document provides a detailed explanation of the `mnist-g2.ipynb` notebook, which demonstrates the end-to-end process of building and training a simple neural network for handwritten digit classification. The project uses the well-known MNIST dataset and the Keras deep learning framework.

***

## 1. Data Preparation

The first step is to load and preprocess the data to make it suitable for a neural network model.

* **Data Loading:** The script loads a CSV file named `mnist_digits_train.csv` into a Pandas DataFrame. This dataset contains pixel values for 60,000 handwritten digit images.
    ```python
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('C:/Users/vipul/Downloads/mnist_digits_train.csv')
    df.head()
    ```
    The DataFrame has 785 columns. Columns `0` through `783` contain the pixel intensity values for a flattened 28x28 pixel image (total 784 pixels), and column `784` contains the corresponding label (the actual digit).
* **Feature and Target Separation:**
    * **Features (`X`):** The input features, consisting of the pixel values, are created by dropping the last column (`'784'`) from the DataFrame. The shape of `X` is (60000, 784).
    * **Target (`y`):** The target labels are the values from the `784` column, which contains the unique digits from 0 to 9.
    ```python
    X = df.drop(columns = ['784'])
    y = df['784']
    ```
* **Data Scaling:**
    * **Definition:** Data scaling is a preprocessing technique that transforms features to a common scale. For pixel data, this typically means scaling the values from their original range (0-255) to a new, smaller range like 0-1.
    * **Implementation:** The `MinMaxScaler` from `sklearn.preprocessing` is used to scale the `X` features. This is important for neural networks as it helps the optimization algorithm converge faster.
    ```python
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    Xs = scaler.fit_transform(X) # Xs contains the scaled pixel values
    ```
* **Train-Test Split:**
    * **Definition:** The dataset is split into two subsets: a training set to train the model and a test set to evaluate its performance on unseen data.
    * **Implementation:** `train_test_split` from `sklearn.model_selection` is used to create the `xtrain`, `xtest`, `ytrain`, and `ytest` sets. The training set (`xtrain`) contains 45,000 samples, which is 75% of the total data.
    ```python
    from sklearn.model_selection import train_test_split
    xtrain, xtest, ytrain, ytest = train_test_split(Xs,y)
    ```

***

## 2. Defining the Neural Network Model

A neural network is a powerful type of model for image classification. The script defines a simple, two-layer feed-forward network using Keras.

* **Model Architecture:** The model is a `Sequential` model, which is a linear stack of layers.
    * **First Layer (`Dense`):** This is a fully connected layer with **10 neurons**. The `input_shape=(784,)` parameter explicitly defines the shape of the input data, which corresponds to the 784 pixels of each image. The number of parameters for this layer is 7,850, calculated as `(784 * 10) + 10` (weights + biases).
    * **Output Layer (`Dense`):** This is another fully connected layer with a single neuron (`1`). The number of parameters is 11, calculated as `(10 * 1) + 1` (weights + biases).
    ```python
    from keras import models, layers
    model = models.Sequential()
    model.add(layers.Dense(10 , input_shape = (784,)))
    model.add(layers.Dense(1))
    ```
* **Model Summary:** `model.summary()` displays a table with the layers, their output shapes, and the number of parameters, providing a clear overview of the model's structure.
    * **Total Parameters:** 7,861.
    * **Trainable Parameters:** 7,861.

***

## 3. Compiling and Training the Model

The model must be compiled before it can be trained. Compilation configures the learning process itself.

* **Compilation:** The `model.compile()` method is used to configure the model.
    * **Optimizer:** The `SGD` (Stochastic Gradient Descent) optimizer is chosen with a `learning_rate` of `0.01`.
    * **Loss Function:** `loss = 'mse'` (Mean Squared Error) is specified. This is typically used for regression tasks.
    * **Metrics:** The `accuracy` metric is used to monitor the model's performance during training.
* **Training:** `model.fit()` trains the neural network by iterating over the training data for a number of `epochs`.
    * `epochs=10`: The model will pass over the entire training dataset 10 times.
    * `validation_data=(xtest,ytest)`: The model's performance is also evaluated on the test set after each epoch. This helps in detecting overfitting, which occurs when the model performs well on training data but poorly on unseen data.
    ```python
    from keras import optimizers
    sgd = optimizers.SGD(learning_rate = 0.01)
    model.compile(optimizer = sgd, loss = 'mse', metrics = ['accuracy'])
    model.fit(xtrain,ytrain,
             epochs = 10,
             validation_data = (xtest,ytest))
    ```
    The output of `model.fit()` shows the `loss` and `accuracy` on the training data, as well as the `val_loss` and `val_accuracy` on the validation data, for each epoch, allowing for a detailed observation of the model's learning progress.

***

## 4. Use Cases, Benefits, and Limitations

* **Use Cases:** The techniques demonstrated are foundational for image classification tasks, especially for simple, standardized images like handwritten digits. They are also applicable to other forms of supervised learning where input features are structured numerical arrays.
* **Benefits:** The notebook provides a clear, step-by-step example of a complete deep learning pipeline, from data loading to model training and validation, which is an excellent starting point for learning image classification with Keras.
* **Limitations:**
    * **Incorrect Output Layer:** For a digit classification task with 10 unique digits (0-9), the output layer should have 10 neurons with a `softmax` activation function, not 1 neuron with a linear activation.
    * **Incorrect Loss Function:** The `mse` (Mean Squared Error) loss function is typically used for regression, not multi-class classification. A more appropriate loss function would be `sparse_categorical_crossentropy` or `categorical_crossentropy`.
    * The combination of these two limitations means that while the model will technically train, it is not correctly configured to perform effective digit classification. A proper multi-class setup would be necessary to achieve meaningful results.
