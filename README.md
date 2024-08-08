# File Share

**File Share** is a Django-based web application designed for secure file sharing. Users can easily upload files and share them via a unique link or a QR code. The application provides a simple, user-friendly interface that makes file sharing across devices and with others a seamless experience.

## Features

- **File Upload**: Securely upload files to the server.
- **Shareable Links**: Get a unique link for each uploaded file.
- **QR Code Generation**: Generate a QR code that links directly to the file.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/file-share.git
   cd file-share
2. **Set up a virtual environment:**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt

    ```
4. **Apply migrations:**
   ```bash
    python manage.py migrate
    ```
5. **Run the development server:**
   ```bash
    python manage.py runserver
    ```
6. **Access the application:**
    Open your web browser and go to http://127.0.0.1:8000/.

## Usage

1. **Upload a File:**
   - Go to the upload page and choose the file you want to share.

2. **Get the Shareable Link or QR Code:**
   - After uploading, you'll receive a unique URL and a QR code that you can share with others.

3. **Access the File:**
   - The recipient can use the link or scan the QR code to download the file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or bugs.


   
