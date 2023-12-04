# Image Generation from Textual Queries Project

## Project Overview

This educational project focuses on building a basic neural network capable of generating images based on textual queries. The input to the system is a text that is transformed into a TF-IDF matrix. This matrix is then fed into a neural network, generating an array of pixels as output, which is further transformed into an image. The project utilizes libraries such as TensorFlow, Keras, and scikit-learn.

## Functionality

- **Text Input:**
  - The user provides a textual query as input.

- **Text Preprocessing:**
  - The text undergoes preprocessing steps, including converting to lowercase, removing stop words, and lemmatization.

- **TF-IDF Matrix:**
  - The preprocessed text is transformed into a TF-IDF matrix.

- **Neural Network:**
  - A simple neural network is employed, taking the TF-IDF matrix as input and generating an array of pixels as output.

- **Image Generation:**
  - The pixel array is transformed into an image.

## Implementation Details

### Libraries Used
- TensorFlow
- Keras
- Scikit-Learn
- Image
- Numpy

### Text Preprocessing
- Lowercasing
- Tokenization
- Stop word removal
- Lemmatization

### Neural Network
- A simple fully connected neural network architecture is implemented to generate images.

## Conclusion

This project aims to provide a fundamental understanding of image generation from textual queries using a simple neural network. The use of TF-IDF matrices and text preprocessing techniques contributes to the overall learning experience.

