
# Taylor Series Approximation App

A Python-based application that approximates a given function using its Taylor Series expansion. The app allows users to input a function, define the degree of the Taylor Series, specify the window of the graph, and choose the center point for the approximation. It then plots the original function alongside its Taylor Series approximation.

---

## Features

- **Interactive Input**: Users can input any valid mathematical function of \(x\), define the degree of the Taylor Series, and set the graphing window.
- **Custom Taylor Series Center**: The app allows users to choose the center point \(a\) for the Taylor Series expansion.
- **Graphical Output**: The app plots the original function and its Taylor Series approximation on the same graph for comparison.
- **Numerical Approximation**: It prints out the Taylor Series expansion without the higher-order terms (using `removeO()`).

---

## Screenshots

![Taylor Series Screenshot 1](https://github.com/user-attachments/assets/c5baebdf-2273-47ca-8135-544a8c20e463)

![Taylor Series Screenshot 2](https://github.com/user-attachments/assets/26e7cbeb-0443-446c-83a3-7b8b8bede85c)

---

## How It Works

1. **Input a Function**: Enter a function in terms of \(x\) (e.g., `sin(x)`, `x**2 + x`, `e**x`, etc.). The app automatically formats the input for processing.
2. **Taylor Series Degree**: Choose the degree of the Taylor Series for approximation.
3. **Graphing Window**: Define the graph window by specifying the minimum and maximum values for both the \(x\) and \(y\) axes.
4. **Center Point**: Input the center point \(a\) around which the Taylor Series will be expanded.
5. **Visualization**: The app will plot the original function and its Taylor Series approximation in the specified window.
<img width="380" alt="image" src="https://github.com/user-attachments/assets/aa74dcc8-36b6-43bf-b793-1aa5da0a6e6a">

<img width="185" alt="image" src="https://github.com/user-attachments/assets/932db659-b3b7-4ccc-be82-779d501d9652">


---

## Installation

### Prerequisites

- Python 3.x
- Required libraries: `matplotlib`, `numpy`, `sympy`

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/taylor-series-app.git
   pip install matplotlib numpy sympy
   python taylor_series_app.py
