"""
Official Luxury Front & Back Standee Generator for Shree Kripa Midway Restaurant
- Designed around the actual Restaurant Interior (Peacock Teal Velvet, Warm Golden Cove Ceiling Lights & Golden Sun Arches)
- HospitalityQR Architecture:
  1. Front Standee: Royal Shree Kripa Branding + QR Menu + Pure Desi Ghee Purity Guarantee + Highway Address
     (No Table No, No Call Button)
  2. Back Standee: Slogans + Banquet/Party Packages (@299, @549) + 100% Pure Desi Ghee Promise + Highway Address
     (No Call Button)
- High-Resolution 300 DPI Ready for Acrylic Table Stands
- URL: https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/
"""

import sys
import os
import re
import math
import numpy as np
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

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

def create_interior_luxury_background(w, h, bg_image_path="assets/interior_hero.jpg"):
    """
    Create an extraordinary luxury background inspired by Shree Kripa's actual interior:
    - Blends the real Peacock Teal velvet dining room & warm golden cove ceiling lights
    - Applies a rich Velvet Peacock Teal & Warm Amber Gold atmospheric gradient
    """
    # 1. Base gradient in Peacock Teal & Deep Cove Gold
    cx, cy = w / 2.0, h * 0.28
    max_r = math.sqrt(cx**2 + (h - cy)**2)

    y, x = np.ogrid[:h, :w]
    dist = np.sqrt((x - cx)**2 + ((y - cy) * 0.85)**2)
    norm_dist = np.clip(dist / (max_r * 0.95), 0.0, 1.0)

    # Rich Peacock Teal palette matching the velvet chairs & golden cove lighting
    c_center = np.array([15, 78, 85], dtype=np.float32)   # Luminous Peacock Teal
    c_mid = np.array([8, 48, 54], dtype=np.float32)       # Deep Velvet Teal
    c_edge = np.array([4, 24, 28], dtype=np.float32)      # Midnight Emerald-Teal

    mid_point = 0.48
    factor1 = np.clip(norm_dist / mid_point, 0.0, 1.0)[:, :, None]
    grad_inner = c_center * (1.0 - factor1) + c_mid * factor1

    factor2 = np.clip((norm_dist - mid_point) / (1.0 - mid_point), 0.0, 1.0)[:, :, None]
    grad_outer = c_mid * (1.0 - factor2) + c_edge * factor2

    base_rgb = np.where(norm_dist[:, :, None] < mid_point, grad_inner, grad_outer)

    # Add warm golden cove lighting glow at the top arch
    top_dist = np.sqrt((x - w / 2.0)**2 + ((y - 180.0) * 1.4)**2)
    top_glow = np.clip(1.0 - (top_dist / 620.0), 0.0, 1.0)[:, :, None] ** 2
    gold_tint = np.array([212, 175, 55], dtype=np.float32)
    base_rgb = base_rgb * (1.0 - top_glow * 0.28) + gold_tint * (top_glow * 0.28)

    grad_img = Image.fromarray(np.clip(base_rgb, 0, 255).astype(np.uint8), mode="RGB")

    # 2. Blend real restaurant interior photo if available
    if os.path.exists(bg_image_path):
        try:
            photo = Image.open(bg_image_path).convert("RGB")
            # Cover-fit resize to (w, h)
            pw, ph = photo.size
            scale = max(w / pw, h / ph)
            nw, nh = int(pw * scale), int(ph * scale)
            photo = photo.resize((nw, nh), Image.Resampling.LANCZOS)
            left = (nw - w) // 2
            top = (nh - h) // 2
            photo = photo.crop((left, top, left + w, top + h))

            # Soft atmospheric blur so foreground text & QR remain 100% ultra-crisp
            photo_blur = photo.filter(ImageFilter.GaussianBlur(radius=8))
            photo_blur = ImageEnhance.Brightness(photo_blur).enhance(0.85)
            photo_blur = ImageEnhance.Color(photo_blur).enhance(1.15)

            # Blend 34% real interior photo + 66% rich Peacock Teal & Gold lighting gradient
            blended = Image.blend(grad_img, photo_blur, alpha=0.34)
            return blended
        except Exception as e:
            print("Notice: Could not blend interior photo, using luxury gradient:", e)

    return grad_img

