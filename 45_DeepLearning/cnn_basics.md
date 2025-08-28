Multi-Layer Perceptron (MLP) models and Convolutional Neural Networks (CNNs) for image processing

  * **MLP Limitations:** MLPs struggle with image structure because they flatten 2D image data into 1D, losing spatial relationships between pixels. This makes them unsuitable for tasks like signature recognition where spatial information is crucial.
  * **Introduction to CNNs:** CNNs address these limitations by processing images as 2D data, preserving spatial relationships and allowing them to learn features based on what is above, below, left, and right of specific elements.
  * **Convolutional Layer Mechanics:**
      * They use "filters" or "kernels" (small 2D matrices with trainable weights) that slide across the input image.
      * A weighted sum operation produces a single value for each position, generating a new 2D output.
      * **Padding:** To prevent information loss and maintain the original input size, zero-value layers are added around the image.
      * **Multiple Kernels:** Using multiple kernels (e.g., 16 or 32) creates multiple output layers, enhancing feature learning and increasing the number of trainable weights. The number of kernels can be adjusted to combat overfitting or underfitting.
  * **Pooling Layers (Max Pooling/Average Pooling):**
      * These layers reduce the dimensionality of feature maps while retaining important information.
      * **Max pooling:** Extracts the maximum value from a defined matrix (e.g., 2x2).
      * **Average pooling:** Calculates the average value from a defined matrix.
      * This process compresses data without significant information loss because the depth of the data has already been increased by multiple kernels.
  * **Fully Connected Layer (FCN):**
      * After several convolutional and pooling layers, the high-dimensional data is flattened into a Fully Connected Layer.
      * Each neuron in the FCN represents structured information about multiple cells from previous layers.
      * This FCN then learns additional weights to perform the final image recognition task.
  * **Case Study (Cat and Dog Image Recognition):** The AI Council proposed a case study for Sunil to perform "feature engineering" for cat and dog image recognition. This involves reading images from separate "cat" and "dog" folders and storing their features into an array as a crucial initial data processing step before building and training the CNN model.
