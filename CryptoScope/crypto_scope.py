# crypto_scope.py
import requests
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup
import argparse
import logging
from datetime import datetime

# Logging ayarları
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def fetch_crypto_data(limit=50):
    URL = "https://coinmarketcap.com/"
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table")
        rows = table.tbody.find_all("tr")
        
        data = []
        for row in rows[:limit]:
            try:
                name = row.find("p", class_="sc-1eb5slv-0 iworPT").text
                price = row.find("div", class_="sc-131di3y-0 cLgOOr").text.replace("$","").replace(",","")
                market_cap = row.find("span", class_="sc-1ow4cwt-1 ieFnWP").text.replace("$","").replace(",","")
                change_24h = row.find_all("span", class_="sc-15yy2pl-0 kAXKAX")[1].text.replace("%","")
                
                data.append({
                    "Name": name,
                    "Price": float(price),
                    "Market Cap": float(market_cap),
                    "Change 24h": float(change_24h)
                })
            except Exception as e:
                logging.warning(f"Bir satır işlenemedi: {e}")
        return pd.DataFrame(data)
    except Exception as e:
        logging.error(f"Veri çekilemedi: {e}")
        return pd.DataFrame()

def visualize_data(df):
    if df.empty:
        logging.info("Görselleştirilecek veri yok.")
        return
    fig = px.bar(df, x="Price", y="Name", color="Change 24h",
                 hover_data=["Market Cap"],
                 title="Top Kripto Paralar ve Fiyat Değişimleri",
                 orientation="h",
                 color_continuous_scale=px.colors.sequential.Viridis)
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    fig.show()

def save_to_csv(df):
    filename = f"crypto_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    logging.info(f"Veriler {filename} olarak kaydedildi.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CryptoScope: Kripto Para Scraper ve Görselleştirici")
    parser.add_argument("--limit", type=int, default=10, help="Kaç kripto çekilecek (default=10)")
    parser.add_argument("--save", action="store_true", help="Verileri CSV olarak kaydet")
    args = parser.parse_args()

    df = fetch_crypto_data(limit=args.limit)
    if not df.empty:
        print(df)
        visualize_data(df)
        if args.save:
            save_to_csv(df)