def generate_styled_qr(data, box_size=15, border=2, fill_color=(7, 46, 52), back_color=(255, 255, 255)):
    """Generate crisp, high contrast QR code in Deep Peacock Teal"""
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

def draw_luxury_borders_and_arches(draw, w, h):
    """Draw ornate golden cove borders, corner sun-discs & architectural arch accents"""
    # Outer Warm Gold frame
    draw.rectangle([22, 22, w - 22, h - 22], outline=(212, 175, 55), width=5)
    # Second inner gold filigree line
    draw.rectangle([34, 34, w - 34, h - 34], outline=(245, 218, 137), width=2)
    # Third fine line
    draw.rectangle([44, 44, w - 44, h - 44], outline=(160, 125, 25), width=1)

    # 4 Corner Ornaments (Inspired by the golden sun discs & geometric mandala on the walls)
    corners = [(28, 28), (w - 28, 28), (28, h - 28), (w - 28, h - 28)]
    for cx, cy in corners:
        draw.polygon([(cx - 14, cy), (cx, cy - 14), (cx + 14, cy), (cx, cy + 14)], fill=(212, 175, 55))
        draw.polygon([(cx - 7, cy), (cx, cy - 7), (cx + 7, cy), (cx, cy + 7)], fill=(8, 48, 54))

def draw_rounded_card(draw, box, fill, outline, width=3, radius=28):
    """Draw a rounded rectangle card"""
    try:
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)
    except Exception:
        draw.rectangle(box, fill=fill, outline=outline, width=width)

