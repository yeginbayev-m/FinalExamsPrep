#include <iostream>
#include <vector>
#include <string>
#include <windows.h>

using namespace std;

int main() {
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);
    string text;
    cout << "Введите текст: ";
    // Текст: Практический опыт показывает, что рамки и место обучения кадров позволяет оценить значение ключевых компонентов планируемого...
    getline(cin, text);  // Считывание текста от пользователя

    vector<string> words;
    string current_word = "";

    // Разделение текста на слова вручную
    for (size_t i = 0; i < text.length(); ++i) {
        char current_char = text[i];

        if (current_char != ' ') {
            current_word += current_char;
        } else {
            if (!current_word.empty()) {
                words.push_back(current_word);
                current_word = "";
            }
        }
    }

    // Добавление последнего слова (если оно не было добавлено)
    if (!current_word.empty()) {
        words.push_back(current_word);
    }

    // Фильтрация слов по наличию слога (подстроки) "ка"
    vector<string> filtered_words;
    for (size_t i = 0; i < words.size(); ++i) {
        if (words[i].find("ка") == string::npos) {
            filtered_words.push_back(words[i]);
        }
    }

    // Сборка отфильтрованных слов обратно в строку
    string result_text = "";
    for (size_t i = 0; i < filtered_words.size(); ++i) {
        result_text += filtered_words[i];
        if (i < filtered_words.size() - 1) {
            result_text += " ";
        }
    }

    // Вывод результата
    cout << "\nИсходный текст:\n" << text << endl;
    cout << "\nРезультат после удаления слов, содержащих \"ка\":\n" << result_text << endl;

    return 0;
}
