import argparse
from basket.basket import Basket
from basket.config_loader import load_catalog, load_offers
from basket.logging_setup import setup_logging
from basket.utils import format_money

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(description="PriceBasket CLI")
    parser.add_argument("items", nargs="+", help="Items to add to basket")
    args = parser.parse_args()

    # try:
    try:
        catalog = load_catalog()
        offers = load_offers()

        basket = Basket(args.items, catalog, offers)
        subtotal, discounts, total, unknown_items = basket.calculate_totals()

        print(f"Subtotal: {format_money(subtotal)}")
        if discounts:
            for d in discounts:
                print(f"{d.description}: {format_money(d.amount, discount=True)}")
        else:
            print("(No offers available)")
        print(f"Total price: {format_money(total)}")

        if unknown_items:
            warning_msg = f"These items are not in the catalog and were ignored: {', '.join(unknown_items)}"
            print(f"Warning: {warning_msg}")
            logger.warning("Unknown items in basket", extra={"error": warning_msg})

        logger.info("Basket processed", extra={
            "extra_data": {
                "items": args.items,
                "processed_items": [i for i in args.items if i.lower() not in unknown_items],
                "subtotal": str(subtotal),
                "discounts": [{"description": d.description, "amount": str(d.amount)} for d in discounts],
                "total": str(total)
            }
        })

    except Exception as e:
        logger.error("Transaction failed", extra={"error": str(e)})
        print("An unexpected error occurred. Check logs for details.")    

if __name__ == "__main__":
    main()
