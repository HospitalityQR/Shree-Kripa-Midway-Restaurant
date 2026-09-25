// =============================================================================
// 🍽️ SHREE KRIPA MIDWAY RESTAURANT - COMPLETE MENU DATABASE
// Extracted with 100% accuracy from Official 14-Page Menu
// Pure Veg • Desi Ghee & Pure Paneer Preparations
// =============================================================================

var MENU_DATA = [
    // -------------------------------------------------------------------------
    // 1. CHINESE चायनीज़ (Page 2)
    // -------------------------------------------------------------------------
    { id: "ch_1", name: "Veg Hakka Noodles", nameHi: "वेज हक्का नूडल्स", category: "chinese", price: 180, prepTime: "20 Min" },
    { id: "ch_2", name: "French Fries", nameHi: "फ्रेंच फ्राइज", category: "chinese", price: 180, prepTime: "20 Min" },
    { id: "ch_3", name: "Veg Manchurian", nameHi: "वेज मंचूरियन", category: "chinese", price: 180, prepTime: "20 Min", isSpecial: true, img: "assets/food_manchurian.jpg" },
    { id: "ch_4", name: "Fried Rice", nameHi: "फ्राइड राइस", category: "chinese", price: 180, prepTime: "20 Min" },
    { id: "ch_5", name: "Chilli Garlic Noodles", nameHi: "चिली गार्लिक नूडल्स", category: "chinese", price: 210, prepTime: "20 Min" },
    { id: "ch_6", name: "Veg Noodles", nameHi: "वेज नूडल्स", category: "chinese", price: 200, prepTime: "20 Min" },
    { id: "ch_7", name: "Crispy Corn", nameHi: "क्रिस्पी कॉर्न", category: "chinese", price: 200, prepTime: "20 Min", isSpecial: true },
    { id: "ch_8", name: "Crispy Veg", nameHi: "क्रिस्पी वेज", category: "chinese", price: 200, prepTime: "20 Min" },
    { id: "ch_9", name: "Spring Roll", nameHi: "स्प्रिंग रोल", category: "chinese", price: 230, prepTime: "20 Min" },
    { id: "ch_10", name: "Veg Lollipop (8PC)", nameHi: "वेज लॉलीपॉप", category: "chinese", price: 210, pcs: "8 Pc", prepTime: "20 Min" },
    { id: "ch_11", name: "Honey Chilli Potato", nameHi: "हनी चिली पोटैटो", category: "chinese", price: 230, prepTime: "20 Min", isSpecial: true },
    { id: "ch_12", name: "Schezwan Fried Rice", nameHi: "सेजवान फ्राइड राइस", category: "chinese", price: 210, prepTime: "20 Min" },
    { id: "ch_13", name: "Chilli Paneer", nameHi: "चिल्ली पनीर", category: "chinese", price: 290, prepTime: "20 Min", isSpecial: true, img: "assets/food_chinese.jpg" },
    { id: "ch_14", name: "Chilli Mushroom", nameHi: "चिल्ली मशरूम", category: "chinese", price: 310, prepTime: "20 Min" },
    { id: "ch_15", name: "Paneer 65", nameHi: "पनीर 65", category: "chinese", price: 290, prepTime: "20 Min" },
    { id: "ch_16", name: "Chilli Baby Corn", nameHi: "चिली बेबी कॉर्न", category: "chinese", price: 310, prepTime: "20 Min" },
    { id: "ch_17", name: "Paneer Mexican Roll", nameHi: "पनीर मेक्सिकन रोल", category: "chinese", price: 310, prepTime: "20 Min" },
    { id: "ch_18", name: "Soya Chilli Chaap", nameHi: "सोया चिल्ली चाप", category: "chinese", price: 280, prepTime: "20 Min" },

    // -------------------------------------------------------------------------
    // 2. CHEESE SPECIAL चीज़ स्पेशल (8Pc) (Page 3)
    // -------------------------------------------------------------------------
    { id: "cs_1", name: "Cheese Ball", nameHi: "चीज़ बॉल", category: "cheese", price: 290, pcs: "8 Pc", prepTime: "20 Min", isSpecial: true },
    { id: "cs_2", name: "Cheese Corn Ball", nameHi: "चीज़ कॉर्न बॉल", category: "cheese", price: 290, pcs: "8 Pc", prepTime: "20 Min" },
    { id: "cs_3", name: "Cheese Cigar Roll", nameHi: "चीज़ सिगार रोल", category: "cheese", price: 310, pcs: "8 Pc", prepTime: "20 Min", isSpecial: true, img: "assets/food_cheese_cigar.jpg" },
    { id: "cs_4", name: "Cheese Lolipop", nameHi: "चीज़ लॉलीपॉप", category: "cheese", price: 310, pcs: "8 Pc", prepTime: "20 Min" },
    { id: "cs_5", name: "Cheese Corn Spider Roll", nameHi: "चीज़ कॉर्न स्पाइडर रोल", category: "cheese", price: 320, pcs: "8 Pc", prepTime: "20 Min" },
    { id: "cs_6", name: "Cheese Finger", nameHi: "चीज़ फिंगर", category: "cheese", price: 320, pcs: "8 Pc", prepTime: "20 Min" },

    // -------------------------------------------------------------------------
    // 3. PLATTER प्लेटर (Page 3)
    // -------------------------------------------------------------------------
    { id: "pl_1", name: "Kabab Platter", nameHi: "कबाब प्लेटर", category: "platter", price: 380, pcs: "4 Variety 12 Pc", prepTime: "20 Min", isSpecial: true, img: "assets/food_platter.jpg" },
    { id: "pl_2", name: "Chinese Platter", nameHi: "चाइनीज प्लेटर", category: "platter", price: 400, prepTime: "20 Min", isSpecial: true },
    { id: "pl_3", name: "Tandoori Platter", nameHi: "तंदूरी प्लेटर", category: "platter", price: 410, pcs: "5 Variety", prepTime: "20 Min" },
    { id: "pl_4", name: "Tandoori Paneer Tikka Platter", nameHi: "तंदूरी पनीर टिक्का प्लेटर", category: "platter", price: 450, pcs: "4 Variety 12 Pc", prepTime: "20 Min", isSpecial: true, img: "assets/food_platter.jpg" },

    // -------------------------------------------------------------------------
    // 4. DAL दाल (Page 4)
    // -------------------------------------------------------------------------
    { id: "dl_1", name: "Jeera Dal", nameHi: "जीरा दाल", category: "dal", price: 170, prepTime: "20 Min" },
    { id: "dl_2", name: "Dal Fry", nameHi: "दाल फ्राय", category: "dal", price: 180, prepTime: "20 Min" },
    { id: "dl_3", name: "Dal Tadka", nameHi: "दाल तड़का", category: "dal", price: 180, prepTime: "20 Min", isSpecial: true, img: "assets/food_dal_tadka.jpg" },
    { id: "dl_4", name: "Dhaba Dal", nameHi: "ढाबा दाल", category: "dal", price: 190, prepTime: "20 Min", isSpecial: true },
    { id: "dl_5", name: "Dal Punjabi", nameHi: "दाल पंजाबी", category: "dal", price: 200, prepTime: "20 Min" },
    { id: "dl_6", name: "Dal Deshi Ghee", nameHi: "दाल देशी घी", category: "dal", price: 210, prepTime: "20 Min", isSpecial: true },
    { id: "dl_7", name: "Dal Makhani", nameHi: "दाल मखानी", category: "dal", price: 260, prepTime: "20 Min", isSpecial: true, img: "assets/food_dal_tadka.jpg" },

    // -------------------------------------------------------------------------
    // 5. RICE चावल (Page 4)
    // -------------------------------------------------------------------------
    { id: "rc_1", name: "Steam Rice", nameHi: "स्टीम राइस", category: "rice", price: 160, prepTime: "20 Min" },
    { id: "rc_2", name: "Jeera Rice", nameHi: "जीरा राइस", category: "rice", price: 190, prepTime: "20 Min" },
    { id: "rc_3", name: "Butter Khichdi", nameHi: "बटर खिचड़ी", category: "rice", price: 230, prepTime: "20 Min", isSpecial: true },
    { id: "rc_4", name: "Onion Chilli Jeera Rice", nameHi: "अनियन चिल्ल्ली जीरा राइस", category: "rice", price: 170, prepTime: "20 Min" },
    { id: "rc_5", name: "Matar Pulav", nameHi: "मटर पुलाव", category: "rice", price: 180, prepTime: "20 Min" },
    { id: "rc_6", name: "Veg Pulav", nameHi: "वेज पुलाव", category: "rice", price: 180, prepTime: "20 Min" },
    { id: "rc_7", name: "Shahi Butter Khichdi", nameHi: "शाही बटर खिचड़ी", category: "rice", price: 240, prepTime: "20 Min", isSpecial: true },
    { id: "rc_8", name: "Veg Biryani", nameHi: "वेज बिरयानी", category: "rice", price: 260, prepTime: "20 Min" },
    { id: "rc_9", name: "Hyderabadi Biryani", nameHi: "हैदराबादी बिरयानी", category: "rice", price: 280, prepTime: "20 Min", isSpecial: true },
    { id: "rc_10", name: "Kashmiri Pulav", nameHi: "कश्मीरी पुलाव", category: "rice", price: 280, prepTime: "20 Min" },

    // -------------------------------------------------------------------------
    // 6. DAHI KA KHAZANA (RAITA) (Page 4)
    // -------------------------------------------------------------------------
    { id: "dh_1", name: "Plane Dahi (200 gm)", nameHi: "प्लेन दही", category: "raita", price: 80, prepTime: "10 Min" },
    { id: "dh_2", name: "Mint Raita", nameHi: "मिंट रायता", category: "raita", price: 90, prepTime: "10 Min" },
    { id: "dh_3", name: "Vegetable Raita", nameHi: "वेजीटेबल रायता", category: "raita", price: 120, prepTime: "10 Min" },
    { id: "dh_4", name: "Bundi Raita", nameHi: "बूँदी रायता", category: "raita", price: 120, prepTime: "10 Min", isSpecial: true, img: "assets/food_raita.jpg" },
    { id: "dh_5", name: "Cucumber Raita", nameHi: "कुकुम्बर रायता", category: "raita", price: 120, prepTime: "10 Min" },
    { id: "dh_6", name: "Pineapple Raita", nameHi: "पाइनएप्पल रायता", category: "raita", price: 150, prepTime: "10 Min" },
    { id: "dh_7", name: "Fruit Raita", nameHi: "फ्रूट रायता", category: "raita", price: 180, prepTime: "10 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 7. HALKA PHULKA हल्का फुल्का (Page 5)
    // -------------------------------------------------------------------------
    { id: "hp_1", name: "Pav Bhaji", nameHi: "पाव भाजी", category: "halka_phulka", price: 150, prepTime: "20 Min", isSpecial: true, img: "assets/food_pavbhaji.jpg" },
    { id: "hp_2", name: "Veg Pakoda (Kalali)", nameHi: "वेज पकोड़ा (कलाली)", category: "halka_phulka", price: 150, prepTime: "20 Min" },
    { id: "hp_3", name: "Chole Kulche", nameHi: "छोले कुलछे", category: "halka_phulka", price: 180, prepTime: "20 Min" },
    { id: "hp_4", name: "Chole Bhature", nameHi: "छोले भटूरे", category: "halka_phulka", price: 160, prepTime: "20 Min", isSpecial: true },
    { id: "hp_5", name: "Crispy Bhindi", nameHi: "क्रिस्पी भिंडी", category: "halka_phulka", price: 180, prepTime: "20 Min" },
    { id: "hp_6", name: "Papad Bhurji", nameHi: "पापड़ भुर्जी", category: "halka_phulka", price: 150, prepTime: "20 Min" },
    { id: "hp_7", name: "Roasted Chana", nameHi: "रोस्टेड चना", category: "halka_phulka", price: 180, prepTime: "20 Min" },
    { id: "hp_8", name: "Paneer Pakoda (8 Pc)", nameHi: "पनीर पकोड़ा", category: "halka_phulka", price: 220, pcs: "8 Pc", prepTime: "20 Min" },
    { id: "hp_9", name: "Extra Pav", nameHi: "एक्स्ट्रा पाव", category: "halka_phulka", price: 25, prepTime: "5 Min" },
    { id: "hp_10", name: "Extra Bhatura", nameHi: "एक्स्ट्रा भटूरा", category: "halka_phulka", price: 50, prepTime: "10 Min" },
    { id: "hp_11", name: "Extra Kulcha", nameHi: "एक्स्ट्रा कुलछा", category: "halka_phulka", price: 50, prepTime: "10 Min" },

    // -------------------------------------------------------------------------
    // 8. KOFTA कोफ्ता (Page 6)
    // -------------------------------------------------------------------------
    { id: "kf_1", name: "Vegetable Kofta", nameHi: "वेजीटेबल कोफ्ता", category: "kofta", gravy: "Yellow Gravy", price: 250, prepTime: "20 Min" },
    { id: "kf_2", name: "Nargis Kofta", nameHi: "नर्गिस कोफ्ता", category: "kofta", gravy: "Red Gravy", price: 280, prepTime: "20 Min" },
    { id: "kf_3", name: "Malai Kofta (Red Gravy)", nameHi: "मलाई कोफ्ता (लाल ग्रेवी)", category: "kofta", gravy: "Red Gravy", price: 280, prepTime: "20 Min", isSpecial: true, img: "assets/food_kofta.jpg" },
    { id: "kf_4", name: "Dahi Anjeer Kofta", nameHi: "दही अंजीर कोफ्ता", category: "kofta", gravy: "Red Gravy", price: 300, prepTime: "20 Min", isSpecial: true },
    { id: "kf_5", name: "Malai Kofta (White Gravy)", nameHi: "मलाई कोफ्ता (सफेद ग्रेवी)", category: "kofta", gravy: "White Gravy", price: 280, prepTime: "20 Min", isSpecial: true },
    { id: "kf_6", name: "Navratan Kofta", nameHi: "नवरतन कोफ्ता", category: "kofta", gravy: "Red Gravy", price: 280, prepTime: "20 Min" },
    { id: "kf_7", name: "Sham Savera Kofta", nameHi: "शाम सवेरा कोफ्ता", category: "kofta", gravy: "Red Gravy", price: 300, prepTime: "20 Min", isSpecial: true },
    { id: "kf_8", name: "Cheese Kofta", nameHi: "चीज़ कोफ्ता", category: "kofta", gravy: "Yellow Gravy", price: 350, prepTime: "20 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 9. KAJU काजू (Page 6)
    // -------------------------------------------------------------------------
    { id: "kj_1", name: "Kaju Paneer", nameHi: "काजू पनीर", category: "kaju", gravy: "Red Gravy", price: 290, prepTime: "20 Min", isSpecial: true },
    { id: "kj_2", name: "Kaju Curry (Red Gravy)", nameHi: "काजू करी", category: "kaju", gravy: "Red Gravy", price: 290, prepTime: "20 Min" },
    { id: "kj_3", name: "Kaju Masala", nameHi: "काजू मसाला", category: "kaju", gravy: "Yellow Gravy", price: 290, prepTime: "20 Min", isSpecial: true },
    { id: "kj_4", name: "Kaju Curry (White Gravy)", nameHi: "काजू करी (सफेद ग्रेवी)", category: "kaju", gravy: "White Gravy", price: 300, prepTime: "20 Min" },

    // -------------------------------------------------------------------------
    // 10. PANEER KHAZANA पनीर खज़ाना (Page 7)
    // -------------------------------------------------------------------------
    { id: "pn_1", name: "Matar Paneer", nameHi: "मटर पनीर", category: "paneer", gravy: "Yellow Gravy", price: 250, prepTime: "20 Min" },
    { id: "pn_2", name: "Palak Paneer", nameHi: "पालक पनीर", category: "paneer", gravy: "Green Gravy", price: 250, prepTime: "20 Min" },
    { id: "pn_3", name: "Paneer Punjabi", nameHi: "पनीर पंजाबी", category: "paneer", gravy: "Red Gravy", price: 250, prepTime: "20 Min" },
    { id: "pn_4", name: "Paneer Lababdar", nameHi: "पनीर लबाबदार", category: "paneer", gravy: "Yellow Gravy", price: 270, prepTime: "20 Min", isSpecial: true, img: "assets/food_paneer.jpg" },
    { id: "pn_5", name: "Paneer Chatpata", nameHi: "पनीर चटपटा", category: "paneer", gravy: "Red Gravy", price: 260, prepTime: "20 Min" },
    { id: "pn_6", name: "Butter Paneer Masala", nameHi: "बटर पनीर मसाला", category: "paneer", gravy: "Red Gravy", price: 280, prepTime: "20 Min", isSpecial: true, img: "assets/food_paneer.jpg" },
    { id: "pn_7", name: "Kadhai Paneer", nameHi: "कढ़ाई पनीर", category: "paneer", gravy: "Yellow Gravy", price: 280, prepTime: "20 Min", isSpecial: true },
    { id: "pn_8", name: "Shahi Paneer (Red Gravy)", nameHi: "शाही पनीर", category: "paneer", gravy: "Red Gravy", price: 280, prepTime: "20 Min" },
    { id: "pn_9", name: "Paneer Khada Masala", nameHi: "पनीर खड़ा मसाला", category: "paneer", gravy: "Yellow Gravy", price: 270, prepTime: "20 Min" },
    { id: "pn_10", name: "Paneer Tikka Masala", nameHi: "पनीर टिक्का मसाला", category: "paneer", gravy: "Red Gravy", price: 300, prepTime: "20 Min", isSpecial: true },
    { id: "pn_11", name: "Tawa Paneer Masala", nameHi: "तवा पनीर मसाला", category: "paneer", gravy: "Red Gravy", price: 300, prepTime: "20 Min" },
    { id: "pn_12", name: "Paneer Khurchan", nameHi: "पनीर खुरचन", category: "paneer", gravy: "Red Gravy", price: 290, prepTime: "20 Min" },
    { id: "pn_13", name: "Paneer Bhurji", nameHi: "पनीर भुर्जी", category: "paneer", price: 290, prepTime: "20 Min", isSpecial: true },
    { id: "pn_14", name: "Shahi Paneer (White Gravy)", nameHi: "शाही पनीर (सफेद ग्रेवी)", category: "paneer", gravy: "White Gravy", price: 300, prepTime: "20 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 11. PANEER EXCLUSIVE पनीर एक्सक्लूसिव (Page 7)
    // -------------------------------------------------------------------------
    { id: "pe_1", name: "Paneer Tufani", nameHi: "पनीर तुफानी", category: "paneer_exclusive", gravy: "Red Gravy", price: 330, prepTime: "20 Min", isSpecial: true },
    { id: "pe_2", name: "Paneer Najakat", nameHi: "पनीर नजाकत", category: "paneer_exclusive", gravy: "Red Gravy", price: 350, prepTime: "20 Min", isSpecial: true },
    { id: "pe_3", name: "Paneer Angara", nameHi: "पनीर अंगारा", category: "paneer_exclusive", gravy: "Red Gravy", price: 350, prepTime: "20 Min", isSpecial: true, img: "assets/food_paneer.jpg" },
    { id: "pe_4", name: "Paneer Cheese Masala", nameHi: "पनीर चीज़ मसाला", category: "paneer_exclusive", gravy: "Yellow Gravy", price: 350, prepTime: "20 Min", isSpecial: true },
    { id: "pe_5", name: "Paneer Mastana", nameHi: "पनीर मस्ताना", category: "paneer_exclusive", gravy: "Red & Green Gravy", price: 380, prepTime: "20 Min", isSpecial: true },
    { id: "pe_6", name: "Paneer Patiyala", nameHi: "पनीर पटियाला", category: "paneer_exclusive", gravy: "Yellow Gravy", price: 330, prepTime: "20 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 12. PARATHA पराठा (With Sauce Chutney) (Page 8)
    // -------------------------------------------------------------------------
    { id: "pr_1", name: "Aloo Paratha", nameHi: "आलू पराठा", category: "paratha", price: 80, prepTime: "15 Min" },
    { id: "pr_2", name: "Pyaj Paratha", nameHi: "प्याज पराठा", category: "paratha", price: 80, prepTime: "15 Min" },
    { id: "pr_3", name: "Vegetable Paratha", nameHi: "वेजिटेबल पराठा", category: "paratha", price: 100, prepTime: "15 Min" },
    { id: "pr_4", name: "Gobhi Paneer Onion Paratha", nameHi: "गोभी पनीर अनियन", category: "paratha", price: 130, prepTime: "15 Min" },
    { id: "pr_5", name: "Sev Cheese Paratha", nameHi: "सेव चीज़ पराठा", category: "paratha", price: 130, prepTime: "15 Min", isSpecial: true },
    { id: "pr_6", name: "Paneer Paratha", nameHi: "पनीर पराठा", category: "paratha", price: 140, prepTime: "15 Min", isSpecial: true },
    { id: "pr_7", name: "Corn Cheese Paratha", nameHi: "कॉर्न चीज़ पराठा", category: "paratha", price: 140, prepTime: "15 Min" },

    // -------------------------------------------------------------------------
    // 13. ICE-CREAM आइसक्रीम (If Available) (Page 8)
    // -------------------------------------------------------------------------
    { id: "ic_1", name: "Vanilla Ice-Cream", nameHi: "वनिला", category: "ice_cream", price: 60, prepTime: "5 Min" },
    { id: "ic_2", name: "Butter Scotch Ice-Cream", nameHi: "बटर स्कॉच", category: "ice_cream", price: 70, prepTime: "5 Min" },
    { id: "ic_3", name: "Strawberry Ice-Cream", nameHi: "स्ट्रॉबेरी", category: "ice_cream", price: 70, prepTime: "5 Min" },
    { id: "ic_4", name: "Choco Chips Ice-Cream", nameHi: "चोको चिप्स", category: "ice_cream", price: 80, prepTime: "5 Min" },
    { id: "ic_5", name: "Rajbhog Ice-Cream", nameHi: "राजभोग", category: "ice_cream", price: 90, prepTime: "5 Min", isSpecial: true, img: "assets/food_icecream.jpg" },
    { id: "ic_6", name: "American Nuts Ice-Cream", nameHi: "अमेरिकन नट्स", category: "ice_cream", price: 90, prepTime: "5 Min" },
    { id: "ic_7", name: "Matka Kulfi (Kesar Pista, Rabdi Malai)", nameHi: "मटका कुल्फी (केसर पिस्ता, रबड़ी मलाई)", category: "ice_cream", price: "On MRP", prepTime: "5 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 14. DESSERT मिठाई (If Available) (Page 8)
    // -------------------------------------------------------------------------
    { id: "ds_1", name: "Gulab Jamun (2 pc)", nameHi: "गुलाब जामुन", category: "dessert", price: 80, pcs: "2 Pc", prepTime: "5 Min", isSpecial: true, img: "assets/food_gulabjamun.jpg" },
    { id: "ds_2", name: "Rasgulla (2 pc)", nameHi: "रसगुल्ला", category: "dessert", price: 80, pcs: "2 Pc", prepTime: "5 Min" },
    { id: "ds_3", name: "Moongdal Halwa (Seasonal 100g)", nameHi: "मूंगदाल हलवा (देसी घी)", category: "dessert", price: 120, pcs: "100g", prepTime: "10 Min", isSpecial: true },
    { id: "ds_4", name: "Gajar Halwa (Seasonal 100g)", nameHi: "गाजर हलवा (देसी घी)", category: "dessert", price: 100, pcs: "100g", prepTime: "10 Min" },
    { id: "ds_5", name: "Icecream With Hot Gulab Jamun", nameHi: "आइसक्रीम विथ हॉट गुलाब जामुन", category: "dessert", price: 100, prepTime: "5 Min", isSpecial: true, img: "assets/food_icecream.jpg" },

    // -------------------------------------------------------------------------
    // 15. BREAD रोटी & TANDOOR (Page 9)
    // -------------------------------------------------------------------------
    { id: "br_1", name: "Tandoori Roti Plain", nameHi: "तंदूरी रोटी प्लेन", category: "bread", price: 20, prepTime: "10 Min" },
    { id: "br_2", name: "Tandoori Roti Butter", nameHi: "तंदूरी रोटी बटर", category: "bread", price: 23, prepTime: "10 Min" },
    { id: "br_3", name: "Missi Roti", nameHi: "मिस्सी रोटी", category: "bread", price: 45, prepTime: "12 Min" },
    { id: "br_4", name: "Plain Naan", nameHi: "प्लेन नॉन", category: "bread", price: 50, prepTime: "12 Min" },
    { id: "br_5", name: "Laccha Paratha", nameHi: "लच्छा पराठा", category: "bread", price: 60, prepTime: "12 Min", isSpecial: true },
    { id: "br_6", name: "Butter Naan", nameHi: "बटर नॉन", category: "bread", price: 70, prepTime: "12 Min", isSpecial: true, img: "assets/food_naan.jpg" },
    { id: "br_7", name: "Makka Roti", nameHi: "मक्का रोटी", category: "bread", price: 50, prepTime: "15 Min" },
    { id: "br_8", name: "Jowar Roti", nameHi: "ज्वार रोटी", category: "bread", price: 50, prepTime: "15 Min" },
    { id: "br_9", name: "Onion Kulcha", nameHi: "अनियन कुलछा", category: "bread", price: 80, prepTime: "15 Min" },
    { id: "br_10", name: "Chilli Naan", nameHi: "चिल्ली नॉन", category: "bread", price: 80, prepTime: "15 Min" },
    { id: "br_11", name: "Garlic Naan", nameHi: "गार्लिक नॉन", category: "bread", price: 90, prepTime: "15 Min", isSpecial: true },
    { id: "br_12", name: "Chilli Garlic Naan", nameHi: "चिल्ली गार्लिक नॉन", category: "bread", price: 100, prepTime: "15 Min" },
    { id: "br_13", name: "Cheese Naan", nameHi: "चीज़ नॉन", category: "bread", price: 100, prepTime: "15 Min", isSpecial: true },
    { id: "br_14", name: "Cheese Chilli Naan", nameHi: "चीज़ चिल्ली नॉन", category: "bread", price: 110, prepTime: "15 Min" },
    { id: "br_15", name: "Cheese Garlic Naan", nameHi: "चीज़ गार्लिक नॉन", category: "bread", price: 110, prepTime: "15 Min" },
    { id: "br_16", name: "Stuffed Naan", nameHi: "स्टफ्ड नान", category: "bread", price: 110, prepTime: "15 Min" },
    { id: "br_17", name: "Cheese Chilli Garlic Naan", nameHi: "चीज़ चिल्ली गार्लिक नॉन", category: "bread", price: 120, prepTime: "15 Min", isSpecial: true },
    { id: "br_18", name: "Chur-Chur Naan", nameHi: "चूर-चूर नान", category: "bread", price: 120, prepTime: "15 Min", isSpecial: true, img: "assets/food_naan.jpg" },
    { id: "br_19", name: "Butter Cube", nameHi: "बटर क्यूब", category: "bread", price: 20, prepTime: "2 Min" },
    { id: "br_20", name: "Roti Basket", nameHi: "रोटी बास्केट (असोर्तेड)", category: "bread", price: 300, prepTime: "15 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 16. SEASONAL VEG सीजनल वेज (Page 10)
    // -------------------------------------------------------------------------
    { id: "sv_1", name: "Bhindi Masala", nameHi: "भिन्डी मसाला", category: "seasonal_veg", price: 180, prepTime: "20 Min" },
    { id: "sv_2", name: "Jeera Aloo", nameHi: "जीरा आलू", category: "seasonal_veg", price: 160, prepTime: "20 Min" },
    { id: "sv_3", name: "Bhindi Do Pyaja", nameHi: "भिन्डी दो प्याजा", category: "seasonal_veg", price: 190, prepTime: "20 Min" },
    { id: "sv_4", name: "Hing Dhaniya ke Chatpate Aloo", nameHi: "हिंग धनिया के चटपटे आलू", category: "seasonal_veg", price: 190, prepTime: "20 Min", isSpecial: true },
    { id: "sv_5", name: "Sev Tamatar Masala", nameHi: "सेव टमाटर मसाला", category: "seasonal_veg", gravy: "Red Gravy", price: 200, prepTime: "20 Min", isSpecial: true },
    { id: "sv_6", name: "Chole Masala", nameHi: "छोले मसाला", category: "seasonal_veg", price: 200, prepTime: "20 Min" },
    { id: "sv_7", name: "Corn Palak", nameHi: "कॉर्न पालक", category: "seasonal_veg", gravy: "Green Gravy", price: 200, prepTime: "20 Min" },
    { id: "sv_8", name: "Dam Aloo", nameHi: "दम आलू", category: "seasonal_veg", price: 250, prepTime: "20 Min" },
    { id: "sv_9", name: "Dudh Sev", nameHi: "दूध सेव", category: "seasonal_veg", price: 200, prepTime: "20 Min", isSpecial: true },
    { id: "sv_10", name: "Mix Veg", nameHi: "मिक्स वेज", category: "seasonal_veg", gravy: "Red Gravy", price: 210, prepTime: "20 Min" },
    { id: "sv_11", name: "Matar Mushroom", nameHi: "मटर मशरूम", category: "seasonal_veg", gravy: "Yellow Gravy", price: 230, prepTime: "20 Min" },
    { id: "sv_12", name: "Veg Lakhnavi", nameHi: "वेज लखनवी", category: "seasonal_veg", gravy: "Yellow Gravy", price: 220, prepTime: "20 Min" },
    { id: "sv_13", name: "Veg Kolhapuri", nameHi: "वेज कोल्हापुरी", category: "seasonal_veg", gravy: "Red Gravy", price: 230, prepTime: "20 Min" },
    { id: "sv_14", name: "Lahasuni Palak", nameHi: "लहसुनी पालक", category: "seasonal_veg", gravy: "Green Gravy", price: 200, prepTime: "20 Min", isSpecial: true },
    { id: "sv_15", name: "Veg Handi", nameHi: "वेज हांडी", category: "seasonal_veg", gravy: "Yellow Gravy", price: 250, prepTime: "20 Min", isSpecial: true, img: "assets/food_veg_handi.jpg" },
    { id: "sv_16", name: "Veg Jalfrezi", nameHi: "वेज जलफ्रेजी", category: "seasonal_veg", gravy: "Red Gravy", price: 250, prepTime: "20 Min" },
    { id: "sv_17", name: "Stuffed Tomato", nameHi: "स्टफ्ड टोमेटो", category: "seasonal_veg", gravy: "Red Gravy", price: 230, prepTime: "20 Min" },
    { id: "sv_18", name: "Methi Matar Malai", nameHi: "मेथी मटर मलाई", category: "seasonal_veg", gravy: "White Gravy", price: 250, prepTime: "20 Min", isSpecial: true },
    { id: "sv_19", name: "Sev Paneer", nameHi: "सेव पनीर (इंदौर स्पेशल)", category: "seasonal_veg", price: 270, prepTime: "20 Min", isSpecial: true },
    { id: "sv_20", name: "Mushroom Masala", nameHi: "मशरूम मसाला", category: "seasonal_veg", price: 290, prepTime: "20 Min" },
    { id: "sv_21", name: "Mushroom Babycorn", nameHi: "मशरूम बेबीकॉर्न", category: "seasonal_veg", price: 300, prepTime: "20 Min" },

    // -------------------------------------------------------------------------
    // 17. SIZZLER सिज़लर (Pre. Time 30 Min) (Page 11)
    // -------------------------------------------------------------------------
    { id: "sz_1", name: "Chinese Cocktail Sizzler", nameHi: "चाइनीज कॉकटेल सिज़लर", category: "sizzler", price: 450, prepTime: "30 Min", isSpecial: true, img: "assets/food_sizzler.jpg" },
    { id: "sz_2", name: "Veg Stick Sizzler", nameHi: "वेज स्टिक सिज़लर", category: "sizzler", price: 450, prepTime: "30 Min", isSpecial: true },
    { id: "sz_3", name: "Tandoori Sizzler", nameHi: "तंदूरी सिज़लर", category: "sizzler", price: 450, prepTime: "30 Min", isSpecial: true, img: "assets/food_sizzler.jpg" },

    // -------------------------------------------------------------------------
    // 18. OUR EXCLUSIVE STARTER (Page 11)
    // -------------------------------------------------------------------------
    { id: "es_1", name: "Crunchy Veg Kabab", nameHi: "क्रंची वेज कबाब", category: "exclusive_starter", price: 210, prepTime: "20 Min", isSpecial: true, img: "assets/food_starter.jpg" },
    { id: "es_2", name: "Aloo Firdoshi", nameHi: "आलू फिरदोशी", category: "exclusive_starter", price: 280, prepTime: "20 Min", isSpecial: true },
    { id: "es_3", name: "Paneer Amritsari Tikka", nameHi: "पनीर अमृतसरी टिक्का", category: "exclusive_starter", price: 320, prepTime: "20 Min", isSpecial: true, img: "assets/food_starter.jpg" },
    { id: "es_4", name: "Paneer Makhmali Tikka", nameHi: "पनीर मखमली टिक्का", category: "exclusive_starter", price: 320, prepTime: "20 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 19. SOUP सूप (Page 12)
    // -------------------------------------------------------------------------
    { id: "sp_1", name: "Clear Vegetable Soup", nameHi: "क्लियर वेजिटेबल सूप", category: "soup", price: 110, prepTime: "15 Min" },
    { id: "sp_2", name: "Lemon Coriander Soup", nameHi: "लेमन कोरिएंडर सूप", category: "soup", price: 110, prepTime: "15 Min", isSpecial: true },
    { id: "sp_3", name: "Cream Of Tomato Soup", nameHi: "क्रीम ऑफ़ टोमेटो सूप", category: "soup", price: 120, prepTime: "15 Min", isSpecial: true, img: "assets/food_soup.jpg" },
    { id: "sp_4", name: "Hot And Sour Soup", nameHi: "हॉट एंड सोर सूप", category: "soup", price: 140, prepTime: "15 Min" },
    { id: "sp_5", name: "Veg Manchow Soup", nameHi: "वेज मंचाऊ सूप", category: "soup", price: 140, prepTime: "15 Min", isSpecial: true },
    { id: "sp_6", name: "Sweet Corn Soup", nameHi: "स्वीट कॉर्न सूप", category: "soup", price: 150, prepTime: "15 Min" },
    { id: "sp_7", name: "Cream Of Mushroom Soup", nameHi: "क्रीम ऑफ़ मशरूम सूप", category: "soup", price: 190, prepTime: "15 Min" },

    // -------------------------------------------------------------------------
    // 20. PAPAD पापड़ (Page 12)
    // -------------------------------------------------------------------------
    { id: "pp_1", name: "Roasted Papad (Chana/Moong)", nameHi: "रोस्टेड पापड़", category: "papad", price: 30, prepTime: "5 Min" },
    { id: "pp_2", name: "Fry Papad (Chana/Moong)", nameHi: "फ्राई पापड़", category: "papad", price: 35, prepTime: "5 Min" },
    { id: "pp_3", name: "Roasted Papad Masala (Chana/Moong)", nameHi: "रोस्टेड पापड़ मसाला", category: "papad", price: 40, prepTime: "5 Min", isSpecial: true, img: "assets/food_papad.jpg" },
    { id: "pp_4", name: "Fry Papad Masala (Chana/Moong)", nameHi: "फ्राई पापड़ मसाला", category: "papad", price: 45, prepTime: "5 Min" },

    // -------------------------------------------------------------------------
    // 21. TIKKA टिक्का (Page 13)
    // -------------------------------------------------------------------------
    { id: "tk_1", name: "Achari Aloo Tikka (8Pc)", nameHi: "अचारी आलू टिक्का", category: "tikka", price: 180, pcs: "8 Pc", prepTime: "20 Min" },
    { id: "tk_2", name: "Paneer Tikka (8Pc)", nameHi: "पनीर टिक्का", category: "tikka", price: 280, pcs: "8 Pc", prepTime: "20 Min", isSpecial: true, img: "assets/food_tikka.jpg" },
    { id: "tk_3", name: "Choice of Tandoori Soya Chaap Tikka", nameHi: "चॉइस ऑफ़ तंदूरी सोया चाप टिक्का", category: "tikka", price: 280, prepTime: "20 Min" },
    { id: "tk_4", name: "Achari Paneer Tikka", nameHi: "अचारी पनीर टिक्का", category: "tikka", price: 290, prepTime: "20 Min" },
    { id: "tk_5", name: "Cheese Hariyali Tikka", nameHi: "चीज़ हरियाली टिक्का", category: "tikka", price: 310, prepTime: "20 Min", isSpecial: true },
    { id: "tk_6", name: "Mushroom Tikka", nameHi: "मशरूम टिक्का", category: "tikka", price: 310, prepTime: "20 Min" },
    { id: "tk_7", name: "Malai Paneer Tikka (White)", nameHi: "मलाई पनीर टिक्का", category: "tikka", price: 310, prepTime: "20 Min", isSpecial: true },

    // -------------------------------------------------------------------------
    // 22. KABAB कबाब (Page 13)
    // -------------------------------------------------------------------------
    { id: "kb_1", name: "Hara Bhara Kabab", nameHi: "हरा भरा कबाब", category: "kabab", price: 180, prepTime: "20 Min", isSpecial: true, img: "assets/food_kabab.jpg" },
    { id: "kb_2", name: "Dahi Kabab", nameHi: "दही कबाब", category: "kabab", price: 220, prepTime: "20 Min", isSpecial: true },
    { id: "kb_3", name: "Corn Cheese Paapdi Kabab", nameHi: "कॉर्न चीज़ पापड़ी कबाब", category: "kabab", price: 250, prepTime: "20 Min" },
    { id: "kb_4", name: "Veg Seekh Kabab", nameHi: "वेज सीख कबाब", category: "kabab", price: 250, prepTime: "20 Min" },
    { id: "kb_5", name: "Corn Cheese Kabab", nameHi: "कॉर्न चीज़ कबाब", category: "kabab", price: 330, prepTime: "20 Min", isSpecial: true },
    { id: "kb_6", name: "Beetroot Kabab", nameHi: "बीटरूट कबाब", category: "kabab", price: 350, prepTime: "20 Min", isSpecial: true }
];

// Rich Category Groups for Top Navigation
var MENU_CATEGORIES = [
    { id: "all", name: "All Dishes", nameHi: "सभी व्यंजन", icon: "✨", image: "assets/food_platter.jpg" },
    { id: "paneer_special", name: "Paneer Khazana", nameHi: "पनीर खज़ाना", icon: "🧀", image: "assets/food_paneer.jpg", match: ["paneer", "paneer_exclusive"] },
    { id: "starters", name: "Starters & Kababs", nameHi: "स्टार्टर व कबाब", icon: "🍢", image: "assets/food_starter.jpg", match: ["tikka", "kabab", "exclusive_starter", "cheese"] },
    { id: "main_course", name: "Seasonal Main Course", nameHi: "सीजनल मेन कोर्स", icon: "🍲", image: "assets/food_veg_handi.jpg", match: ["seasonal_veg", "kofta", "kaju"] },
    { id: "bread", name: "Tandoori Breads", nameHi: "रोटी व नान", icon: "🫓", image: "assets/food_naan.jpg", match: ["bread"] },
    { id: "chinese", name: "Chinese & Rolls", nameHi: "चायनीज़", icon: "🥢", image: "assets/food_chinese.jpg", match: ["chinese"] },
    { id: "dal_rice", name: "Dal & Biryani", nameHi: "दाल व चावल", icon: "🍚", image: "assets/food_dal_tadka.jpg", match: ["dal", "rice"] },
    { id: "platter", name: "Royal Platters", nameHi: "शाही प्लेटर", icon: "🍱", image: "assets/food_platter.jpg", match: ["platter"] },
    { id: "sizzler", name: "Sizzlers (30 Min)", nameHi: "सिज़लर", icon: "🔥", image: "assets/food_sizzler.jpg", match: ["sizzler"] },
    { id: "desserts", name: "Desserts & Ice-Cream", nameHi: "मिठाई व आइसक्रीम", icon: "🍨", image: "assets/food_icecream.jpg", match: ["dessert", "ice_cream"] },
    { id: "halka_phulka", name: "Halka Phulka", nameHi: "हल्का फुल्का", icon: "🥟", image: "assets/food_pavbhaji.jpg", match: ["halka_phulka"] },
    { id: "soup_papad", name: "Soups & Raita", nameHi: "सूप व रायता", icon: "🥣", image: "assets/food_soup.jpg", match: ["soup", "papad", "raita"] },
    { id: "paratha", name: "Stuffed Parathas", nameHi: "पराठा", icon: "🥞", image: "assets/food_naan.jpg", match: ["paratha"] }
];

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { MENU_DATA, MENU_CATEGORIES };
}
