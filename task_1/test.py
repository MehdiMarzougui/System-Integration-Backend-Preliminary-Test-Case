import sqlite3
from xml.etree import ElementTree as ET
from pathlib import Path


class Product:
    # Product class containing all relevant attributes as well as helper functions to extract information from the db
    def __init__(self, id, model, ean,  quantity, image, manufacturer_id, price, status) -> None:
        self.id = id
        self.title, self.description = self.extract_from_product_description_table(
            self.id)
        self.link = f"https://butopea.com/p/{self.id}"
        self.image_links = [
            f"https://butopea.com/{image}"]+self.fetch_additional_images(self.id)
        self.availability = "in_stock" if int(quantity) > 0 else "out_of_stock"
        self.brand = self.fetch_from_manufacturer_table(manufacturer_id)
        self.price = f"{round(float(price),2)} HUF"
        self.condition = "new"

    def extract_from_product_description_table(self, id):
        commad = f"""SELECT name,description FROM product_description WHERE product_id =?"""
        cursor = conn.execute(commad, (id,))
        return cursor.fetchone()

    def fetch_additional_images(self, id):
        command = """SELECT image FROM product_image WHERE product_id = ? ORDER BY  sort_order"""
        cursor = conn.execute(command, (id,))
        return [f"https://butopea.com/{row[0]}" for row in cursor.fetchall()]

    def fetch_from_manufacturer_table(self, manufacturer_id):
        command = """SELECT name FROM manufacturer WHERE manufacturer_id = ?"""
        cursor = conn.execute(command, (manufacturer_id,))
        return cursor.fetchone()[0]


def fetch_products():
    # fetch raw data from the product table and initiate product object creation
    exclude_status_0 = "1" if True else "0"
    command = """SELECT * FROM product WHERE status =?"""
    cursor = conn.execute(command, (exclude_status_0,))
    return [Product(*row) for row in cursor.fetchall()]


def generate_xml(product_dicts):
    # Define the root element and set the Google namespace
    root = ET.Element("rss", attrib={
        "xmlns:g": "http://base.google.com/ns/1.0",
        "version": "2.0",
    }
    )
    # Define the channel elments
    channel = ET.SubElement(root, "channel")
    ET.SubElement(channel, "title").text = "Butopea"
    ET.SubElement(channel, "link").text = "https://butopea.com/"
    ET.SubElement(channel, "description").text = "Butopea data feed"
    # itirate over products and define products attributes
    for product in product_dicts:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "g:id").text = product["id"]
        ET.SubElement(item, "g:title").text = product["title"]
        ET.SubElement(item, "g:description").text = product["description"]
        ET.SubElement(item, "g:link").text = product["link"]
        for image_link in product["image_links"]:
            ET.SubElement(item, "g:image_link").text = image_link
        ET.SubElement(item, "g:condition").text = product["condition"]
        ET.SubElement(item, "g:availability").text = product["availability"]
        ET.SubElement(item, "g:price").text = product["price"]
        ET.SubElement(item, "g:brand").text = product["brand"]
    tree = ET.ElementTree(root)
    # write out the file
    tree.write("feed.xml", encoding="UTF-8", xml_declaration=True)


with sqlite3.connect("data.sqlite") as conn:
    # establish a connection with the database, fetch products data and then create a feed XML file
    products = fetch_products()
    product_dicts = [product.__dict__ for product in products]
    generate_xml(product_dicts)
