import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(42)
    weights_input_hidden = np.random.rand(input_size, hidden_size)
    weights_hidden_output = np.random.rand(hidden_size, output_size)
    bias_hidden = np.zeros((1, hidden_size))
    bias_output = np.zeros((1, output_size))

    return weights_input_hidden, weights_hidden_output, bias_hidden, bias_output

def forward_propagation(X, weights_input_hidden, weights_hidden_output, bias_hidden, bias_output):
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(output_layer_input)

    return hidden_layer_output, predicted_output

def backpropagation(X, y, hidden_layer_output, predicted_output,
                    weights_input_hidden, weights_hidden_output,
                    bias_hidden, bias_output, learning_rate):
    error_output = y - predicted_output
    delta_output = error_output * sigmoid_derivative(predicted_output)

    error_hidden = delta_output.dot(weights_hidden_output.T)
    delta_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)

    weights_hidden_output += hidden_layer_output.T.dot(delta_output) * learning_rate
    weights_input_hidden += X.T.dot(delta_hidden) * learning_rate

    bias_output += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

    return weights_input_hidden, weights_hidden_output, bias_hidden, bias_output

def train_neural_network(X, y, hidden_size, epochs, learning_rate):
    input_size = X.shape[1]
    output_size = y.shape[1]

    weights_input_hidden, weights_hidden_output, bias_hidden, bias_output = initialize_parameters(input_size, hidden_size, output_size)

    for epoch in range(epochs):
        hidden_layer_output, predicted_output = forward_propagation(X, weights_input_hidden, weights_hidden_output, bias_hidden, bias_output)
        weights_input_hidden, weights_hidden_output, bias_hidden, bias_output = backpropagation(X, y, hidden_layer_output, predicted_output,
                                                                                                weights_input_hidden, weights_hidden_output,
                                                                                                bias_hidden, bias_output, learning_rate)

        if epoch % 1000 == 0:
            loss = np.mean(np.square(y - predicted_output))
            print(f"Epoch {epoch}, Loss: {loss}")

    return weights_input_hidden, weights_hidden_output, bias_hidden, bias_output

# Example usage:
# XOR dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Train the neural network
hidden_size = 4
epochs = 10000
learning_rate = 0.1

trained_parameters = train_neural_network(X, y, hidden_size, epochs, learning_rate)

# Test the neural network
_, predicted_output = forward_propagation(X, *trained_parameters)

print("\nFinal Predictions:")
print(predicted_output)
