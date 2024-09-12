package com.wp161.binarytree;

/**
 * The BinaryTree class represents a binary tree, where each node has a left and right child.
 * The tree supports operations like checking if it's a binary search tree (BST),
 * calculating its maximum depth, and finding the maximum value within the tree.
 */
public class BinaryTree {

  /** The root node of the binary tree. */
  private Node root;

  /**
   * Constructs a binary tree with the specified root node.
   *
   * @param root the root node of the binary tree
   */
  public BinaryTree(Node root) {
    this.root = root;
  }

  /**
   * Constructs an empty binary tree (i.e., a tree with no nodes).
   */
  public BinaryTree() {
    this.root = null;
  }

  /**
   * Returns the root node of the binary tree.
   *
   * @return the root node of the tree, or null if the tree is empty
   */
  public Node getRoot() {
    return root;
  }

  /**
   * Checks if the binary tree is a binary search tree (BST).
   * A binary search tree is a binary tree in which, for every node n,
   * all nodes in the left subtree have values less than n's value,
   * and all nodes in the right subtree have values greater than n's value.
   *
   * @return true if the tree is a BST, false otherwise
   */
  public boolean isBst() {
    return isBstHelper(root, null, null);
  }

  /**
   * Helper method to check if the tree is a binary search tree (BST) within a given range.
   *
   * @param node the current node being checked
   * @param min  the minimum allowable value for the current node (null if unbounded)
   * @param max  the maximum allowable value for the current node (null if unbounded)
   * @return true if the subtree rooted at this node is a BST, false otherwise
   */
  private boolean isBstHelper(Node node, Integer min, Integer max) {
    if (node == null) {
      return true; // An empty tree is a valid BST
    }

    if ((min != null && node.getValue() <= min) || (max != null && node.getValue() >= max)) {
      return false;
    }

    return isBstHelper(node.getLeft(), min, node.getValue())
        && isBstHelper(node.getRight(), node.getValue(), max);
  }

  /**
   * Returns the maximum depth of the binary tree. The maximum depth is the longest path
   * from the root node to a leaf node.
   *
   * @return the maximum depth of the tree
   */
  public Integer getMaxDepth() {
    return getHeight(root);
  }

  /**
   * Helper method to calculate the height of the tree.
   *
   * @param node the current node whose height is being calculated
   * @return the height of the subtree rooted at this node, or 0 if the node is null
   */
  private Integer getHeight(Node node) {
    if (node == null) {
      return 0; // Base case: an empty subtree has height 0
    }

    return 1 + Math.max(getHeight(node.getLeft()), getHeight(node.getRight()));
  }

  /**
   * Returns the maximum value held in the binary tree.
   *
   * @return the maximum integer value in the tree
   * @throws IllegalStateException if the tree is empty
   */
  public Integer getMaxValue() {
    if (root == null) {
      throw new IllegalStateException("Tree is empty");
    }
    return getMaxValueHelper(root);
  }

  /**
   * Helper method to recursively find the maximum value in the tree.
   *
   * @param node the current node being checked
   * @return the maximum value in the subtree rooted at this node
   */
  private Integer getMaxValueHelper(Node node) {
    if (node == null) {
      return Integer.MIN_VALUE;
    }

    int leftMax = getMaxValueHelper(node.getLeft());
    int rightMax = getMaxValueHelper(node.getRight());

    return Math.max(node.getValue(), Math.max(leftMax, rightMax));
  }
}
