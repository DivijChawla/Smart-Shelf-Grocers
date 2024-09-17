# Smart-Shelf-Grocers

## Overview

Smart-Shelf-Grocers is a Python-based Point of Sale (POS) system designed to manage grocery items and store transaction details. The application features a graphical interface built with Tkinter, enabling users to browse items, manage a shopping cart, and log transactions into a MySQL database.

## Features

- **Graphical User Interface**: Created with Tkinter for an intuitive user experience.
- **Item Management**: View and interact with a list of grocery items.
- **Shopping Cart**: Add items to a cart, view quantities, and calculate total costs.
- **Transaction Logging**: Store transaction details in a MySQL database.
- **Image Support**: Display images of items using PIL (Pillow).

## Installation

To set up Smart-Shelf-Grocers, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Smart-Shelf-Grocers.git
   cd Smart-Shelf-Grocers
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database**:
   - Ensure you have MySQL installed and running.
   - Update the database connection details in `shopping.py` with your MySQL configuration.

5. **Run the Application**:
   ```bash
   python main.py
   ```

## Usage

1. **Launch the Application**:
   - Run `python main.py` to start the application.

2. **Navigating the Application**:
   - **Continue**: Click "Continue" to proceed to the login page.
   - **Login/Register**: Use the login or registration functionality to access the main application.
   - **Shopping and Cart Management**: Browse items, add them to your cart, and view cart details.
   - **Transaction Logging**: When you proceed to pay, the application logs transaction details in the database.

## Code Overview

- **`main.py`**: Initializes the application and provides the initial user interface.
- **`Login_Button.py`**: Handles user authentication and registration.
- **`shopping.py`**: Manages item display, cart functionality, and transaction logging.

## Troubleshooting

- **Database Connection Issues**:
  Ensure your MySQL server is running and the connection parameters in `shopping.py` are correctly configured.

- **Missing Dependencies**:
  Confirm that all required packages are installed by reviewing the `requirements.txt` file.

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the Repository**.
2. **Create a Branch** for your feature or bug fix.
3. **Submit a Pull Request** with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please contact divijchawla7@gmail.com

---
