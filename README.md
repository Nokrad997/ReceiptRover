# ReceiptRover
## Introduction
This mobile application is designed to help users manage their expenses efficiently. The entire application, including its dependencies, is containerized using Docker. It is written in Python and utilizes a PostgreSQL database for data storage. The admin interface is handled through pgAdmin4, and the OCR functionality is powered by the Tesseract server. The application features a graphical user interface (GUI) for a seamless user experience.

## Installation
### Prerequisites
Ensure that you have Docker installed on your system. You can download it from Docker's official website.

### Steps
Clone the Repository:
git clone [https://github.com/ReceiptRover.git](https://github.com/Nokrad997/ReceiptRover.git)
### Configuration:
Update the configuration in the config.py file with your database and OCR server credentials.

### Build and Run:
docker-compose up --build
This command will download the necessary images, build the application, and start all services in Docker containers.

## Usage
### Registered User:
#### Cloud Storage:
As a registered user, all expense receipts are stored in the PostgreSQL database, providing accessibility across multiple devices. Your data is securely stored in the cloud.

#### Expense History:
Access your expense history and analyze spending patterns through the application. The app generates charts and other analytical tools to help you understand your financial habits.

#### Manual Entry or OCR:
Add expenses manually or leverage OCR functionality by submitting photos of receipts. The OCR system extracts data, allowing you to modify and confirm information before saving it.

### Unregistered User:
#### Local Database:
If you choose not to register, your expense data is stored locally in an XML file.

#### Expense Tracking:
Track your expenses using the application's local database, which provides a basic but functional experience without the need for cloud storage.
