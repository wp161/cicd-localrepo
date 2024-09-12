# Binary Tree Library
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xROpBYU4)

A Java library for creating and manipulating binary trees. This library provides functionality for:
- Checking if a binary tree is a binary search tree (BST).
- Calculating the maximum depth of a binary tree.
- Finding the maximum value in a binary tree.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation/ JavaDoc](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Binary Search Tree (BST) Validation**: Determines if a binary tree satisfies the properties of a binary search tree.
- **Maximum Depth Calculation**: Finds the longest path from the root to any leaf node.
- **Maximum Value Calculation**: Retrieves the highest integer value in the tree.

## Installation

### Prerequisites

To use this library, you need:
- Java 17 or higher
- Gradle (for building)

### Building the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/wp161/binarytree.git
   ```
2. Build the project using Gradle
   ```bash
   ./gradlew doAll
   ```
## Usage
Here’s an example of how you can use the Binary Tree library in your Java project.

### Create a Binary Tree
```java
import com.wp161.binarytree.*;

public class Main {
  public static void main(String[] args) {
    // Create nodes
    Node root = new Node(10);
    root.setLeft(new Node(5));
    root.setRight(new Node(15));

    // Create a binary tree with root
    BinaryTree tree = new BinaryTree(root);

    // Check if the tree is a BST
    System.out.println("Is BST? " + tree.isBst());
    // output: Is BST? true

    // Get the maximum depth of the tree
    System.out.println("Max Depth: " + tree.getMaxDepth());
    // output: Max Depth: 2

    // Find the maximum value in the tree
    System.out.println("Max Value: " + tree.getMaxValue());
    // output: Max Value: 15
  }
}
```

### Handling an Empty Tree
You can also handle an empty tree:
```java
BinaryTree emptyTree = new BinaryTree();
try {
    emptyTree.getMaxValue(); // This will throw an exception
} catch (IllegalStateException e) {
    System.out.println(e.getMessage()); // Output: Tree is empty
    }
```

## API Documentation/ JavaDoc
To generate the API documentation, run the following command:
```bash
./gradlew javadoc
```
The generated documentation will be located in the `build/docs/javadoc` directory.

## Contributing
Contributions are welcome! Here’s how you can contribute:
1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes.
4. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
5. Push to the branch:
   ```bash
   git push origin feature-name
      ```
6. Open a pull request.

Please ensure your code follows the project’s style and that tests are written for any new functionality.

### Code Style
We use `checkstyle` for consistent code formatting. Please ensure your code passes `checkstyle` checks by running `./gradlew check`.

### Running Tests
You can run the unit tests using Gradle:
```bash
./gradlew test
```
## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.