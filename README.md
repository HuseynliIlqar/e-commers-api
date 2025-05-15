# E-Commerce API

A RESTful API for an e-commerce platform built with Django and Django REST Framework. This project provides endpoints for user accounts, product listing, category management, baskets (shopping carts), search, and marketplace features.

## Features

* **Authentication**: Register, login, logout, password reset
* **User Accounts**: Profile management and permissions
* **Products**: CRUD operations for products
* **Categories**: Manage product categories
* **Baskets**: Add, update, and remove items from a shopping cart
* **Search**: Full-text and filter-based product search
* **Marketplace**: Additional marketplace-specific logic

## Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework
* SQLite (default) — easily configurable to PostgreSQL or MySQL

## Project Structure

```
├── accounts/          # User registration & authentication
├── baskets/           # Shopping cart functionality
├── category/          # Product categories
├── filter/            # Product filtering logic
├── market_place/      # Marketplace features
├── product/           # Product CRUD operations
├── search/            # Search endpoints
├── myproject/         # Django project settings and URLs
├── db.sqlite3         # Default development database
└── manage.py          # Django management script
```

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/HuseynliIlqar/e-commers-api.git
   cd e-commers-api
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .\.venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`.

## Environment Variables

Rename `.env.example` to `.env` and set the following:

```
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## API Endpoints

| Path                     | Methods | Description                       |
| ------------------------ | ------- | --------------------------------- |
| `/api/auth/register/`    | POST    | Register a new user               |
| `/api/auth/login/`       | POST    | Obtain authentication tokens      |
| `/api/auth/logout/`      | POST    | Logout (token blacklist)          |
| `/api/products/`         | GET     | List all products                 |
| `/api/products/`         | POST    | Create a new product              |
| `/api/products/{id}/`    | GET     | Retrieve product details          |
| `/api/products/{id}/`    | PUT     | Update a product                  |
| `/api/products/{id}/`    | DELETE  | Delete a product                  |
| `/api/categories/`       | GET     | List all categories               |
| `/api/categories/`       | POST    | Create a new category             |
| `/api/baskets/`          | GET     | View current user's basket        |
| `/api/baskets/`          | POST    | Add item to basket                |
| `/api/baskets/{id}/`     | PUT     | Update basket item quantity       |
| `/api/baskets/{id}/`     | DELETE  | Remove item from basket           |
| `/api/search/?q=<query>` | GET     | Search products by name or filter |

Adjust paths if your URLconf differs.

## Running Tests

```bash
pytest
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to your branch: `git push origin feature/YourFeature`
5. Open a pull request

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

Congratulations! Your e-commerce API is now ready for development and testing. Feel free to file issues or contribute enhancements.