def build_front_standee(config, output_filenames=["table_standee_printable.png", "standee_front_printable.png"]):
    """
    Generate 300 DPI Front Standee (Peacock Teal & Warm Golden Cove Interior Theme)
    No Table No, No Call Button.
    """
    w, h = 1200, 1800
    canvas = create_interior_luxury_background(w, h, "assets/interior_hero.jpg")
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw_luxury_borders_and_arches(draw, w, h)

    # Subtle top golden sun disc halo behind logo (inspired by the restaurant's yellow sun murals)
    draw.ellipse([w // 2 - 118, 58, w // 2 + 118, 294], fill=(232, 185, 49, 55), outline=(245, 218, 137, 180), width=2)

    # 1. Official Logo with Gold Rim
    logo_path = "logo_with_gold_rim.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((210, 210), Image.Resampling.LANCZOS)
        canvas.paste(logo, (int((w - 210) / 2), 70), mask=logo)

    font_brand = get_font(54, bold=True)
    font_title = get_font(36, bold=True)
    font_veg = get_font(22, bold=True)
    font_cta = get_font(38, bold=True)
    font_meta = get_font(22, bold=False)
    font_sub = get_font(26, bold=True)
    font_slogan = get_font(28, bold=True, italic=True)
    font_thanks = get_font(25, bold=True)

    # Brand Title: SHREE KRIPA (Warm Luminous Gold)
    brand_text = "SHREE KRIPA"
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    draw.text(((w - (bbox[2] - bbox[0])) / 2 + 2, 297), brand_text, fill=(0, 0, 0, 140), font=font_brand)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 295), brand_text, fill=(251, 230, 155), font=font_brand)

    # Subtitle: MIDWAY RESTAURANT
    title_text = "MIDWAY RESTAURANT"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 362), title_text, fill=(255, 252, 245), font=font_title)

    # 100% Pure Veg Pill Badge
    pill_w, pill_h = 520, 44
    pill_x = (w - pill_w) // 2
    pill_y = 418
    draw_rounded_card(draw, [pill_x, pill_y, pill_x + pill_w, pill_y + pill_h], fill=(12, 85, 50, 230), outline=(212, 175, 55), width=2, radius=22)
    veg_text = "100% PURE VEG  •  PURE DESI GHEE"
    bbox = draw.textbbox((0, 0), veg_text, font=font_veg)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pill_y + 9), veg_text, fill=(255, 255, 255), font=font_veg)

    # Center Luxury Cream & Gold Arch Panel for QR Code
    panel_w, panel_h = 820, 760
    panel_x = (w - panel_w) // 2
    panel_y = 490
    draw_rounded_card(
        draw,
        [panel_x, panel_y, panel_x + panel_w, panel_y + panel_h],
        fill=(255, 252, 244, 248),
        outline=(212, 175, 55),
        width=4,
        radius=32
    )
    draw_rounded_card(
        draw,
        [panel_x + 10, panel_y + 10, panel_x + panel_w - 10, panel_y + panel_h - 10],
        fill=None,
        outline=(197, 155, 39, 120),
        width=1,
        radius=24
    )

    # Call to action inside panel: SCAN FOR DIGITAL MENU
    cta_text = "SCAN FOR DIGITAL MENU"
    bbox = draw.textbbox((0, 0), cta_text, font=font_cta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, panel_y + 28), cta_text, fill=(9, 62, 68), font=font_cta)

    sub_cta = "Explore 170+ Dishes  •  Party Packages  •  Instant Menu"
    bbox = draw.textbbox((0, 0), sub_cta, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, panel_y + 82), sub_cta, fill=(140, 100, 20), font=font_meta)

    # QR Code Box
    qr_url = config.get("landingPageUrl", "https://hospitalityqr.github.io/Shree-Kripa-Midway-Restaurant/")
    qr_img = generate_styled_qr(qr_url, box_size=15, border=2, fill_color=(7, 46, 52))
    qr_size = 540
    qr_img = qr_img.resize((qr_size, qr_size), Image.Resampling.LANCZOS)

    box_x = int((w - qr_size - 36) / 2)
    box_y = panel_y + 130
    draw_rounded_card(draw, [box_x, box_y, box_x + qr_size + 36, box_y + qr_size + 36], fill=(255, 255, 255), outline=(212, 175, 55), width=3, radius=18)
    canvas.paste(qr_img, (box_x + 18, box_y + 18))

    # Purity Guarantee Card below QR Panel (NO TABLE NO)
    pledge_y = panel_y + panel_h + 30
    pledge_w = 980
    pledge_x = (w - pledge_w) // 2
    draw_rounded_card(
        draw,
        [pledge_x, pledge_y, pledge_x + pledge_w, pledge_y + 115],
        fill=(6, 38, 43, 225),
        outline=(212, 175, 55),
        width=2,
        radius=20
    )

    pledge_text = "Pure Desi Ghee, Amul Butter & Pure Paneer Used In Cooking"
    bbox = draw.textbbox((0, 0), pledge_text, font=font_sub)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 20), pledge_text, fill=(251, 230, 155), font=font_sub)

    prep_text = "Please Allow Us 20 Min Time For Fresh Order Preparation"
    bbox = draw.textbbox((0, 0), prep_text, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, pledge_y + 64), prep_text, fill=(235, 245, 245), font=font_meta)

    # Address & Highway Location (NO CALL BUTTON)
    footer_y = pledge_y + 145
    addr_1 = "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Indore"
    addr_2 = "Agra - Mumbai Highway  •  Near Highway Toll Plaza"

    bbox = draw.textbbox((0, 0), addr_1, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, footer_y), addr_1, fill=(255, 252, 245), font=font_meta)

    bbox = draw.textbbox((0, 0), addr_2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, footer_y + 34), addr_2, fill=(212, 175, 55), font=font_meta)

    # Devotional Slogan & Hospitality Closing
    slogan_text = "\"Ek Baar Khaiye, Baar-Baar Aaiye\""
    bbox = draw.textbbox((0, 0), slogan_text, font=font_slogan)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, footer_y + 82), slogan_text, fill=(251, 230, 155), font=font_slogan)

    thanks_str = "Thank You For Visiting Shree Kripa Midway Restaurant"
    bbox = draw.textbbox((0, 0), thanks_str, font=font_thanks)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, footer_y + 130), thanks_str, fill=(255, 255, 255), font=font_thanks)

    for fn in output_filenames:
        canvas.save(fn, quality=95, dpi=(300, 300))
        print(f"[OK] Generated {fn} (300 DPI)")

