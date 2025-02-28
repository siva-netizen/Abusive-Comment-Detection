# Abusive Comment Detection

## Project Overview
This project focuses on detecting abusive comments in text, leveraging machine learning techniques to classify comments into various categories of toxicity. A deep learning approach using LSTMs (Long Short-Term Memory networks) has been implemented to process and classify comments efficiently. The application includes a user-friendly interface built using Gradio.

---

## Architecture

1. **Dataset**: `comments.csv` contains inputs and labels.
   - **Source**: [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
   - **Size**: 159,571 rows, 8 columns
   - **Columns**:
     - `id`: Unique identifier for the comment
     - `comment_text`: Text content of the comment
     - `toxic`: Binary label indicating toxic content
     - `severe_toxic`: Binary label indicating severely toxic content
     - `obscene`: Binary label for obscene content
     - `threat`: Binary label for threats
     - `insult`: Binary label for insults
     - `identity_hate`: Binary label for identity-based hate

2. **Processing Flow**:
   - **Inputs**: Comments from the dataset
   - **Labels**: Corresponding categories of toxicity
   - **Preprocessing**:
     - Tokenization and embedding of text features
   - **Deep Neural Network (DNN)**: LSTM model for classification
   - **Gradio Interface**: Simplified UI for model interaction

---

## Implementation Details

### 1. Preprocessing

#### Text Vectorization
A preprocessing layer maps text features to integer sequences:
- **Outcome**:
  - `Vectorized_text`: Shape (159,571, 1800)
  - *Note*: 1800 represents the maximum length of input text sequences.

### 2. TensorFlow Data Pipeline
The dataset is processed as a TensorFlow pipeline for efficient data loading:
```python
import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices((vectorized_text, y))
dataset = dataset.cache()
dataset = dataset.shuffle(160000)
dataset = dataset.batch(16)
dataset = dataset.prefetch(8)
```

### 3. Train, Validation, and Test Splits
- **Total dataset batches**: 9,974
  - **Train**: 70% (6,981 batches)
  - **Validation**: 20% (1,994 batches)
  - **Test**: 10% (997 batches)

### 4. Building the Deep Neural Network (DNN)

To capture relationships between words, word embeddings are used. These embeddings are learned automatically during training, extracting meaningful features from the input text.

#### Model Summary:
- **Loss Function**: Binary Cross-Entropy
- **Optimizer**: Adam
- **Early Stopping**:
  - Patience: 3 epochs
- **Epochs**: 10 (due to time constraints)

---

## Results

### Training Performance
After 10 epochs, the training process showed a clear reduction in loss, as observed in the loss curve:

![Loss Curve](https://github.com/user-attachments/assets/89a071b9-1c93-48f5-992f-6adc9d13398d)

### Evaluation Metrics
- **Precision**: 92.19%
- **Recall**: 90.51%
- **Accuracy**: 50.75%
  
*Note*: The accuracy metric appears low due to the imbalanced nature of the dataset. Precision and recall are more reliable indicators in this context.

---

## Future Improvements
- **Model Optimization**:
  - Increase training epochs to allow the model to converge further.
  - Experiment with advanced architectures (e.g., BERT, GPT).
- **Data Augmentation**:
  - Use data augmentation techniques to address class imbalances.
- **UI Enhancements**:
  - Add more interactive features to the Gradio interface.
- **Deployment**:
  - Deploy the model as a web service using Flask/Django.

---

## Usage Instructions

### Dependencies
- Python 3.8+
- TensorFlow 2.x
- Gradio 3.x
- Pandas, NumPy, Matplotlib

### Running the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/abusive-comment-detection.git
   cd abusive-comment-detection
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```



---

## References
- [Jigsaw Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)
- TensorFlow Documentation
- Gradio Documentation

