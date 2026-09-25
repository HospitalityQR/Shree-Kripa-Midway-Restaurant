"""
Official Luxury Front & Back Standee Generator for Shree Kripa Midway Restaurant
- HospitalityQR Architecture:
  1. Front Standee: Logo + Sri Krishna Flute/Mor Pankh + QR Menu + Table No + Call Button + Desi Ghee Purity
  2. Back Standee: Slogans + Banquet/Party Packages (@299, @549) + Ambience Photos + Highway Address + Helpline
- High-Resolution 300 DPI Ready for Acrylic Table Stands
- URL: https://hospitalityqr.github.io/shree-kripa-QR/
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
        "restaurantName": "श्री कृपा",
        "restaurantSubname": "MIDWAY RESTAURANT",
        "tagline": "MIDWAY RESTAURANT • 100% PURE VEG",
        "landingPageUrl": "https://hospitalityqr.github.io/shree-kripa-QR/",
        "phoneNumber": "9111030307",
        "phoneButtonText": "Call / Table Order: +91-91110-30307",
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
    Generate a warm royal parchment texture with subtle golden radial glow
    and fine artistic shading (matching the menu PDF).
    """
    cx, cy = w / 2.0, h * 0.35
    max_r = math.sqrt(cx**2 + (h - cy)**2)

    y, x = np.ogrid[:h, :w]
    dist = np.sqrt((x - cx)**2 + ((y - cy) * 0.9)**2)
    norm_dist = np.clip(dist / (max_r * 0.95), 0.0, 1.0)

    c_center = np.array([255, 252, 244], dtype=np.float32)
    c_mid = np.array([247, 237, 218], dtype=np.float32)
    c_edge = np.array([233, 212, 178], dtype=np.float32)

    mid_point = 0.52
    factor1 = np.clip(norm_dist / mid_point, 0.0, 1.0)[:, :, None]
    grad_inner = c_center * (1.0 - factor1) + c_mid * factor1

    factor2 = np.clip((norm_dist - mid_point) / (1.0 - mid_point), 0.0, 1.0)[:, :, None]
    grad_outer = c_mid * (1.0 - factor2) + c_edge * factor2

    base_rgb = np.where(norm_dist[:, :, None] < mid_point, grad_inner, grad_outer)

    np.random.seed(42)
    noise = np.random.normal(0.0, 1.8, (h, w, 1)).astype(np.float32)
    base_rgb = np.clip(base_rgb + noise, 0, 255).astype(np.uint8)

    return Image.fromarray(base_rgb, mode="RGB")

def generate_styled_qr(data, box_size=14, border=2, fill_color=(115, 0, 24), back_color=(255, 255, 255)):
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

