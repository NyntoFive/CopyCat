"""
Store PDFs in sqlite. Fund that random document that you saved 4months ago 
in an obscure location. ;D

by Mike King
"""
import sqlite3
import os


def convertToBinaryData(filename):
    """Convert data into binary format."""
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(id, title, image, pdfFile):
    try:
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()

        sqlite_insert_blob_query = """INSERT INTO pdfs
                                   (id, title, image, pdfFile) VALUES(?, ?, ?, ?)"""
        image = convertToBinaryData(image)
        pdfFile = convertToBinaryData(pdfFile)
        # Convert data into tuple format
        data_tuple = (id, title, image, pdfFile)
        cursor = cursor.execute(sqlite_insert_blob_query, data_tuple)
        conn.commit()
        print("Success!")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into table", error)
    finally:
        if (conn):
            conn.close()

def main():
    insertBLOB(1, "CSS Defenitive Guide", "ben.jpg", "css_thedefinitiveguide.pdf")
    insertBLOB(2, "SVG and HTML", "brenny.jpg", "usingsvgwithcss3andhtml5.pdf")

if __name__ == "__main__":
    main()
    