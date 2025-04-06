import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.lang.*;

/**
 * BlackRock 货币汇率转换题
 * 输入格式：
 * 第一行：货币对和汇率，如 "USD,EUR,1.1;EUR,GBP,0.8"
 * 第二行：起始货币
 * 第三行：目标货币
 */
public class Main {
    /**
     * 货币节点类
     * currency: 目标货币
     * val: 对应的汇率
     */
    protected static class Node {
        String currency;
        double val;
        Node (String currency, double val) {
            this.currency = currency;
            this.val = val;
        }
    }

    // 存储最大汇率值，使用数组便于在递归中修改
    protected static double[] max = new double[]{-1};

    /**
     * DFS查找货币转换路径
     * @param map 货币转换关系图
     * @param original 当前货币
     * @param target 目标货币
     * @param value 当前累积的汇率值
     * @param visited 已访问的货币集合
     * @return 最大可能的汇率值，-1表示无法转换
     */
    private static double find(HashMap<String, ArrayList<Node>> map, 
                             String original, 
                             String target, 
                             double value, 
                             HashSet<String> visited) {
        if (visited.contains(original)) return -1;  // 检测到循环转换
        if (!map.containsKey(original)) return -1;  // 当前货币不存在转换关系
        if (original.equals(target)) return value;  // 找到目标货币

        visited.add(original);  // 标记当前货币为已访问
        
        // 遍历所有可能的转换路径
        for (Node next : map.get(original)) {
            double sub = find(map, next.currency, target, value * next.val, visited);
            max[0] = Math.max(max[0], sub);  // 更新最大汇率值
        }
        
        visited.remove(original);  // 回溯：移除访问标记
        return max[0];
    }

    public static void main(String[] args) throws IOException {
        // 设置输入流
        InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
        BufferedReader in = new BufferedReader(reader);
        String line;
        
        // 存储货币转换关系的图
        HashMap<String, ArrayList<Node>> map = new HashMap<>();
        int counter = 0;  // 记录读取的行数
        String original = "";  // 起始货币
        String target = "";    // 目标货币
        ArrayList<String> separate = new ArrayList<>();  // 存储第一行分割后的转换关系

        // 读取输入
        while ((line = in.readLine()) != null) {
            if (counter == 0) {  // 第一行：货币对和汇率
                String[] temp = line.split(";");
                for (String s : temp) {
                    separate.add(s);
                }
            } else if (counter == 1) {  // 第二行：起始货币
                original = line;
            } else {  // 第三行：目标货币
                target = line;
            }
            counter++;
        }

        // 构建货币转换图
        for (String s : separate) {
            String[] trans = s.split(",");
            String from = trans[0];    // 起始货币
            String to = trans[1];      // 目标货币
            Double value = Double.parseDouble(trans[2]);  // 汇率

            // 为起始货币创建邻接表
            if (!map.containsKey(from)) {
                map.put(from, new ArrayList<>());
            }
            // 添加转换关系
            map.get(from).add(new Node(to, value));
            
            // 确保目标货币在图中存在（即使暂时没有出边）
            if (!map.containsKey(to)) {
                map.put(to, new ArrayList<>());
            }
        }

        // 查找并输出最优汇率
        System.out.println(find(map, original, target, 1, new HashSet<>()));
    }
}



