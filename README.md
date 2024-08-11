---

# InkwellMart

InkwellMart is an e-commerce web application built with Django, allowing users to browse, search, and purchase various products online. The platform provides a seamless shopping experience with a user-friendly interface and secure payment processing.




## Features

- User Authentication: Sign up, log in, and manage profiles.
- Product Listing: Browse through a variety of products.
- Shopping Cart: Add, remove, and manage items in the cart.
- Checkout Process: Secure payment gateway integration.
- Order History: View and track past orders.
- Admin Panel: Manage products, orders, and users.

## Technologies Used

- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default)
- **Other:** Django Admin, Bootstrap

## Folder Structure

```plaintext
inkwellmart/
│
├── inkwell/
│   ├── inkwell/         # Project settings and configurations
│   ├── media/           # Uploaded media files (images, etc.)
│   ├── shop/            # Core app containing views, models, and templates
│   └── static/          # Static files (CSS, JS, images)
│
└── manage.py            # Django project management script
```

## Installation and Setup

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Yashgabani845/inkwellmart.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd inkwellmart
   ```

3. **Install dependencies:**

   Ensure you have Python installed. Then install the required packages:

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

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Screenshots

### Home Page
![Screenshot (6)](https://github.com/user-attachments/assets/3e2bb406-1118-4dc5-8693-81c214b2f6bc)

### Product Page
![Screenshot (9)](https://github.com/user-attachments/assets/f77e7b26-8457-4e2e-aaa7-8c0f3b5f4eb2)

### Shopping Cart
![Screenshot (10)](https://github.com/user-attachments/assets/dedece32-97de-46e4-8841-b432d7d76b2e)

### Admin Dashboard
![Screenshot (11)](https://github.com/user-attachments/assets/83132558-eac8-49e9-99b9-72eb7af6e798)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please reach out to:

- **Name:** Yash Gabani
- **Email:** [gabaniyash846@gmail.com](mailto:your-email@example.com)
- **GitHub:** [Yashgabani845](https://github.com/Yashgabani845)

---
