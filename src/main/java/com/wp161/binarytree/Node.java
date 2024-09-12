package com.wp161.binarytree;

import java.util.Objects;

/**
 * The Node class represents a single node in a binary tree.
 * Each node contains an integer value, a reference to its left child,
 * and a reference to its right child.
 */
public class Node {
  /** The integer value stored in this node. */
  private Integer value;
  /** The left child of this node. */
  private Node left;
  /** The right child of this node. */
  private Node right;

  /**
   * Constructs a new Node with a given integer value.
   *
   * @param value the integer value to be stored in the node, must not be null
   * @throws IllegalArgumentException if the value is null
   */
  public Node(Integer value) {
    if (!isValidValue(value)) {
      throw new IllegalArgumentException("Node value cannot be null");
    }
    this.value = value;
  }

  /**
   * Validates if the given value is not null.
   *
   * @param value the value to be validated
   * @return true if the value is not null, false otherwise
   */
  private boolean isValidValue(Integer value) {
    return value != null;
  }

  /**
   * Returns the integer value stored in this node.
   *
   * @return the value of the node
   */
  public Integer getValue() {
    return value;
  }

  /**
   * Sets the integer value of this node.
   *
   * @param value the new integer value to be set
   */
  public void setValue(Integer value) {
    this.value = value;
  }

  /**
   * Returns the left child of this node.
   *
   * @return the left child node, or null if no left child exists
   */
  public Node getLeft() {
    return left;
  }

  /**
   * Sets the left child of this node.
   *
   * @param left the node to be set as the left child
   */
  public void setLeft(Node left) {
    this.left = left;
  }

  /**
   * Returns the right child of this node.
   *
   * @return the right child node, or null if no right child exists
   */
  public Node getRight() {
    return right;
  }

  /**
   * Sets the right child of this node.
   *
   * @param right the node to be set as the right child
   */
  public void setRight(Node right) {
    this.right = right;
  }

  /**
   * Determines if this node is a leaf node.
   * A node is considered a leaf node if it has no left or right children.
   *
   * @return true if the node is a leaf (both left and right children are null), false otherwise
   */
  public boolean isLeaf() {
    return left == null && right == null;
  }

  /**
   * Returns a string representation of the node, including its value, left child, and right child.
   *
   * @return a string representation of this node
   */
  @Override
  public String toString() {
    return "Node{"
        + "value=" + value
        + ", left=" + left
        + ", right=" + right
        + '}';
  }

  /**
   * Compares this node to another object for equality.
   * Two nodes are considered equal if they have the same value, left child, and right child.
   *
   * @param o the object to compare to
   * @return true if the nodes are equal, false otherwise
   */
  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Node node = (Node) o;
    return Objects.equals(getValue(), node.getValue())
        && Objects.equals(getLeft(), node.getLeft())
        && Objects.equals(getRight(), node.getRight());
  }

  /**
   * Returns a hash code value for this node.
   * The hash code is generated based on the node's value, left child, and right child.
   *
   * @return the hash code value for this node
   */
  @Override
  public int hashCode() {
    return Objects.hash(getValue(), getLeft(), getRight());
  }
}