def build_back_standee(config, output_filename="standee_back_printable.png"):
    """
    Generate 300 DPI Back Standee (Peacock Teal & Golden Cove Interior Theme)
    Party Packages, Purity Promise, Slogans, Location.
    """
    w, h = 1200, 1800
    canvas = create_interior_luxury_background(w, h, "assets/interior_hero.jpg")
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw_luxury_borders_and_arches(draw, w, h)

    # Top golden sun disc halo behind logo
    draw.ellipse([w // 2 - 112, 58, w // 2 + 112, 282], fill=(232, 185, 49, 55), outline=(245, 218, 137, 180), width=2)

    # 1. Logo
    logo_path = "logo_with_gold_rim.png"
    if os.path.exists(logo_path):
        logo = Image.open(logo_path).convert("RGBA").resize((200, 200), Image.Resampling.LANCZOS)
        canvas.paste(logo, (int((w - 200) / 2), 70), mask=logo)

    font_brand = get_font(52, bold=True)
    font_title = get_font(36, bold=True)
    font_slogan = get_font(32, bold=True, italic=True)
    font_sub = get_font(23, bold=False)
    font_pkg_title = get_font(30, bold=True)
    font_pkg_name = get_font(27, bold=True)
    font_pkg_price = get_font(26, bold=True)
    font_meta = get_font(22, bold=False)
    font_trust = get_font(25, bold=True)
    font_thanks = get_font(25, bold=True)

    # Brand Title: SHREE KRIPA
    brand_text = "SHREE KRIPA"
    bbox = draw.textbbox((0, 0), brand_text, font=font_brand)
    draw.text(((w - (bbox[2] - bbox[0])) / 2 + 2, 287), brand_text, fill=(0, 0, 0, 140), font=font_brand)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 285), brand_text, fill=(251, 230, 155), font=font_brand)

    title_text = "MIDWAY RESTAURANT"
    bbox = draw.textbbox((0, 0), title_text, font=font_title)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 350), title_text, fill=(255, 252, 245), font=font_title)

    # Signature Slogans
    slogan_hi = "\"Ek Baar Khaiye, Baar-Baar Aaiye\""
    bbox = draw.textbbox((0, 0), slogan_hi, font=font_slogan)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 412), slogan_hi, fill=(251, 230, 155), font=font_slogan)

    slogan_en = "You Can Enjoy Delicious Food Serving Happiness, One Plate At A Time"
    bbox = draw.textbbox((0, 0), slogan_en, font=font_sub)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 465), slogan_en, fill=(235, 245, 245), font=font_sub)

    draw.line([140, 515, w - 140, 515], fill=(212, 175, 55), width=2)

    # 2. Grand Party Packages Card (Warm Ivory & Gold Arch Panel)
    card_y = 550
    card_w = 1020
    card_h = 340
    card_x = (w - card_w) // 2

    draw_rounded_card(draw, [card_x, card_y, card_x + card_w, card_y + card_h], fill=(255, 252, 244, 248), outline=(212, 175, 55), width=4, radius=28)
    
    pkg_head = "BANQUET & PARTY PACKAGES"
    bbox = draw.textbbox((0, 0), pkg_head, font=font_pkg_title)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, card_y + 25), pkg_head, fill=(9, 62, 68), font=font_pkg_title)

    # 2 Packages Side by Side
    col_w = card_w // 2

    # Package 1: Kitty Party
    p1_t = "Kitty Party Package"
    bbox = draw.textbbox((0, 0), p1_t, font=font_pkg_name)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 90), p1_t, fill=(40, 25, 15), font=font_pkg_name)

    p1_p = "Started @ Rs 299"
    bbox = draw.textbbox((0, 0), p1_p, font=font_pkg_price)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 142), p1_p, fill=(115, 0, 24), font=font_pkg_price)

    p1_d1 = "Special Celebrations & Kitty Meals"
    bbox = draw.textbbox((0, 0), p1_d1, font=font_meta)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 200), p1_d1, fill=(70, 55, 40), font=font_meta)

    p1_d2 = "Starters • Main Course • Sweet Dessert"
    bbox = draw.textbbox((0, 0), p1_d2, font=font_meta)
    draw.text((card_x + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 240), p1_d2, fill=(140, 100, 20), font=font_meta)

    # Vertical Divider Line
    draw.line([card_x + col_w, card_y + 80, card_x + col_w, card_y + 295], fill=(212, 175, 55), width=2)

    # Package 2: Lunch & Dinner Party
    p2_t = "Lunch & Dinner Party"
    bbox = draw.textbbox((0, 0), p2_t, font=font_pkg_name)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 90), p2_t, fill=(40, 25, 15), font=font_pkg_name)

    p2_p = "Started @ Rs 549"
    bbox = draw.textbbox((0, 0), p2_p, font=font_pkg_price)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 142), p2_p, fill=(115, 0, 24), font=font_pkg_price)

    p2_d1 = "Lavish Multi-Course Buffet Feast"
    bbox = draw.textbbox((0, 0), p2_d1, font=font_meta)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 200), p2_d1, fill=(70, 55, 40), font=font_meta)

    p2_d2 = "Paneer Exclusives • Tandoori Breads • Halwa"
    bbox = draw.textbbox((0, 0), p2_d2, font=font_meta)
    draw.text((card_x + col_w + (col_w - (bbox[2] - bbox[0])) / 2, card_y + 240), p2_d2, fill=(140, 100, 20), font=font_meta)

    # 3. 100% Pure Desi Ghee Purity Promise Card
    pledge_y = 935
    pledge_h = 260
    draw_rounded_card(draw, [card_x, pledge_y, card_x + card_w, pledge_y + pledge_h], fill=(255, 252, 244, 248), outline=(212, 175, 55), width=4, radius=28)

    p_head = "100% PURE VEG & PURE DESI GHEE PROMISE"
    bbox = draw.textbbox((0, 0), p_head, font=font_pkg_name)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 28), p_head, fill=(9, 62, 68), font=font_pkg_name)

    p_t1 = "Pure Desi Ghee, Refined Oil, Amul Butter, Cheese, Milk, Curd, Paneer (Pure)"
    bbox = draw.textbbox((0, 0), p_t1, font=font_meta)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 88), p_t1, fill=(60, 40, 20), font=font_meta)

    p_t2 = "Are Exclusively Used In All Cooking & Preparations."
    bbox = draw.textbbox((0, 0), p_t2, font=font_meta)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 128), p_t2, fill=(60, 40, 20), font=font_meta)

    p_trust = "Taste, Quality & Pure Veg Dining Trust Since Inception"
    bbox = draw.textbbox((0, 0), p_trust, font=font_trust)
    draw.text((card_x + (card_w - (bbox[2] - bbox[0])) / 2, pledge_y + 188), p_trust, fill=(27, 122, 58), font=font_trust)

    # 4. Location & Hospitality Footer
    draw.line([140, 1245, w - 140, 1245], fill=(212, 175, 55), width=2)

    addr_1 = "Near Maharana Pratap Bridge, Pigdamber, Rau, NH 3, Near Highway Toll Plaza"
    addr_2 = "Agra - Mumbai Highway, Indore, (M.P.) 453331"

    bbox = draw.textbbox((0, 0), addr_1, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1290), addr_1, fill=(255, 252, 245), font=font_meta)

    bbox = draw.textbbox((0, 0), addr_2, font=font_meta)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1335), addr_2, fill=(212, 175, 55), font=font_meta)

    thanks_str = "Thank You For Visiting Shree Kripa Midway Restaurant"
    bbox = draw.textbbox((0, 0), thanks_str, font=font_thanks)
    draw.text(((w - (bbox[2] - bbox[0])) / 2, 1410), thanks_str, fill=(251, 230, 155), font=font_thanks)

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

    # 1b. Save shared Luxury Interior Background for Landing Page (index.html) & Standee HTML
    bg_shared = create_interior_luxury_background(1200, 1800, "assets/interior_hero.jpg")
    bg_shared.save("assets/luxury_interior_bg.jpg", quality=92)
    print("[OK] Saved assets/luxury_interior_bg.jpg")

    # 2. Front Standee (300 DPI)
    build_front_standee(cfg, ["table_standee_printable.png", "standee_front_printable.png"])

    # 3. Back Standee (300 DPI)
    build_back_standee(cfg, "standee_back_printable.png")

    print("[SUCCESS] Official Shree Kripa Front & Back Standees created at 300 DPI!")

if __name__ == "__main__":
    main()
