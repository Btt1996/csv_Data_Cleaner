import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class CSVAnalyzer {
    
    private final String filePath;
    private final String delimiter;

    public CSVAnalyzer(String filePath, String delimiter) {
        this.filePath = filePath;
        this.delimiter = delimiter;
    }

    public void analyze() {
        Map<String, Integer> valueCounts = new HashMap<>();
        int totalRows = 0;
        int nonEmptyRows = 0;
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                totalRows++;
                if (!line.trim().isEmpty()) {
                    nonEmptyRows++;
                    String[] values = line.split(delimiter);
                    for (String value : values) {
                        valueCounts.put(value, valueCounts.getOrDefault(value, 0) + 1);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Total number of rows: " + totalRows);
        System.out.println("Number of non-empty rows: " + nonEmptyRows);
        System.out.println("Number of unique values:");
        for (Map.Entry<String, Integer> entry : valueCounts.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }

    public static void main(String[] args) {
        CSVAnalyzer analyzer = new CSVAnalyzer("data/cleaned_data.csv", ",");
        analyzer.analyze();
    }
}
