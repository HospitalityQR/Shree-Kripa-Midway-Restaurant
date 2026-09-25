"""
Official Luxury Front & Back Standee Generator for Shree Kripa Midway Restaurant
- HospitalityQR Architecture:
  1. Front Standee: Royal Shree Kripa Branding + QR Menu + Pure Desi Ghee Purity Guarantee + Highway Address
     (No Table No, No Call Button, No Ambience)
  2. Back Standee: Slogans + Banquet/Party Packages (@299, @549) + 100% Pure Desi Ghee Promise + Highway Address
     (No Ambience, No Call Button)
- High-Resolution 300 DPI Ready for Acrylic Table Stands
- URL: https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/
"""

import sys
import os
import re
import math
import numpy as np
import qrcode
from PIL import Image, ImageDraw, ImageFont

def load_config():
    config = {
        "restaurantName": "SHREE KRIPA",
        "restaurantSubname": "MIDWAY RESTAURANT",
        "tagline": "MIDWAY RESTAURANT • 100% PURE VEG",
        "landingPageUrl": "https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/",
        "phoneNumber": "9111030307",
        "address": "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Indore",
        "footerThanks": "Thank You For Visiting Shree Kripa Midway Restaurant"
    }
    if os.path.exists("config.js"):
        try:
            with open("config.js", "r", encoding="utf-8") as f:
                content = f.read()
            for key in config.keys():
                m = re.search(rf'{key}\s*:\s*["\']([^"\']+)["\']', content)
                if m:
                    config[key] = m.group(1)
        except Exception as e:
            print("Notice: Could not parse config.js, using defaults:", e)
    return config

def create_luxury_parchment_background(w, h):
    """
    Generate an ultra-luxurious warm royal parchment canvas matching the authentic menu PDF.
    Warm golden ivory core -> creamy gold midtone -> vintage warm gold edge.
    """
    cx, cy = w / 2.0, h * 0.38
    max_r = math.sqrt(cx**2 + (h - cy)**2)

    y, x = np.ogrid[:h, :w]
    dist = np.sqrt((x - cx)**2 + ((y - cy) * 0.88)**2)
    norm_dist = np.clip(dist / (max_r * 0.95), 0.0, 1.0)

    # Authentic menu parchment RGB palette sampled directly from the official PDF
    c_center = np.array([255, 248, 232], dtype=np.float32)
    c_mid = np.array([253, 230, 200], dtype=np.float32)
    c_edge = np.array([242, 212, 175], dtype=np.float32)

    mid_point = 0.50
    factor1 = np.clip(norm_dist / mid_point, 0.0, 1.0)[:, :, None]
    grad_inner = c_center * (1.0 - factor1) + c_mid * factor1

    factor2 = np.clip((norm_dist - mid_point) / (1.0 - mid_point), 0.0, 1.0)[:, :, None]
    grad_outer = c_mid * (1.0 - factor2) + c_edge * factor2

    base_rgb = np.where(norm_dist[:, :, None] < mid_point, grad_inner, grad_outer)

    # Subtle fine paper grain
    np.random.seed(42)
    noise = np.random.normal(0.0, 1.6, (h, w, 1)).astype(np.float32)
    base_rgb = np.clip(base_rgb + noise, 0, 255).astype(np.uint8)

    return Image.fromarray(base_rgb, mode="RGB")

def generate_styled_qr(data, box_size=15, border=2, fill_color=(115, 0, 24), back_color=(255, 255, 255)):
    """Generate crisp, high contrast QR code in Royal Maroon"""
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")
    return img

def get_font(size, bold=False, italic=False):
    """Load standard high-quality serif font"""
    if italic:
        candidates = ["C:\\Windows\\Fonts\\georgiai.ttf", "C:\\Windows\\Fonts\\ariali.ttf"]
    elif bold:
        candidates = ["C:\\Windows\\Fonts\\georgiab.ttf", "C:\\Windows\\Fonts\\arialbd.ttf"]
    else:
        candidates = ["C:\\Windows\\Fonts\\georgia.ttf", "C:\\Windows\\Fonts\\arial.ttf"]

    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_luxury_borders(draw, w, h):
    """Draw ornate royal gold borders & corner diamond accents"""
    # Outer Maroon border
    draw.rectangle([20, 20, w - 20, h - 20], outline=(115, 0, 24), width=2)
    # Main Royal Gold border
    draw.rectangle([28, 28, w - 28, h - 28], outline=(197, 155, 39), width=5)
    # Inner Fine Gold border
    draw.rectangle([40, 40, w - 40, h - 40], outline=(160, 125, 25), width=1)

    # 4 Corner Ornaments (Diamond + Corner Brackets)
    corners = [(28, 28), (w - 28, 28), (28, h - 28), (w - 28, h - 28)]
    for cx, cy in corners:
        draw.polygon([(cx - 10, cy), (cx, cy - 10), (cx + 10, cy), (cx, cy + 10)], fill=(197, 155, 39))
        draw.polygon([(cx - 5, cy), (cx, cy - 5), (cx + 5, cy), (cx, cy + 5)], fill=(115, 0, 24))

