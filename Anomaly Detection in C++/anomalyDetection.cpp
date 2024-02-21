#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream> // for std::stringstream
#include <unordered_set>
#include <algorithm> // for std::remove

bool isValidVariableName(const std::string& word) {
    // Check if the word is a valid variable name (not a reserved word or include statement)
    static const std::unordered_set<std::string> reservedWords = {
        "int", "double", "float", "char", "bool",
        "cout", "cin", "printf", "scanf"
    };
    return (reservedWords.find(word) == reservedWords.end() &&
            std::find(word.begin(), word.end(), '<') == word.end() &&
            std::find(word.begin(), word.end(), '>') == word.end());
}

bool hasUninitializedVariable(const std::vector<std::string>& codeLines) {
    std::unordered_set<std::string> initializedVariables;
    for (const std::string& line : codeLines) {
        std::stringstream ss(line);
        std::string word;
        while (ss >> word) {
            if (word == "=") {
                // If an assignment is found, mark the variable as initialized
                ss >> word; // Get the variable name
                if (isValidVariableName(word)) {
                    initializedVariables.insert(word);
                }
            } else if (word == "int" || word == "double" || word == "float" || word == "char" || word == "bool") {
                // If a variable declaration is found, add the variable to the set of initialized variables
                ss >> word; // Get the variable name
                if (isValidVariableName(word)) {
                    initializedVariables.insert(word);
                }
            } else if (word == "delete") {
                // If a delete operation is found, remove the variable from the set of initialized variables
                ss >> word; // Get the variable name
                if (isValidVariableName(word)) {
                    initializedVariables.erase(word);
                }
            } else if (isValidVariableName(word)) {
                // Check if a variable is being accessed without being initialized
                if (initializedVariables.find(word) == initializedVariables.end()) {
                    std::cerr << "Anomaly: Variable '" << word << "' accessed without initialization." << std::endl;
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    std::ifstream inputFile("code.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Error: Unable to open file 'code.txt'." << std::endl;
        return 1;
    }

    std::vector<std::string> code;
    std::string line;

    // Read input code from the file
    while (std::getline(inputFile, line)) {
        code.push_back(line);
        if (code.size() >= 20) {
            break; // Limit to 20 lines
        }
    }

    inputFile.close();

    // Detect data flow anomalies
    if (!hasUninitializedVariable(code)) {
        std::cout << "No data flow anomalies detected." << std::endl;
    }

    return 0;
}