def get_font(size, bold=False):
    """Attempt to load system font, fallback to default"""
    candidates = [
        "C:\\Windows\\Fonts\\Georgia.ttf" if not bold else "C:\\Windows\\Fonts\\Georgiab.ttf",
        "C:\\Windows\\Fonts\\arial.ttf" if not bold else "C:\\Windows\\Fonts\\arialbd.ttf",
        "C:\\Windows\\Fonts\\segoeui.ttf" if not bold else "C:\\Windows\\Fonts\\segoeuib.ttf"
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_luxury_borders(draw, w, h):
    """Draw ornate royal gold borders & corner diamond accents"""
    draw.rectangle([24, 24, w - 24, h - 24], outline=(197, 155, 39), width=4)
    draw.rectangle([34, 34, w - 34, h - 34], outline=(140, 107, 18), width=1)

    corners = [(24, 24), (w - 24, 24), (24, h - 24), (w - 24, h - 24)]
    for cx, cy in corners:
        draw.polygon([(cx - 8, cy), (cx, cy - 8), (cx + 8, cy), (cx, cy + 8)], fill=(197, 155, 39))

def build_front_standee(config, output_filenames=["table_standee_printable.png", "standee_front_printable.png"]):
    """
    Generate 300 DPI Front Standee (QR Code + Table Ordering)
    """
    w, h = 1200, 1800
    canvas = create_luxury_parchment_background(w, h)
    draw = ImageDraw.Draw(canvas)
    draw_luxury_borders(draw, w, h)

    # 1. Official Logo
    logo_path = "logo_with_gold_rim.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((190, 190), Image.Resampling.LANCZOS)
        canvas.paste(logo, (int((w - 190) / 2), 70), mask=logo)

    font_title = get_font(56, bold=True)
    font_sub = get_font(28, bold=True)
    font_veg = get_font(22, bold=True)
    font_cta = get_font(38, bold=True)
    font_meta = get_font(21, bold=False)

    title_text = "MIDWAY RESTAURANT"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 280), title_text, fill=(115, 0, 24), font=font_title)

    veg_text = "100% PURE VEG - PURE DESI GHEE"
    bbox = draw.textbbox((0, 0), veg_text, font=font_veg)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 355), veg_text, fill=(27, 122, 58), font=font_veg)

    draw.line([150, 400, w - 150, 400], fill=(197, 155, 39), width=2)

    # Call to action
    cta_text = "SCAN FOR DIGITAL MENU"
    bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 430), cta_text, fill=(77, 0, 16), font=font_cta)

    sub_cta = "Explore 170+ Dishes - Table Ordering - Instant Service"
    bbox = draw.textbbox((0, 0), sub_cta, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 485), sub_cta, fill=(100, 70, 30), font=font_meta)

    # QR Code Box
    qr_url = config.get("landingPageUrl", "https://hospitalityqr.github.io/shree-kripa-QR/")
    qr_img = generate_styled_qr(qr_url, box_size=15, border=2, fill_color=(115, 0, 24))
    qr_size = 550
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    box_x = int((w - qr_size - 40) / 2)
    box_y = 540
    draw.rectangle([box_x, box_y, box_x + qr_size + 40, box_y + qr_size + 40], fill=(255, 255, 255), outline=(197, 155, 39), width=4)
    canvas.paste(qr_img, (box_x + 20, box_y + 20))

    # Table Number Pill Placeholder
    table_pill_y = box_y + qr_size + 65
    draw.rectangle([(w - 340) / 2, table_pill_y, (w + 340) / 2, table_pill_y + 52], fill=(255, 252, 244), outline=(115, 0, 24), width=2)
    tbl_text = "TABLE NO: ________"
    bbox = draw.textbbox((0, 0), tbl_text, font=font_sub)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, table_pill_y + 10), tbl_text, fill=(115, 0, 24), font=font_sub)

    # Purity Guarantee Note
    pledge_text = "Pure Desi Ghee, Amul Butter & Pure Paneer Are Used In Cooking"
    bbox = draw.textbbox((0, 0), pledge_text, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1260), pledge_text, fill=(115, 0, 24), font=font_meta)

    prep_text = "Please Allow Us 20 Min Time For Each Order Preparation"
    bbox = draw.textbbox((0, 0), prep_text, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1300), prep_text, fill=(140, 100, 20), font=font_meta)

    draw.line([120, 1360, w - 120, 1360], fill=(197, 155, 39), width=1)

    # Address & Phone
    addr_1 = "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Indore"
    addr_2 = "Agra - Mumbai Highway - Near Highway Toll Plaza"
    phone_str = config.get("phoneButtonText", "Call / Table Order: +91-91110-30307")

    bbox = draw.textbbox((0, 0), addr_1, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1400), addr_1, fill=(80, 50, 30), font=font_meta)

    bbox = draw.textbbox((0, 0), addr_2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1435), addr_2, fill=(100, 70, 40), font=font_meta)

    font_phone = get_font(26, bold=True)
    bbox = draw.textbbox((0, 0), phone_str, font=font_phone)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1485), phone_str, fill=(115, 0, 24), font=font_phone)

    font_thanks = get_font(24, bold=True)
    thanks_str = "Thank You For Visiting Shree Kripa Midway Restaurant"
    bbox = draw.textbbox((0, 0), thanks_str, font=font_thanks)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1550), thanks_str, fill=(197, 155, 39), font=font_thanks)

    for fn in output_filenames:
        canvas.save(fn, quality=95, dpi=(300, 300))
        print(f"[OK] Generated {fn} (300 DPI)")