def build_front_standee(config, output_filenames=["table_standee_printable.png", "standee_front_printable.png"]):
    """
    Generate 300 DPI Front Standee (QR Code + Digital Menu Focus)
    No Table No, No Call Button, Pure Royal Hospitality Aesthetic.
    """
    w, h = 1200, 1800
    canvas = create_luxury_parchment_background(w, h)
    draw = ImageDraw.Draw(canvas)
    draw_luxury_borders(draw, w, h)

    # 1. Official Logo with Gold Rim
    logo_path = "logo_with_gold_rim.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((210, 210), Image.Resampling.LANCZOS)
        canvas.paste(logo, (int((w - 210) / 2), 65), mask=logo)

    font_brand = get_font(52, bold=True)
    font_title = get_font(38, bold=True)
    font_veg = get_font(23, bold=True)
    font_cta = get_font(40, bold=True)
    font_meta = get_font(22, bold=False)
    font_sub = get_font(27, bold=True)
    font_slogan = get_font(28, bold=True, italic=True)
    font_thanks = get_font(25, bold=True)

    # Brand Title: SHREE KRIPA
    brand_text = "SHREE KRIPA"
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 285), brand_text, fill=(115, 0, 24), font=font_brand)

    # Subtitle: MIDWAY RESTAURANT
    title_text = "MIDWAY RESTAURANT"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 350), title_text, fill=(77, 0, 16), font=font_title)

    # 100% Pure Veg Tag
    veg_text = "100% PURE VEG - PURE DESI GHEE"
    bbox = draw.textbbox((0, 0), veg_text, font=font_veg)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 410), veg_text, fill=(27, 122, 58), font=font_veg)

    # Golden Divider Line
    draw.line([160, 455, w - 160, 455], fill=(197, 155, 39), width=2)

    # Call to action: SCAN FOR DIGITAL MENU
    cta_text = "SCAN FOR DIGITAL MENU"
    bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 480), cta_text, fill=(115, 0, 24), font=font_cta)

    sub_cta = "Explore 170+ Dishes - Authentic Flavors - Pure Desi Ghee"
    bbox = draw.textbbox((0, 0), sub_cta, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 535), sub_cta, fill=(110, 75, 30), font=font_meta)

    # QR Code Box (Expanded & Centered, without Table No)
    qr_url = config.get("landingPageUrl", "https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/")
    qr_img = generate_styled_qr(qr_url, box_size=15, border=2, fill_color=(115, 0, 24))
    qr_size = 560
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    box_x = int((w - qr_size - 40) / 2)
    box_y = 585
    draw.rectangle([box_x, box_y, box_x + qr_size + 40, box_y + qr_size + 40], fill=(255, 255, 255), outline=(197, 155, 39), width=4)
    canvas.paste(qr_img, (box_x + 20, box_y + 20))

    # Purity Guarantee Note (NO TABLE NO)
    pledge_y = box_y + qr_size + 65
    pledge_text = "Pure Desi Ghee, Amul Butter & Pure Paneer Used In Cooking"
    bbox = draw.textbbox((0, 0), pledge_text, font=font_sub)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y), pledge_text, fill=(115, 0, 24), font=font_sub)

    prep_text = "Please Allow Us 20 Min Time For Each Order Preparation"
    bbox = draw.textbbox((0, 0), prep_text, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 40), prep_text, fill=(140, 100, 20), font=font_meta)

    draw.line([130, pledge_y + 90, w - 130, pledge_y + 90], fill=(197, 155, 39), width=1)

    # Address & Highway Location (NO CALL BUTTON)
    addr_1 = "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Indore"
    addr_2 = "Agra - Mumbai Highway - Near Highway Toll Plaza"

    bbox = draw.textbbox((0, 0), addr_1, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 115), addr_1, fill=(80, 50, 30), font=font_meta)

    bbox = draw.textbbox((0, 0), addr_2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 150), addr_2, fill=(100, 70, 40), font=font_meta)

    # Devotional Slogan & Hospitality Closing
    slogan_text = "\"Ek Baar Khaiye, Baar-Baar Aaiye\""
    bbox = draw.textbbox((0, 0), slogan_text, font=font_slogan)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 205), slogan_text, fill=(115, 0, 24), font=font_slogan)

    thanks_str = "Thank You For Visiting Shree Kripa Midway Restaurant"
    bbox = draw.textbbox((0, 0), thanks_str, font=font_thanks)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 260), thanks_str, fill=(180, 140, 30), font=font_thanks)

    for fn in output_filenames:
        canvas.save(fn, quality=95, dpi=(300, 300))
        print(f"[OK] Generated {fn} (300 DPI)")

