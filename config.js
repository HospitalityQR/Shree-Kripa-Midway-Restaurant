// =============================================================================
// 🦚 SHREE KRIPA MIDWAY RESTAURANT - MASTER CONFIGURATION
// 100% Pure Veg • Pure Desi Ghee & Pure Paneer • Rau, Indore
// Hosted on GitHub: HospitalityQR / shree-kripa-QR
// =============================================================================

var RESTAURANT_CONFIG = {
    // 1. Restaurant Brand Identity (श्री कृपा MIDWAY RESTAURANT)
    restaurantId: "shree-kripa",
    restaurantName: "श्री कृपा",
    restaurantSubname: "MIDWAY RESTAURANT",
    restaurantType: "100% PURE VEG",
    tagline: "Pure Desi Ghee & Amul Butter • Authentic Highway Hospitality",
    logoImage: "logo_with_gold_rim.png",
    heroBanner: "brand_hero_banner.jpg",

    // 2. Standee Heading & Call to Action (Digital Menu Focus)
    standeeHeading: "SCAN FOR DIGITAL MENU",
    standeeSubheading: "100% Pure Veg • 170+ Dishes • Instant Table Order",

    // 3. Direct Contact & Location Details
    phoneNumber: "9111030307",
    phoneDisplay: "+91-91110-30307",
    phoneButtonText: "Call / Table Order: +91-91110-30307",
    address: "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Indore",
    fullAddress: "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Near Highway Toll Plaza, Agra - Mumbai Hwy, Indore, (M.P.) 453331",
    mapUrl: "https://www.google.com/maps/search/?api=1&query=Shree+Kripa+Midway+Restaurant+Pigdamber+Rau+Indore",

    // 4. Authentic Kitchen Purity & Courtesy Notices (From Menu PDF)
    purityNotice: "Pure Desi Ghee, Refined Oil, Amul Butter, Cheese, Milk, Curd, Paneer (Pure) Are Used In Cooking.",
    prepTimeNotice: "PLEASE ALLOW US 20 MIN TIME FOR EACH ORDER PREPARATION.",
    prepTimeHindi: "कृपया स्वादिष्ट भोजन की तैयारी के लिए कम से कम 20 मिनट का समय दें।",
    taxesNotice: "Taxes Extra as Applicable*",

    // 5. Signature Slogans (From Menu PDF Page 14)
    sloganEnglish: "You Can Enjoy Delicious Food Serving Happiness, One Plate At A Time",
    sloganHindi: "एक बार खाइए, बार-बार आइए",
    sloganDesc: "श्री कृपा रेस्टोरेंट में स्वाद, सेवा और विश्वास एक साथ पाइए।",

    // 6. Party & Event Packages (From Menu PDF Page 5)
    partyPackages: [
        { 
            title: "Kitty Party Packages", 
            price: "Started @ ₹299", 
            desc: "Starters, Main Course & Dessert combo crafted for kitty parties and celebrations." 
        },
        { 
            title: "Lunch & Dinner Party Packages", 
            price: "Started @ ₹549", 
            desc: "Grand multi-course highway buffet feast with Paneer delicacies and Desi Ghee sweets." 
        }
    ],

    // 7. Footer Hospitality Note
    footerThanks: "Thank You For Visiting श्री कृपा Midway Restaurant 🙏",
    footerCity: "Royal Highway Hospitality • Rau, Indore (Agra - Mumbai Hwy)",

    // 8. Hosted Digital Menu URL on HospitalityQR
    landingPageUrl: "https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/"
};

if (typeof module !== 'undefined' && module.exports) {
    module.exports = RESTAURANT_CONFIG;
}
