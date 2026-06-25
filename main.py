import sys

from PySide6.QtWidgets import QApplication

from app.gui.main_window import MainWindow

from app.scraper.catalog_scraper import CatalogScraper

from app.scraper.product_scraper import ProductScraper

from app.parser.product_parser import ProductParser


def main():

    catalog = CatalogScraper()

    urls = catalog.scrape()

    scraper = ProductScraper()

    parser = ProductParser()

    raw = scraper.load(urls[0])

    product = parser.parse(raw)

    print()

    print("======== PRODUCT ========")

    print("Title:", product.title)

    print("Vendor:", product.vendor)

    print("Price:", product.msrp)

    print("Images:", len(product.images))

    print("Variants:", len(product.variants))

    print()

    for variant in product.variants:

        print("----------------------")

        print("Title:", variant.title)
    
        print("SKU:", variant.sku)
    
        print("Price:", variant.price)

        print("Color:", variant.color)

        print("Shape:", variant.shape)
    
        print("Barcode:", variant.barcode)

        print("Available:", variant.available)

        print("=========================")

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()