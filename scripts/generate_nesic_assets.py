import os
import sys
import re
from PIL import Image, ImageDraw

REPO_ROOT = r"C:\Users\Mrs Thao\.gemini\antigravity\scratch\Dmusic"
SOURCE_IMAGE_PATH = r"C:\Users\Mrs Thao\.gemini\antigravity\brain\26a44a7c-e0e7-4f8a-8d1a-b4b941911bbc\.user_uploaded\media_1795157466979_04c377f2.jpg"

def generate_assets():
    print("=== 1. GENERATING NESIC ASSETS ===")
    src_raw = Image.open(SOURCE_IMAGE_PATH).convert("RGBA")
    
    # The squircle is within (96, 96, 928, 928)
    squircle_crop = src_raw.crop((96, 96, 928, 928))
    
    # 1.1 Helpers for masks
    def make_rounded(img, size, radius_ratio=0.22):
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        supersample = 4
        mask_size = size * supersample
        radius = int(mask_size * radius_ratio)
        mask = Image.new("L", (mask_size, mask_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, mask_size - 1, mask_size - 1), radius=radius, fill=255)
        mask = mask.resize((size, size), Image.Resampling.LANCZOS)
        out = resized.copy()
        out.putalpha(mask)
        return out

    def make_circle(img, size, padding_ratio=0.02):
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        supersample = 4
        mask_size = size * supersample
        pad = int(mask_size * padding_ratio)
        mask = Image.new("L", (mask_size, mask_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((pad, pad, mask_size - pad - 1, mask_size - pad - 1), fill=255)
        mask = mask.resize((size, size), Image.Resampling.LANCZOS)
        out = resized.copy()
        out.putalpha(mask)
        return out

    def make_square(img, size):
        return img.resize((size, size), Image.Resampling.LANCZOS)

    # 1.2 ComposeApp icons
    icon_dir = os.path.join(REPO_ROOT, "composeApp", "icon")
    os.makedirs(icon_dir, exist_ok=True)
    
    circle_512 = make_circle(squircle_crop, 512)
    circle_png_path = os.path.join(icon_dir, "circle_app_icon.png")
    circle_512.save(circle_png_path, "PNG")
    print("Saved:", circle_png_path)
    
    ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ico_path = os.path.join(icon_dir, "circle_app_icon.ico")
    circle_512.save(ico_path, format="ICO", sizes=ico_sizes)
    print("Saved:", ico_path)
    
    circle_1024 = make_circle(squircle_crop, 1024)
    circle_icns_path = os.path.join(icon_dir, "circle_app_icon.icns")
    circle_1024.save(circle_icns_path, format="ICNS")
    print("Saved:", circle_icns_path)
    
    rounded_512 = make_rounded(squircle_crop, 512)
    rounded_png_path = os.path.join(icon_dir, "rounded_app_icon.png")
    rounded_512.save(rounded_png_path, "PNG")
    print("Saved:", rounded_png_path)
    
    rounded_1024 = make_rounded(squircle_crop, 1024)
    rounded_icns_path = os.path.join(icon_dir, "rounded_app_icon.icns")
    rounded_1024.save(rounded_icns_path, format="ICNS")
    print("Saved:", rounded_icns_path)
    
    # 1.3 ComposeResources drawables
    res_draw_dir = os.path.join(REPO_ROOT, "composeApp", "src", "commonMain", "composeResources", "drawable")
    os.makedirs(res_draw_dir, exist_ok=True)
    circle_512.save(os.path.join(res_draw_dir, "app_icon.png"), "PNG")
    circle_512.save(os.path.join(res_draw_dir, "circle_app_icon.png"), "PNG")
    print("Saved composeResources app_icon and circle_app_icon")
    
    # 1.4 AndroidApp drawables
    android_draw_dir = os.path.join(REPO_ROOT, "androidApp", "src", "main", "res", "drawable")
    os.makedirs(android_draw_dir, exist_ok=True)
    rounded_512.save(os.path.join(android_draw_dir, "app_icon.png"), "PNG")
    print("Saved androidApp app_icon.png")
    
    # 1.5 Android Mipmaps
    densities = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    for folder, size in densities.items():
        folder_path = os.path.join(REPO_ROOT, "androidApp", "src", "main", "res", folder)
        os.makedirs(folder_path, exist_ok=True)
        sq = make_rounded(squircle_crop, size, radius_ratio=0.18)
        circ = make_circle(squircle_crop, size)
        
        sq.save(os.path.join(folder_path, "ic_launcher.webp"), "WEBP")
        circ.save(os.path.join(folder_path, "ic_launcher_round.webp"), "WEBP")
        sq.save(os.path.join(folder_path, "ic_launcher_foreground.webp"), "WEBP")
        circ.save(os.path.join(folder_path, "ic_launcher_round_foreground.webp"), "WEBP")
    print("Generated all Android mipmaps")
    
    # 1.6 Colors & Adaptive Icon XML
    colors_xml_path = os.path.join(REPO_ROOT, "androidApp", "src", "main", "res", "values", "colors.xml")
    with open(colors_xml_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#F8F4F0</color>\n</resources>\n')
    print("Saved:", colors_xml_path)
    
    anydpi_dir = os.path.join(REPO_ROOT, "androidApp", "src", "main", "res", "mipmap-anydpi-v26")
    for xml_name in ["ic_launcher.xml", "ic_launcher_round.xml"]:
        xml_p = os.path.join(anydpi_dir, xml_name)
        if os.path.exists(xml_p):
            with open(xml_p, "r", encoding="utf-8") as f:
                c = f.read()
            c = re.sub(r'android:drawable="@android:color/\w+"', 'android:drawable="@color/ic_launcher_background"', c)
            with open(xml_p, "w", encoding="utf-8") as f:
                f.write(c)
    print("Updated adaptive-icon XMLs with @color/ic_launcher_background")
    
    # 1.7 Fastlane metadata images
    feature_w, feature_h = 1024, 500
    banner = Image.new("RGBA", (feature_w, feature_h), (248, 244, 240, 255))
    # Scale squircle to fit height 360 px
    target_h = 360
    target_w = 360
    logo_resized = rounded_512.resize((target_w, target_h), Image.Resampling.LANCZOS)
    banner.paste(logo_resized, ((feature_w - target_w) // 2, (feature_h - target_h) // 2), mask=logo_resized)
    
    for loc in ["en-US", "vi-VN"]:
        loc_dir = os.path.join(REPO_ROOT, "fastlane", "metadata", "android", loc, "images")
        os.makedirs(loc_dir, exist_ok=True)
        circle_512.save(os.path.join(loc_dir, "icon.png"), "PNG")
        banner.save(os.path.join(loc_dir, "featureGraphic.png"), "PNG")
    print("Saved fastlane icons and featureGraphics")
    
    # 1.8 Master logo in asset/
    asset_dir = os.path.join(REPO_ROOT, "asset")
    os.makedirs(asset_dir, exist_ok=True)
    src_raw.save(os.path.join(asset_dir, "logo.png"), "PNG")
    print("Saved master logo.png in asset/")

if __name__ == "__main__":
    generate_assets()
