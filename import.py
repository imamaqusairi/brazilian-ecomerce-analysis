# import kagglehub
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
print(r"C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset", path)

# Import necessary modules
import pandas as pd 
from sqlalchemy import create_engine

# Store data into virtual machine
customer = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_customers_dataset.csv'
geo = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_geolocation_dataset.csv'
order_items = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_order_items_dataset.csv'
order_payment = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_order_payments_dataset.csv'
order_review = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_order_reviews_dataset.csv'
order = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_orders_dataset.csv'
product = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_products_dataset.csv'
seller = r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_sellers_dataset.csv'

crawled_data = [geo, order_items, order_payment, order_review, order, product, seller]

# Konfigurasi SQL Server dari DBEAVER
USER = "postgres"
PASSWORD = "hidupmahasiswa" 
HOST = "localhost"
PORT = "5432"
DB_NAME = "brazillian-ecommerce"

# Buat Koneksi (Connection String)
connection_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
engine = create_engine(connection_string)

for data in crawled_data:
    df = pd.read_csv(data)
    try:
        # Masukkan ke tabel bernama 'tabel_ecommerce'
        df.to_sql('tabel_ecommerce', con=engine, index=False, if_exists='replace')
        
        print("Berhasil! Data sekarang bisa dilihat di DBeaver.")
        
    except Exception as e:
        print(f"Gagal konek: {e}")
