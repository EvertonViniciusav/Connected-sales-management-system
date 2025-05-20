# Sales Management System

A complete sales management system developed in Python, featuring both a graphical interface and terminal mode. The system allows for efficient control of clients, products, orders, and order items, with persistent data storage using a MySQL database.

## Features

### 🧑 Clients
- Register, edit, and remove client records.
- View and manage all client information in an organized interface.

### 📦 Products
- Add, update, and delete products from inventory.
- Keep track of product stock and details with ease.

### 🧾 Orders
- Create and manage sales orders.
- Associate orders with clients and select products directly from the inventory.

### 📋 Order Items
- Add multiple items to each order.
- Monitor quantities and values of individual items within each sale.

### 💻 Graphical User Interface (Flet)
- Built with [Flet](https://flet.dev/), offering a clean and modern interface.
- Intuitive design for ease of use across all sales operations.
- Fully functional GUI that complements the terminal version.

### 🗃️ Database Integration (MySQL)
- All data is stored securely in a **MySQL** database.
- Ensures persistence, consistency, and scalability of information.
- Ready to support multi-user access and data centralization.

## Requirements

- Python 3.x
- MySQL Server
- Python packages:
  - `flet`
  - `mysql-connector-python`

Install dependencies with:
```bash
pip install flet mysql-connector-python
```

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EvertonViniciusav/Connected-sales-management-system.git
   cd sales-management-system
   ```

2. **Configure the database connection**:
   - Set your MySQL credentials and database name in the configuration section of the code (or via environment variables, if applicable).

3. **Initialize the database** (if needed):
   - Run any provided SQL script or manually create the required tables.

4. **Run the system**:
     ```bash
     python main.py
     ```

## Contact

**Author:** Everton Vinicius  
📧 **Email:** evertonvinicius071@gmail.com

Feel free to reach out for feedback, collaboration, or support.
