package com.wp161.binarytree;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class BinaryTreeTest {

  private BinaryTree binaryTree;
  private Node root;

  @BeforeEach
  void setUp() {
    root = new Node(10);
    root.setLeft(new Node(5));
    root.setRight(new Node(15));
    binaryTree = new BinaryTree(root);
  }

  @Test
  void getRoot() {
    assertEquals(root, binaryTree.getRoot());
  }

  @Test
  void isBstSuccess() {
    assertTrue(binaryTree.isBst());
  }

  @Test
  void isBstFail() {
    root.setRight(new Node(8));
    binaryTree = new BinaryTree(root);

    assertFalse(binaryTree.isBst());
  }

  @Test
  void getMaxDepth() {
    assertEquals(2, binaryTree.getMaxDepth());

    // Add more levels to the tree and check again
    root.getLeft().setLeft(new Node(3));
    root.getLeft().getLeft().setLeft(new Node(1));
    assertEquals(4, binaryTree.getMaxDepth());
  }

  @Test
  void getMaxValueSuccess() {
    assertEquals(15, binaryTree.getMaxValue());

    // Modify the tree and check the maximum value again
    root.getRight().setRight(new Node(20));
    assertEquals(20, binaryTree.getMaxValue());

    // Add a larger value and check the max
    root.getRight().getRight().setRight(new Node(25));
    assertEquals(25, binaryTree.getMaxValue());
  }

  @Test
  void getMaxValueFailed() {
    BinaryTree emptyTree = new BinaryTree();
    Exception exception = assertThrows(IllegalStateException.class, emptyTree::getMaxValue);
    assertEquals("Tree is empty", exception.getMessage());
  }
}
