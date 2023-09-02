import numpy as np

# Define the sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Create a simple feedforward neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.uniform(-1, 1, (self.input_size, self.hidden_size))
        self.bias_hidden = np.zeros((1, self.hidden_size))
        self.weights_hidden_output = np.random.uniform(-1, 1, (self.hidden_size, self.output_size))
        self.bias_output = np.zeros((1, self.output_size))

    def forward(self, inputs):
        # Forward pass through the network
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output_layer_output = sigmoid(self.output_layer_input)
        return self.output_layer_output

    def train(self, inputs, targets, learning_rate):
        # Forward pass
        self.output = self.forward(inputs)

        # Calculate the error
        error = targets - self.output

        # Backpropagation
        delta_output = error * sigmoid_derivative(self.output)
        error_hidden = delta_output.dot(self.weights_hidden_output.T)
        delta_hidden = error_hidden * sigmoid_derivative(self.hidden_layer_output)

        # Update weights and biases
        self.weights_hidden_output += self.hidden_layer_output.T.dot(delta_output) * learning_rate
        self.bias_output += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += inputs.T.dot(delta_hidden) * learning_rate
        self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

    def predict(self, inputs):
        # Make predictions
        return self.forward(inputs)

# Example usage:
if __name__ == "__main__":
    # Create a simple dataset for binary classification
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    # Initialize the neural network
    input_size = 2
    hidden_size = 4
    output_size = 1
    learning_rate = 0.1

    nn = NeuralNetwork(input_size, hidden_size, output_size)

    # Train the neural network
    epochs = 10000
    for i in range(epochs):
        nn.train(X, y, learning_rate)

    # Make predictions
    predictions = nn.predict(X)
    print("Predictions:")
    print(predictions)
