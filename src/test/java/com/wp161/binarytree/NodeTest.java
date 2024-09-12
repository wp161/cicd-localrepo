package com.wp161.binarytree;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class NodeTest {

  private Node node;
  private Node leftChild;
  private Node rightChild;

  @BeforeEach
  void setUp() {
    // Initialize the node and its children before each test
    node = new Node(10);
    leftChild = new Node(5);
    rightChild = new Node(15);
  }

  @Test
  void testConstructorFail() {
    // Test that constructor throws an exception when given a null value
    Exception exception = assertThrows(IllegalArgumentException.class, () -> {
      new Node(null);
    });
    assertEquals("Node value cannot be null", exception.getMessage());
  }

  @Test
  void getValue() {
    assertEquals(10, node.getValue());
  }

  @Test
  void setValue() {
    node.setValue(20);
    assertEquals(20, node.getValue());
  }

  @Test
  void getLeft() {
    assertNull(node.getLeft());

    node.setLeft(leftChild);
    assertEquals(leftChild, node.getLeft());
  }

  @Test
  void setLeft() {
    node.setLeft(leftChild);
    assertEquals(leftChild, node.getLeft());
  }

  @Test
  void getRight() {
    assertNull(node.getRight());

    node.setRight(rightChild);
    assertEquals(rightChild, node.getRight());
  }

  @Test
  void setRight() {
    node.setRight(rightChild);
    assertEquals(rightChild, node.getRight());
  }

  @Test
  void isLeaf() {
    // Test that a node with no children is a leaf
    assertTrue(node.isLeaf());

    // Test that a node with children is not a leaf
    node.setLeft(leftChild);
    assertFalse(node.isLeaf());
    node.setRight(rightChild);
    assertFalse(node.isLeaf());
  }

  @Test
  void testToString() {
    // Test that the toString method returns the correct representation
    String expected = "Node{value=10, left=null, right=null}";
    assertEquals(expected, node.toString());

    // Test after setting left and right children
    node.setLeft(leftChild);
    node.setRight(rightChild);
    expected = "Node{value=10, left=Node{value=5, left=null, right=null}, right=Node{value=15, "
        + "left=null, right=null}}";
    assertEquals(expected, node.toString());
  }

  @Test
  void testEquals() {
    // Test equality between nodes
    Node anotherNode = new Node(10);
    assertEquals(node, anotherNode); // Same value, should be equal

    // Test inequality when values are different
    anotherNode.setValue(20);
    assertNotEquals(node, anotherNode); // Different values, not equal

    // Test equality when both nodes have the same left and right children
    node.setLeft(leftChild);
    node.setRight(rightChild);
    anotherNode.setValue(10);
    anotherNode.setLeft(new Node(5));
    anotherNode.setRight(new Node(15));
    assertEquals(node, anotherNode); // Should be equal when structure and values are the same

    // Test inequality when left and right children are different
    anotherNode.setRight(new Node(12)); // Change one child
    assertNotEquals(node, anotherNode); // Not equal
  }

  @Test
  void testHashCode() {
    // Test that nodes with the same structure and values have the same hash code
    Node anotherNode = new Node(10);
    assertEquals(node.hashCode(), anotherNode.hashCode());

    // Test after setting left and right children
    node.setLeft(leftChild);
    node.setRight(rightChild);
    anotherNode.setLeft(new Node(5));
    anotherNode.setRight(new Node(15));
    assertEquals(node.hashCode(), anotherNode.hashCode());

    // Test that different structures result in different hash codes
    anotherNode.setRight(new Node(12));
    assertNotEquals(node.hashCode(), anotherNode.hashCode());
  }

}
