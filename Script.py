# import kagglehub
# path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
# print(r"C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset", path)

# Import necessary modules
import pandas as pd 
from sqlalchemy import create_engine

# Store data into virtual machine
customer = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_customers_dataset.csv')
geo = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_geolocation_dataset.csv')
order_item = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_order_items_dataset.csv')
order_payment = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_order_payments_dataset.csv')
order_review = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_order_reviews_dataset.csv')
order = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_orders_dataset.csv')
product = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_products_dataset.csv')
seller = pd.read_csv(r'C:\Users\MSI THIN\Documents\Projects\Brazillian E Commerce Dataset\brazilian-ecommerce\olist_sellers_dataset.csv')

# Implement Dictionary Methods
crawled_data = {
    "customer" : customer,
    "geo" : geo,
    "order item" : order_item,
    "order payment" : order_payment,
    "order review" : order_review,
    "order" : order,
    "product" : product,
    "seller" : seller
}

# Konfigurasi SQL Server dari DBEAVER
USER = "postgres"
PASSWORD = "hidupmahasiswa" 
HOST = "localhost"
PORT = "5432"
DB_NAME = "brazilian-ecommerce"

# Buat Koneksi (Connection String)
connection_string = f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
engine = create_engine(connection_string)

for table_name, df_content in crawled_data.items():
    try:
        # Masukkan ke tabel bernama 'tabel_ecommerce'
        df_content.to_sql(f'{table_name}', con=engine, index=False, if_exists='replace')
        
        print(f"Berhasil! Data {table_name} sekarang bisa dilihat di DBeaver.")
        
    except Exception as e:
        print(f"Gagal konek: {e}")


