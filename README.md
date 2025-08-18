# Shopping Basket Application

This project is a **command-line shopping basket application** that calculates the total price of items in a basket, including applying special offers. It is modular, configuration-driven, and logs all transactions. The application can handle unknown items gracefully.

---

## 1. Features

- Accepts a list of items via the command line.
- Calculates subtotal, applies discounts, and shows total price.
- Supports multiple catalogs and offer configurations.
- Case-insensitive item names.
- Handles unknown items by warning the user while processing valid items.
- Full logging of transactions with timestamps.
- Unit-tested for correctness.
- Scalable: new products and offers can be added via configuration files without changing code.

---

## 2. Project Structure

```bash
shopping-basket/
│
├── basket/ # Main application modules
│ ├── init.py
│ ├── basket.py # Core basket logic
│ ├── catalog.py # Catalog management
│ ├── offer.py # Offer management
│ └── utils.py # Utility functions
│
├── config/ # Configuration files
│ ├── catalog.json # Product catalog
│ └── offers.json # Current offers
│
├── tests/ # Unit tests
│ └── test_basket.py
│
├── main.py # Entry point script
├── requirements.txt # Python dependencies
└── README.md
```

---

## 3. Installation

1. **Install Python 3.9+** from [python.org](https://www.python.org/downloads/).

2. **Clone the repository**:
```bash
git clone https://github.com/your-username/shopping-basket.git
cd shopping-basket
```

3. **Create a virtual environment (optional but recommended)**:
```bash
python -m venv venv
```

4. **Activate the virtual environment**:

```bash
Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate
```

5. **Install dependencies**:
```bash
pip install -r requirements.txt
```
---
## 4. Configuration

### Catalog: config/catalog.json
```bash
Example:

[
    {"name": "apples", "price": "1.00"},
    {"name": "milk", "price": "1.30"},
    {"name": "bread", "price": "0.80"},
    {"name": "soup", "price": "0.65"}
]
```

### Offers: config/offers.json
```bash
Example:

[
    {"type": "percentage", "item": "apples", "discount": 10},
    {"type": "buy_x_get_y", "buy_item": "soup", "buy_qty": 2, "free_item": "bread", "discount_percent": 50}
]
```

You can update these files to add new products or offers without changing the code.

## 5. Running the Application

Run the program from the command line:

```bash
python main.py Apples Milk Bread
```

Example output:
```bash
Subtotal: £3.10
Apples 10% off: 10p
Total price: £3.00
```

If some items are unknown:
```bash
python main.py Apples Milk Chocolate

Subtotal: £2.30
Apples 10% off: 10p
Total price: £2.20
Warning: These items are not in the catalog and were ignored: chocolate
```
## 6. Unit Tests

The project includes unit tests to validate:

- Correct calculation of subtotal.
- Proper application of discounts.
- Handling of unknown items.
- No-offer scenarios.

Run tests:
```bash
python -m unittest discover -s tests
```

## 7. Logging

Logs are stored with timestamps.

- Transaction logs include:
- Items processed
- Subtotal
- Discounts applied
- Total price
- Unknown items (if any)
- Unknown items are logged as warnings.

## 8. Notes

Item names are case-insensitive.

The application is scalable: just update catalog.json or offers.json to handle new products or promotions.

Designed for production usage on high volumes (modular, configuration-driven, and with logging).

Unknown items do not stop processing; valid items are calculated normally.

## 9. Support

For issues or questions, contact the repository owner via GitHub.
