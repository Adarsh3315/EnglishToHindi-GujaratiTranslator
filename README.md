# English To Hindi-Gujarati Translator

## Overview
The **English to Hindi-Gujarati Translator** is a simple and interactive GUI application designed to translate English text into Hindi or Gujarati. Developed using Python and the Tkinter library, this tool leverages the `googletrans` library to provide accurate and quick translations. The application is user-friendly and includes essential features such as language selection, translation, and result display.

## Features
- **User-Friendly GUI:** Built with Tkinter for easy navigation and usability.
- **Language Options:** Translate English text into Hindi or Gujarati.
- **Error Handling:** Provides appropriate warnings and error messages for invalid inputs or operations.
- **Real-Time Translation:** Quickly translates text into the selected language.
- **Clear Output:** Users can clear the input and output boxes with a single click.

## How It Works
1. Enter the English text you want to translate in the input box.
2. Select the target language (Hindi or Gujarati) using the radio buttons.
3. Click the **Translate** button to generate the translation.
4. The translated text will be displayed in the output box.
5. Use the **Clear** button to reset the input and output boxes.

## Prerequisites
This application requires the following Python libraries:

- `tkinter`: Built-in Python library for creating graphical user interfaces.
- `googletrans`: Library for accessing Google Translate.

### Installing Dependencies
Install the required libraries using the following command:

```bash
pip install googletrans==4.0.0-rc1
```

> **Note:** The `requirements.txt` file for the larger multimodal system includes dependencies for all models. If you're using this model independently, ensure only the required dependencies are installed.

## How to Run the Application
1. Save the code as `translator.py`.
2. Open a terminal and navigate to the directory where the file is saved.
3. Run the following command:

```bash
python translator.py
```

4. The application window will open, allowing you to interact with the translator.

## Demo
Watch the [YouTube demo video](https://youtu.be/K_Rv1-Qq9lY?si=Q2TWhQpXW8MsjDz8) to see the application in action.

## Code Explanation
### Key Functions
1. **translate()**
   - Retrieves the English text from the input box.
   - Translates the text into the selected target language (Hindi or Gujarati).
   - Displays the translated text in the output box.

2. **clear_output()**
   - Clears the input and output text boxes.

3. **show_about()**
   - Displays information about the application in a message box.

4. **show_help()**
   - Provides a brief guide on how to use the application.

### GUI Elements
- **Text Box:** For entering English text and displaying translated output.
- **Radio Buttons:** For selecting the target language (Hindi or Gujarati).
- **Buttons:** For translating, clearing the output, and accessing help/about sections.
- **Menu Bar:** Includes options to exit the application and view help/about.

### Example Translation
- **Input:** "Hello, how are you?"
- **Target Language:** Hindi
- **Output:** "हेलो, आप कैसे हैं?"

## Screenshots
- **Main Window:** The primary interface where users can input text and view translations.
- **Error Messages:** Examples of warnings for invalid inputs or errors.

## Future Enhancements
- Support for additional languages.
- Improved error handling and offline translation capabilities.
- Integration with speech-to-text and text-to-speech modules.

## About
This application was developed as part of a larger multimodal system by **A&J**. It is designed to be simple, efficient, and user-friendly, making translations accessible to everyone.

---
For additional information or assistance, please refer to the [YouTube demo video](https://youtu.be/K_Rv1-Qq9lY?si=Q2TWhQpXW8MsjDz8).
