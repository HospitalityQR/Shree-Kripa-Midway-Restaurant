# 🦚 श्री कृपा MIDWAY RESTAURANT - Official Digital QR Menu & Table Standee

**100% Pure Veg • Pure Desi Ghee & Pure Paneer • Rau, Indore (Agra - Mumbai Hwy)**

Ye platform **श्री कृपा Midway Restaurant** ke liye banaya gaya ek dedicated, ultra-luxurious Digital QR Menu aur Table Standee System hai. Isme kisi third-party Google ya Instagram ki dependency nahi hai — poora focus restaurant ke **170+ authentic dishes**, **live table ordering (My Tray)**, aur **highway hospitality** par hai.

---

## 🏛️ Project Structure

```
Shree Kripa Menu QR/
├── index.html                   # 📱 Ultra-Premium Digital Menu & Table Ordering Web App
├── config.js                    # ⚙️ Master Configuration (Links, Phone, Address, Purity Pledge)
├── menu-data.js                 # 🍽️ 170+ Dishes Database with Authentic Food Photography
├── standee.html                 # 🖨️ Printable Web Table Standee (Ctrl + P Ready with Dynamic Live QR)
├── generate_qr.py               # 🎨 High-Res 300 DPI Standee Generator Script
├── table_standee_printable.png  # 🖼️ 300 DPI Luxury Table Standee (Print-Ready)
├── logo_with_gold_rim.png       # 👑 Official SK Logo with Luxury Gold Bevel Rim
├── qr_code.png                  # 📱 Digital Menu QR Code
└── assets/                      # 📸 Authentic Food Photos, Ambience Photos & Menu Graphics
```

---

## 💡 "404 Not Found" Solution & QR Setup

### 404 Kyun Aaya Tha?
Pehle QR code me GitHub Pages ka dummy link (`https://hospitalityqr.github.io/shree-kripa-QR/`) encode tha, jo GitHub par live upload na hone ke karan phone se scan karne par **404 Not Found** bata raha tha.

### Ab Yeh Kaise Theek Hua?
1. **Dynamic QR in `standee.html`**:
   - `standee.html` ko jab aap browser me kholenge, to uske upar ek input box diya gaya hai.
   - Wahan aap apna **live website link** (jaise aapka GitHub Pages link: `https://hospitalityqr.github.io/shree-kripa-QR/`) ya local Wi-Fi test IP (jaise: `http://192.168.1.5:8080`) daalkar **"Update QR"** par click karein.
   - QR code turant naye link ke sath update ho jayega aur **kabhi bhi 404 nahi aayega**!
2. **Python se Custom QR Standee Generate Karein**:
   ```bash
   python generate_qr.py "https://hospitalityqr.github.io/shree-kripa-QR/"
   ```
   Aap jo bhi link denge, script usi ka 300 DPI high-resolution `table_standee_printable.png` bana dega!

---

## ✨ Features & Hospitality Experience

### 1. 📱 Interactive Digital Menu (`index.html`)
- **Royal Parchment Aesthetic**: Menu PDF ke anuroop warm ivory cream background, golden flourishes, aur devotional Royal Maroon typography.
- **Visual Category Photo Tiles**: Menu ke top par asli dishes ki photos ke sath circular tiles (Paneer Khazana, Tandoori Starters, Platters, Breads, Chinese, etc.).
- **170+ Dishes**:
  - Chinese & Rolls (Veg Hakka Noodles, Manchurian, Chilli Paneer, Soya Chaap)
  - Cheese Specials (Cheese Ball, Cheese Cigar Roll, Spider Roll)
  - Royal Platters (Kabab Platter, Chinese Platter, Tandoori Tikka Platter)
  - Dal & Rice (Dal Makhani, Dal Desi Ghee, Shahi Butter Khichdi, Veg Biryani)
  - Paneer Khazana & Paneer Exclusive (Butter Paneer Masala, Paneer Tufani, Paneer Angara, Paneer Mastana)
  - Main Course & Seasonal Veg (Sev Tamatar, Sev Paneer, Dudh Sev, Veg Handi)
  - Tandoori Breads (Garlic Naan, Cheese Chilli Naan, Chur-Chur Naan, Roti Basket)
  - Sizzlers, Soups, Papad & Desi Ghee Desserts (Moongdal Halwa, Gulab Jamun)
- **Live Search**: English ya Hindi me search karein (e.g. "paneer", "kofta", "पनीर", "नाॅन").
- **My Table Tray (ऑर्डर)**:
  - Table number enter karein (e.g. Table 5).
  - Dishes add karein (+ / -).
  - **Show to Waiter**: Badi screen par fullscreen format me waiter ko order dikhane ka button.
  - **Order via WhatsApp**: Formatted table order sidhe kitchen/reception (`+91-91110-30307`) par WhatsApp bhejne ki suvidha.
- **Purity Guarantee**:
  - *"Pure Desi Ghee, Refined Oil, Amul Butter, Cheese, Milk, Curd, Paneer (Pure) Are Used In Cooking."*
  - *"Please allow us 20 min time for each order preparation."*
- **Party Packages & Ambience**:
  - Kitty Party @₹299
  - Lunch & Dinner Party @₹549
  - Grand Opening highway entrance, reception counter, flower arch, aur dining hall photos.

---

## 🖨️ Table Standee Print Guide (`standee.html`)

1. Browser me `standee.html` open karein.
2. Apna live link confirm karein.
3. **Ctrl + P** press karein ya **"Print Standee"** button click karein.
4. Settings:
   - **Destination**: Save as PDF ya aapka Printer
   - **Layout**: Portrait
   - **Paper Size**: A4 ya 4x6 inch (Table Stand Size)
   - **Margins**: None
   - **Options**: "Background Graphics" ko enable karein.
