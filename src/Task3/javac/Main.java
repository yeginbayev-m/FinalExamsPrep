import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите текст:");
        String text = scanner.nextLine();

        String[] words = text.split(" ");
        ArrayList<String> filteredWords = new ArrayList<>();

        int wordIndex = 0;
        while (wordIndex < words.length) {
            String word = words[wordIndex];

            if (!word.contains("ка")) {
                filteredWords.add(word);
            }

            wordIndex = wordIndex + 1;
        }

        // Собираем результат в строку
        StringBuilder resultText = new StringBuilder();
        for (int i = 0; i < filteredWords.size(); i++) {
            resultText.append(filteredWords.get(i));
            if (i < filteredWords.size() - 1) {
                resultText.append(" ");
            }
        }

        System.out.println("\nИсходный текст:");
        System.out.println(text);

        System.out.println("\nРезультат после удаления слов, содержащих 'ка':");
        System.out.println(resultText.toString());

        scanner.close();
    }
}
