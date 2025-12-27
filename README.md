
# QR Asset Manager & Ownership System

A production-ready Django application designed to digitize the management of physical assets. Users can register items using a webcam or file upload, generate unique QR codes for physical tagging, and manage ownership through a secure, UUID-based permission system.



## 🚀 Problem Statement
Traditional asset tracking often relies on manual spreadsheets or memory, leading to lost warranty info, difficulty in verifying physical item "identities," and a lack of secure sharing options. This project bridges the gap between physical objects and digital metadata using QR technology.

## ✨ Key Features
* **Secure Data Registry:** UUID4-based primary keys to prevent URL enumeration and IDOR attacks.
* **Hardware Integration:** In-browser Webcam capture using HTML5 MediaDevices API and JavaScript Canvas.
* **Automated QR Lifecycle:** Automatic generation of permanent QR codes linked to unique asset URLs.
* **Ownership Control:** Strict Row-Level Access Control—only owners can edit or delete their assets.
* **Detailed Asset Metadata:** Tracks categories, serial numbers, purchase prices, and warranty expiry dates.
* **Responsive Dashboard:** A centralized hub for users to manage their entire inventory.

## 🛠️ Tech Stack
* **Backend:** Python 3.12, Django 5.x
* **Database:** SQLite (Development)
* **Libraries:** * `qrcode` & `Pillow` (QR generation and image processing)
    * `Bootstrap 5` (UI Styling)
* **Frontend:** JavaScript (Base64 image encoding & Webcam stream)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/qr-asset-manager.git](https://github.com/yourusername/qr-asset-manager.git)
   cd qr-asset-manager

```

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install django qrcode pillow

```


4. **Run Migrations:**
```bash
python3 manage.py makemigrations
python3 manage.py migrate

```


5. **Create a Superuser:**
```bash
python3 manage.py createsuperuser

```


6. **Start the Server:**
```bash
python3 manage.py runserver

```



## 🖥️ Usage

1. **Home Page:** Visit `http://127.0.0.1:8000` to view the landing page.
2. **Register:** Create an account to access your personal dashboard.
3. **Add Asset:** Click "Register New Item" and choose to either upload a photo or take one live with your **webcam**.
4. **Manage:** From the dashboard, scan the QR code to view details, or use the "Edit" and "Delete" buttons to manage the asset.

## 🔒 Security Implementation

* **IDOR Prevention:** Uses UUIDs so attackers cannot guess item URLs.
* **CSRF Protection:** All forms are protected against Cross-Site Request Forgery.
* **Access Control:** The backend verifies `item.owner == request.user` for all sensitive operations.

## 🛣️ Roadmap

* [ ] **Ownership Transfer:** A "handshake" system to transfer assets between users.
* [ ] **Cloud Storage:** Integration with AWS S3 for production media handling.
* [ ] **Expiry Notifications:** Email alerts for upcoming warranty expirations.

