# CryptoScope

CryptoScope, CoinMarketCap verilerini çekerek kripto para piyasasını analiz eden ve interaktif grafiklerle görselleştiren Python tabanlı bir araçtır.

## Özellikler
- Web scraping (CoinMarketCap)
- Veri analizi (Pandas)
- Interaktif görselleştirme (Plotly)
- CLI parametreleri ile esnek kullanım
- Hata yönetimi ve logging
- Opsiyonel CSV kaydı

## Kurulum

```bash

Depoyu klonlayın: 

git clone <repo-url>
cd crypto-scope

Gereksinimleri yükleyin:

pip install -r requirements.txt

Kullanım 🖥️

Varsayılan olarak ilk 10 kriptoyu görselleştirir:


python crypto_scope.py


İlk 20 kriptoyu çekmek için:

python crypto_scope.py --limit 20

Verileri CSV olarak kaydetmek için:

python crypto_scope.py --save

Neden CryptoScope? 💡

Web scraping ve veri işleme deneyimi sunar

Etkileşimli görselleştirmeler ile kullanıcı deneyimi sağlar


Kahve Bağışı ☕💖
Bu proje işinize yaradıysa ve destek olmak istersen, bir kahve ile teşekkür edebilirsiniz