import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.lang.*;

/**
 * The Main class implements an application that reads lines from the standard input
 * and prints them to the standard output.
 */

public class Main {
  protected static class Node {
    String currency;
    double val;
    Node (String currency, double val) {
      this.currency = currency;
      this.val = val;
    }
  }

  protected static double[] max = new double[]{-1}; // initial the double that stores the maximum transaction value achived
  private static double find(HashMap<String, ArrayList<Node>> map, String original, String target, double value, HashSet<String> visited) {
      if (visited.contains(original)) return -1;  // if got into a loop
      if (!map.containsKey(original)) return -1;   // if origianl doens't exist


      if (original.equals(target)) return value;   // if found the target
      visited.add(original);
      // iterate through all possible transaction
      for (Node next : map.get(original)) {
        double sub = find(map, next.currency, target, value * next.val, visited);
        max[0] = Math.max(max[0], sub); // update the max value
      }
      visited.remove(original);
      return max[0];
    }

  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    HashMap<String, ArrayList<Node>> map = new HashMap<>(); // store all the correncies and it's forwarding currency
    int counter = 0;
    String original = ""; // store the original currency
    String target = ""; // store the targte currency
    ArrayList<String> separate = new ArrayList<>(); // store the separated transactions in line 0
    while ((line = in.readLine()) != null) {
      // get all transaction rates
      if (counter == 0) {
        String[] temp = line.split(";");
        for (String s : temp) {
          separate.add(s);
        }
      } else if (counter == 1) {
        original = line;
      } else {
        target = line;
      }
      counter ++;
    }

    for (String s : separate) {
      String[] trans = s.split(",");
      String from = trans[0];
      String to = trans[1];
      Double value = Double.parseDouble(trans[2]);
      // create a new node for original if doesn't exist
      if (!map.containsKey(from)) {
        map.put(from, new ArrayList<>());
      }
      // connect original to target
      map.get(from).add(new Node(to, value));
      if (!map.containsKey(to)) {
        map.put(to, new ArrayList<>());
      }
    }

    System.out.println(find(map, original, target, 1, new HashSet<>()));

  }
}



