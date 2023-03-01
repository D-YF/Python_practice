import java.util.*;

public class BinaryTree {
    /*
     * Create
     * Search
     * Preorder   Traversal
     * In order   Traversal
     * Post order Traversal
     */

    Node root;
    BinaryTree(){
        root = null;
    }

    void IterativePreorder(Node root){
        if(root==null){
            System.out.println("The root is empty");
            return;
        }
        Stack<Node> stack = new Stack<Node>();
        stack.push(root);

        while(stack.isEmpty() == false){
            Node node = stack.pop();
            System.out.print(node.key);
            if (node.right != null)
                stack.push(node.right);
            if (node.left != null)
                stack.push(node.left);
        }
        System.out.println();
    }

    void IterativeInorder(Node root){
        if(root==null){
            System.out.println("The root is empty");
            return;
        }

        Stack<Node> stack = new Stack<Node>();
        stack.push(root);
        while(stack.isEmpty()==false){
            Node cur = stack.pop();

            if (cur==null){
                Node printCur = stack.pop();
                System.out.print(printCur.key);
                continue;
            }

            if(cur.right != null){
                stack.push(cur.right);
            }
            stack.push(cur);
            stack.push(null);
            if (cur.left != null){
                stack.push(cur.left);
            }

        }
        System.out.println();
    }

    void IterativePostorder(Node node){
        if (node==null){
            System.out.println("The tree is empty!");
            return;
        }

        Stack<Node> stack = new Stack<Node>();
        stack.push(node);
        while(! stack.isEmpty()){
            Node cur = stack.pop();

            if(cur==null){
                Node printCur = stack.pop();
                System.out.print((printCur.key));
                continue;
            }

            if(cur.right != null){
                stack.push(cur.right);
            }
            if(cur.left != null){
                stack.push(cur.left);
            }
            stack.push(cur);
            stack.push(null);
        }

    }


    void printInorder(Node node){
        if (node==null)
            return;
        
        printInorder(node.left);
        System.out.print(node.key+" ");
        printInorder(node.right);
    }

    void printPreorder(Node node){
        if (node==null)
            return;
        
        System.out.print(node.key+" ");
        printPreorder(node.left);
        printPreorder(node.right);
    }

    void printPostorder(Node node){
        if (node==null)
            return;
        printPostorder(node.left);
        printPostorder(node.right);
        System.out.print(node.key+" ");
    }

    // void IterativePreorder(Node node){
    //     if (node==null)
    //         return;

    //     Stack<Node> stack = new Stack<Node>();
    //     stack.push(node);
    //     while(!stack.isEmpty()){
    //         Node cur = stack.pop();
    //         System.out.print(cur.key + " ");
    //         if(cur.right != null)
    //             stack.push(cur.right);
    //         if(cur.left != null)
    //             stack.push(cur.left);
    //     }


    // }


    public void BFS(Node node){
        // O(N) and O(N)
        if(node==null){
            System.out.println("The root is empty");
            return;
        }
        Queue<Node> queue = new LinkedList<Node>();
        queue.add(node);

        while(! queue.isEmpty()){
            int N = queue.size();
            for (int i=0; i<N; i++){
                Node cur = queue.poll();
                System.out.print(cur.key);
                if (cur.left != null){
                    queue.add(cur.left);
                }

                if (cur.right != null){
                    queue.add(cur.right);
                }
            }
            System.out.println();

        }
    }

    public static void main(String args[]){
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(5);
        tree.root.right.left = new Node(6);
 
        System.out.println("In order:");
        tree.printInorder(tree.root);
        System.out.println();

        System.out.println("Preorder:");
        tree.printPreorder(tree.root);
        System.out.println();

        System.out.println("Post order:");
        tree.printPostorder(tree.root);
        System.out.println();

        System.out.println("Level traversal:");
        tree.BFS(tree.root);

        System.out.println("Iteratively Preorder traversal:");
        tree.IterativePreorder(tree.root);

        System.out.println("Iteratively Inorder traversal:");
        tree.IterativeInorder(tree.root);

        System.out.println("Iteratively Possorder traversal:");
        tree.IterativePostorder(tree.root);


    }

}


class Node{
    int key;
    Node left, right;

    public Node(int item){
        key = item;
        left = right = null;
    }
}