def build_back_standee(config, output_filename="standee_back_printable.png"):
    """
    Generate 300 DPI Back Standee (Party Packages, Purity Promise, Slogans, Location)
    No Ambience, No Call Waiter, Ultra-Clean Royal Hospitality.
    """
    w, h = 1200, 1800
    canvas = create_luxury_parchment_background(w, h)
    draw = ImageDraw.Draw(canvas)
    draw_luxury_borders(draw, w, h)

    # 1. Logo
    logo_path = "logo_with_gold_rim.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA").resize((200, 200), Image.Resampling.LANCZOS)
        canvas.paste(logo, (int((w - 200) / 2), 65), mask=logo)

    font_brand = get_font(52, bold=True)
    font_title = get_font(38, bold=True)
    font_slogan = get_font(32, bold=True, italic=True)
    font_sub = get_font(23, bold=False)
    font_pkg_title = get_font(30, bold=True)
    font_pkg_name = get_font(26, bold=True)
    font_pkg_price = get_font(24, bold=True)
    font_meta = get_font(21, bold=False)
    font_trust = get_font(25, bold=True)
    font_thanks = get_font(25, bold=True)

    # Brand Title: SHREE KRIPA
    brand_text = "SHREE KRIPA"
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 285), brand_text, fill=(115, 0, 24), font=font_brand)

    title_text = "MIDWAY RESTAURANT"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 350), title_text, fill=(77, 0, 16), font=font_title)

    # Signature Slogans
    slogan_hi = "\"Ek Baar Khaiye, Baar-Baar Aaiye\""
    bbox = draw.textbbox((0, 0), slogan_hi, font=font_slogan)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 415), slogan_hi, fill=(115, 0, 24), font=font_slogan)

    slogan_en = "You Can Enjoy Delicious Food Serving Happiness, One Plate At A Time"
    bbox = draw.textbbox((0, 0), slogan_en, font=font_sub)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 470), slogan_en, fill=(100, 70, 30), font=font_sub)

    draw.line([140, 520, w - 140, 520], fill=(197, 155, 39), width=2)

    # 2. Grand Party Packages Card
    card_y = 560
    card_w = 1000
    card_h = 320
    card_x = (w - card_w) // 2

    draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill=(255, 252, 244), outline=(197, 155, 39), width=3)
    
    pkg_head = "BANQUET & PARTY PACKAGES"
    bbox = draw.textbbox((0, 0), pkg_head, font=font_pkg_title)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, card_y + 25), pkg_head, fill=(115, 0, 24), font=font_pkg_title)

    # 2 Packages Side by Side
    col_w = card_w // 2

    # Package 1: Kitty Party
    p1_t = "Kitty Party Package"
    bbox = draw.textbbox((0, 0), p1_t, font=font_pkg_name)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 85), p1_t, fill=(50, 20, 10), font=font_pkg_name)

    p1_p = "Started @ Rs 299"
    bbox = draw.textbbox((0, 0), p1_p, font=font_pkg_price)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 135), p1_p, fill=(160, 115, 20), font=font_pkg_price)

    p1_d1 = "Special Celebrations & Kitty Meals"
    bbox = draw.textbbox((0, 0), p1_d1, font=font_meta)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 190), p1_d1, fill=(90, 60, 40), font=font_meta)

    p1_d2 = "Starters - Main Course - Sweet Dessert"
    bbox = draw.textbbox((0, 0), p1_d2, font=font_meta)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 230), p1_d2, fill=(120, 80, 20), font=font_meta)

    # Vertical Divider Line
    draw.line([card_x + col_w, card_y + 75, card_x + col_w, card_y + 285], fill=(197, 155, 39), width=2)

    # Package 2: Lunch & Dinner Party
    p2_t = "Lunch & Dinner Party"
    bbox = draw.textbbox((0, 0), p2_t, font=font_pkg_name)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 85), p2_t, fill=(50, 20, 10), font=font_pkg_name)

    p2_p = "Started @ Rs 549"
    bbox = draw.textbbox((0, 0), p2_p, font=font_pkg_price)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 135), p2_p, fill=(160, 115, 20), font=font_pkg_price)

    p2_d1 = "Lavish Multi-Course Buffet Feast"
    bbox = draw.textbbox((0, 0), p2_d1, font=font_meta)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 190), p2_d1, fill=(90, 60, 40), font=font_meta)

    p2_d2 = "Paneer Exclusives - Tandoori Breads - Desi Ghee Halwa"
    bbox = draw.textbbox((0, 0), p2_d2, font=font_meta)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 230), p2_d2, fill=(120, 80, 20), font=font_meta)

    # 3. 100% Pure Desi Ghee Purity Promise Card (Replaced Ambience Photos)
    pledge_y = 930
    pledge_h = 240
    draw.rectangle([card_x, pledge_y, card_x + card_w, pledge_y + pledge_h], fill=(255, 252, 244), outline=(115, 0, 24), width=3)

    p_head = "100% PURE VEG & PURE DESI GHEE PROMISE"
    bbox = draw.textbbox((0, 0), p_head, font=font_pkg_name)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 25), p_head, fill=(115, 0, 24), font=font_pkg_name)

    p_t1 = "Pure Desi Ghee, Refined Oil, Amul Butter, Cheese, Milk, Curd, Paneer (Pure)"
    bbox = draw.textbbox((0, 0), p_t1, font=font_meta)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 80), p_t1, fill=(60, 40, 20), font=font_meta)

    p_t2 = "Are Exclusively Used In All Cooking & Preparations."
    bbox = draw.textbbox((0, 0), p_t2, font=font_meta)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 120), p_t2, fill=(60, 40, 20), font=font_meta)

    p_trust = "Taste, Quality & Pure Veg Dining Trust Since Inception"
    bbox = draw.textbbox((0, 0), p_trust, font=font_trust)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 175), p_trust, fill=(27, 122, 58), font=font_trust)

    # 4. Location & Hospitality Footer (No Call Button)
    draw.line([120, 1240, w - 120, 1240], fill=(197, 155, 39), width=1)

    addr_1 = "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Near Highway Toll Plaza"
    addr_2 = "Agra - Mumbai Highway, Indore, (M.P.) 453331"

    bbox = draw.textbbox((0, 0), addr_1, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1290), addr_1, fill=(80, 50, 30), font=font_meta)

    bbox = draw.textbbox((0, 0), addr_2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1335), addr_2, fill=(100, 70, 40), font=font_meta)

    thanks_str = "Thank You For Visiting Shree Kripa Midway Restaurant"
    bbox = draw.textbbox((0, 0), thanks_str, font=font_thanks)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1410), thanks_str, fill=(180, 140, 30), font=font_thanks)

    canvas.save(output_filename, quality=95, dpi=(300, 300))
    print(f"[OK] Generated {output_filename} (300 DPI)")

def main():
    cfg = load_config()

    if len(sys.argv) > 1 and sys.argv[1].startswith("http"):
        cfg["landingPageUrl"] = sys.argv[1]
        print(f"Using Custom Destination URL: {cfg['landingPageUrl']}")
    else:
        print(f"Using Destination URL: {cfg['landingPageUrl']}")

    print("Generating High-Resolution Luxury Front & Back Standees for Shree Kripa...")
    
    # 1. QR Code
    qr_menu = generate_styled_qr(cfg["landingPageUrl"])
    qr_menu.save("qr_code.png")
    qr_menu.save("qr_landing_page.png")
    print("[OK] Saved qr_code.png")

    # 2. Front Standee (300 DPI)
    build_front_standee(cfg, ["table_standee_printable.png", "standee_front_printable.png"])

    # 3. Back Standee (300 DPI)
    build_back_standee(cfg, "standee_back_printable.png")

    print("[SUCCESS] Official Shree Kripa Front & Back Standees created at 300 DPI!")

if __name__ == "__main__":
    main()