def build_back_standee(config, output_filename="standee_back_printable.png"):
    """
    Generate 300 DPI Back Standee (Ambience, Slogans, Party Packages, Contact)
    """
    w, h = 1200, 1800
    canvas = create_luxury_parchment_background(w, h)
    draw = ImageDraw.Draw(canvas)
    draw_luxury_borders(draw, w, h)

    # Logo
    logo_path = "logo_with_gold_rim.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA").resize((170, 170), Image.Resampling.LANCZOS)
        canvas.paste(logo, (int((w - 170) / 2), 65), mask=logo)

    font_title = get_font(52, bold=True)
    font_slogan = get_font(26, bold=True)
    font_sub = get_font(23, bold=False)
    font_pkg_title = get_font(28, bold=True)
    font_pkg_price = get_font(24, bold=True)
    font_meta = get_font(20, bold=False)

    title_text = "MIDWAY RESTAURANT"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 250), title_text, fill=(115, 0, 24), font=font_title)

    # Slogan
    slogan_en = "You Can Enjoy Delicious Food Serving Happiness, One Plate At A Time"
    bbox = draw.textbbox((0, 0), slogan_en, font=font_sub)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 320), slogan_en, fill=(100, 70, 30), font=font_sub)

    draw.line([140, 370, w - 140, 370], fill=(197, 155, 39), width=2)

    # Party Packages Card
    card_y = 410
    card_w = 980
    card_h = 240
    card_x = (w - card_w) // 2

    draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill=(255, 252, 244), outline=(197, 155, 39), width=2)
    
    pkg_head = "BANQUET & PARTY PACKAGES"
    bbox = draw.textbbox((0, 0), pkg_head, font=font_pkg_title)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, card_y + 20), pkg_head, fill=(115, 0, 24), font=font_pkg_title)

    # 2 Packages Side by Side
    col_w = card_w // 2
    # Package 1
    p1_t = "Kitty Party Package"
    bbox = draw.textbbox((0, 0), p1_t, font=font_slogan)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 80), p1_t, fill=(50, 20, 10), font=font_slogan)

    p1_p = "Started @ Rs 299"
    bbox = draw.textbbox((0, 0), p1_p, font=font_pkg_price)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 125), p1_p, fill=(140, 100, 18), font=font_pkg_price)

    p1_d = "Special Celebrations & Kitty Meals"
    bbox = draw.textbbox((0, 0), p1_d, font=font_meta)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 175), p1_d, fill=(100, 80, 60), font=font_meta)

    # Package 2
    draw.line([card_x + col_w, card_y + 60, card_x + col_w, card_y + 200], fill=(197, 155, 39), width=1)

    p2_t = "Lunch & Dinner Party"
    bbox = draw.textbbox((0, 0), p2_t, font=font_slogan)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 80), p2_t, fill=(50, 20, 10), font=font_slogan)

    p2_p = "Started @ Rs 549"
    bbox = draw.textbbox((0, 0), p2_p, font=font_pkg_price)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 125), p2_p, fill=(140, 100, 18), font=font_pkg_price)

    p2_d = "Lavish Multi-Course Buffet Feast"
    bbox = draw.textbbox((0, 0), p2_d, font=font_meta)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 175), p2_d, fill=(100, 80, 60), font=font_meta)

    # Ambience Photos (From PDF Page 14)
    amb_y = 690
    photos = [
        ("assets/ambience_exterior.jpg", "Grand Highway Entrance"),
        ("assets/ambience_reception.jpg", "Royal Reception Desk"),
        ("assets/ambience_arch.jpg", "Floral Welcome Arch")
    ]
    img_w, img_h = 300, 200
    total_imgs_w = len(photos) * img_w + (len(photos) - 1) * 30
    start_x = (w - total_imgs_w) // 2

    for i, (path, cap) in enumerate(photos):
        px = start_x + i * (img_w + 30)
        if os.path.exists(path):
            pic = Image.open(path).convert("RGBA").resize((img_w, img_h), Image.Resampling.LANCZOS)
            canvas.paste(pic, (px, amb_y))
            draw.rectangle([px, amb_y, px + img_w, amb_y + img_h], outline=(197, 155, 39), width=2)
            bbox = draw.textbbox((0, 0), cap, font=font_meta)
            draw.text((px + (img_w - (bbox[2] - bbox[0])) / 2, amb_y + img_h + 10), cap, fill=(115, 0, 24), font=font_meta)

    # Purity Pledge Box
    pledge_y = 970
    draw.rectangle([(w - 980) / 2, pledge_y, (w + 980) / 2, pledge_y + 120], fill=(255, 252, 244), outline=(115, 0, 24), width=2)
    p_t1 = "100% PURE VEG COOKING PROMISE"
    bbox = draw.textbbox((0, 0), p_t1, font=font_slogan)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 20), p_t1, fill=(115, 0, 24), font=font_slogan)

    p_t2 = "Pure Desi Ghee, Refined Oil, Amul Butter, Cheese, Milk, Curd, Paneer (Pure) Used In Cooking"
    bbox = draw.textbbox((0, 0), p_t2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 65), p_t2, fill=(60, 40, 20), font=font_meta)

    # Location & Call Footer
    draw.line([120, 1140, w - 120, 1140], fill=(197, 155, 39), width=1)

    addr_1 = "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Near Highway Toll Plaza"
    addr_2 = "Agra - Mumbai Hwy, Indore, (M.P.) 453331"
    phone_str = config.get("phoneButtonText", "Call / Table Order: +91-91110-30307")

    bbox = draw.textbbox((0, 0), addr_1, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1180), addr_1, fill=(80, 50, 30), font=font_meta)

    bbox = draw.textbbox((0, 0), addr_2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1220), addr_2, fill=(100, 70, 40), font=font_meta)

    font_phone = get_font(28, bold=True)
    bbox = draw.textbbox((0, 0), phone_str, font=font_phone)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1275), phone_str, fill=(115, 0, 24), font=font_phone)

    font_thanks = get_font(24, bold=True)
    thanks_str = "Thank You For Visiting Shree Kripa Midway Restaurant"
    bbox = draw.textbbox((0, 0), thanks_str, font=font_thanks)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1350), thanks_str, fill=(197, 155, 39), font=font_thanks)

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
