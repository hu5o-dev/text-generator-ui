# 📚 Text Generator with GPT-2 and CustomTkinter

This project uses a pre-trained GPT-2 model to generate text based on a user-provided prompt. The UI is built using the CustomTkinter library, allowing users to interactively generate and save text.

## 🚀 Features

- **Text Generation**: Generate text based on a user-input prompt using GPT-2.
- **Customizable**: Adjust parameters like maximum length, temperature, top-k, and top-p for text generation.
- **User Interface**: Simple and intuitive interface built with CustomTkinter.
- **Logging**: Logs important events and errors to a log file.
- **Text Saving**: Automatically saves the generated text to a file with a timestamp.

## 🛠️ Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hu5o-dev/text-generator-ui.git
   cd text-generator-ui
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install torch transformers customtkinter
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

## 🖥️ How to Use

1. **Enter your prompt**: Start by typing a prompt into the input field.
2. **Generate Text**: Click the "Generate Text" button to create text based on your prompt.
3. **View and Save**: The generated text will appear in the textbox below. It is also automatically saved in the `generated_texts` directory.

## 📁 Project Structure

- `app.py`: Main application script.
- `text_generation.log`: Log file for the application's operations.
- `generated_texts/`: Directory where the generated texts are saved.

## 📝 Example

1. Enter a prompt like `"Once upon a time,"`.
2. Click **Generate Text**.
3. View the generated story in the textbox and find it saved in the `generated_texts` folder.
   ![image](https://github.com/user-attachments/assets/d25b2b84-2e78-4131-8411-b370b2c1ce7e)

## 🧑‍💻 Author

- **Hugo** - [My GitHub](https://github.com/hu5o-dev)

## 📄 License

This project is licensed under the MIT License.

---

Happy Text Generating! ✨
