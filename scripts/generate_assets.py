"""
Asset and Icon Generation Script for Dmusic
Processes source image (logo Dmusic) to generate all required application icons,
mipmaps, banners, and cleans up legacy assets.
"""

import os
import sys
from PIL import Image, ImageDraw

SOURCE_IMAGE_PATH = r"C:\Users\Mrs Thao\.gemini\antigravity\brain\7095ec88-2b67-4dc1-b884-15ca2b4ce729\.user_uploaded\media_1794720486874_ef283b1c.jpg"
REPO_ROOT = r"C:\Users\Mrs Thao\.gemini\antigravity\scratch\Dmusic"


def make_circle_icon(img: Image.Image, size: int, padding_ratio: float = 0.03125) -> Image.Image:
    """Create a circular masked icon with high-quality antialiasing."""
    # Resize source image to target size
    resized = img.convert("RGBA").resize((size, size), Image.Resampling.LANCZOS)
    
    # Render antialiased mask at 4x resolution
    supersample = 4
    mask_size = size * supersample
    pad = int(mask_size * padding_ratio)
    
    mask = Image.new("L", (mask_size, mask_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((pad, pad, mask_size - pad - 1, mask_size - pad - 1), fill=255)
    mask = mask.resize((size, size), Image.Resampling.LANCZOS)
    
    # Apply alpha mask
    output = resized.copy()
    output.putalpha(mask)
    return output


def make_rounded_icon(img: Image.Image, size: int, padding_ratio: float = 0.035, radius_ratio: float = 0.22) -> Image.Image:
    """Create a rounded rectangle (squircle) icon with high-quality antialiasing for macOS."""
    resized = img.convert("RGBA").resize((size, size), Image.Resampling.LANCZOS)
    
    supersample = 4
    mask_size = size * supersample
    pad = int(mask_size * padding_ratio)
    radius = int(mask_size * radius_ratio)
    
    mask = Image.new("L", (mask_size, mask_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle(
        (pad, pad, mask_size - pad - 1, mask_size - pad - 1),
        radius=radius,
        fill=255
    )
    mask = mask.resize((size, size), Image.Resampling.LANCZOS)
    
    output = resized.copy()
    output.putalpha(mask)
    return output


def make_square_icon(img: Image.Image, size: int) -> Image.Image:
    """Create a square icon."""
    return img.convert("RGBA").resize((size, size), Image.Resampling.LANCZOS)


def make_feature_graphic(img: Image.Image, width: int = 1024, height: int = 500) -> Image.Image:
    """
    Create a 1024x500 banner with Dmusic logo centered on solid black background.
    """
    banner = Image.new("RGBA", (width, height), (0, 0, 0, 255))
    
    # Logo non-black bounding box in 1024x1024 is (211, 263, 792, 751)
    # Crop the logo area
    logo_crop = img.convert("RGBA").crop((211, 263, 792, 751))
    crop_w, crop_h = logo_crop.size
    
    # Scale logo to fit nicely in 500 height (e.g. height 360 px)
    target_h = 360
    target_w = int(crop_w * (target_h / crop_h))
    logo_resized = logo_crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Center on banner
    paste_x = (width - target_w) // 2
    paste_y = (height - target_h) // 2
    banner.paste(logo_resized, (paste_x, paste_y), mask=logo_resized)
    return banner


def main():
    if not os.path.exists(SOURCE_IMAGE_PATH):
        print(f"ERROR: Source image not found at {SOURCE_IMAGE_PATH}")
        sys.exit(1)
        
    print(f"Loading source image: {SOURCE_IMAGE_PATH}")
    src_img = Image.open(SOURCE_IMAGE_PATH)
    print(f"Source size: {src_img.size}, mode: {src_img.mode}")
    
    # Ensure directories exist
    os.makedirs(os.path.join(REPO_ROOT, "composeApp", "icon"), exist_ok=True)
    os.makedirs(os.path.join(REPO_ROOT, "composeApp", "src", "commonMain", "composeResources", "drawable"), exist_ok=True)
    os.makedirs(os.path.join(REPO_ROOT, "androidApp", "src", "main", "res", "drawable"), exist_ok=True)
    os.makedirs(os.path.join(REPO_ROOT, "asset"), exist_ok=True)
    
    # ----------------------------------------------------
    # 1. ComposeApp icons
    # ----------------------------------------------------
    print("\n--- Generating ComposeApp icons ---")
    circle_512 = make_circle_icon(src_img, 512)
    circle_png_path = os.path.join(REPO_ROOT, "composeApp", "icon", "circle_app_icon.png")
    circle_512.save(circle_png_path, "PNG")
    print(f"Saved: {circle_png_path} ({circle_512.size})")
    
    # Windows ICO containing 16, 24, 32, 48, 64, 128, 256
    ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ico_path = os.path.join(REPO_ROOT, "composeApp", "icon", "circle_app_icon.ico")
    circle_512.save(ico_path, format="ICO", sizes=ico_sizes)
    print(f"Saved: {ico_path} (sizes: {ico_sizes})")
    
    # macOS circle ICNS (1024x1024 master for crisp macOS retina rendering)
    circle_1024 = make_circle_icon(src_img, 1024)
    circle_icns_path = os.path.join(REPO_ROOT, "composeApp", "icon", "circle_app_icon.icns")
    circle_1024.save(circle_icns_path, format="ICNS")
    print(f"Saved: {circle_icns_path}")
    
    # Rounded icon (512x512)
    rounded_512 = make_rounded_icon(src_img, 512)
    rounded_png_path = os.path.join(REPO_ROOT, "composeApp", "icon", "rounded_app_icon.png")
    rounded_512.save(rounded_png_path, "PNG")
    print(f"Saved: {rounded_png_path} ({rounded_512.size})")
    
    # macOS rounded ICNS
    rounded_1024 = make_rounded_icon(src_img, 1024)
    rounded_icns_path = os.path.join(REPO_ROOT, "composeApp", "icon", "rounded_app_icon.icns")
    rounded_1024.save(rounded_icns_path, format="ICNS")
    print(f"Saved: {rounded_icns_path}")
    
    # ----------------------------------------------------
    # 2. ComposeResources drawables
    # ----------------------------------------------------
    print("\n--- Generating ComposeResources drawables ---")
    app_icon_res_path = os.path.join(
        REPO_ROOT, "composeApp", "src", "commonMain", "composeResources", "drawable", "app_icon.png"
    )
    circle_512.save(app_icon_res_path, "PNG")
    print(f"Saved: {app_icon_res_path} ({circle_512.size})")
    
    circle_res_path = os.path.join(
        REPO_ROOT, "composeApp", "src", "commonMain", "composeResources", "drawable", "circle_app_icon.png"
    )
    circle_512.save(circle_res_path, "PNG")
    print(f"Saved: {circle_res_path} ({circle_512.size})")
    
    # ----------------------------------------------------
    # 3. AndroidApp drawables
    # ----------------------------------------------------
    print("\n--- Generating AndroidApp drawables ---")
    android_app_icon_path = os.path.join(
        REPO_ROOT, "androidApp", "src", "main", "res", "drawable", "app_icon.png"
    )
    square_512 = make_square_icon(src_img, 512)
    square_512.save(android_app_icon_path, "PNG")
    print(f"Saved: {android_app_icon_path} ({square_512.size})")
    
    # ----------------------------------------------------
    # 4. Android Mipmaps (WebP)
    # ----------------------------------------------------
    print("\n--- Generating Android mipmaps ---")
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
        
        sq = make_square_icon(src_img, size)
        circ = make_circle_icon(src_img, size, padding_ratio=0.03)
        
        # ic_launcher.webp
        p_launcher = os.path.join(folder_path, "ic_launcher.webp")
        sq.save(p_launcher, "WEBP")
        
        # ic_launcher_round.webp
        p_launcher_round = os.path.join(folder_path, "ic_launcher_round.webp")
        circ.save(p_launcher_round, "WEBP")
        
        # ic_launcher_foreground.webp
        p_foreground = os.path.join(folder_path, "ic_launcher_foreground.webp")
        sq.save(p_foreground, "WEBP")
        
        # ic_launcher_round_foreground.webp
        p_round_foreground = os.path.join(folder_path, "ic_launcher_round_foreground.webp")
        circ.save(p_round_foreground, "WEBP")
        
        print(f"Generated {folder}: size={size}x{size} (launcher, round, foreground, round_foreground)")
        
    # ----------------------------------------------------
    # 5. Fastlane metadata images
    # ----------------------------------------------------
    print("\n--- Generating Fastlane metadata images ---")
    fastlane_locales = ["en-US", "vi-VN"]
    fastlane_icon_512 = make_circle_icon(src_img, 512)
    feature_graphic = make_feature_graphic(src_img, 1024, 500)
    
    for loc in fastlane_locales:
        loc_dir = os.path.join(REPO_ROOT, "fastlane", "metadata", "android", loc, "images")
        os.makedirs(loc_dir, exist_ok=True)
        
        f_icon_path = os.path.join(loc_dir, "icon.png")
        fastlane_icon_512.save(f_icon_path, "PNG")
        print(f"Saved: {f_icon_path} ({fastlane_icon_512.size})")
        
        f_banner_path = os.path.join(loc_dir, "featureGraphic.png")
        feature_graphic.save(f_banner_path, "PNG")
        print(f"Saved: {f_banner_path} ({feature_graphic.size})")
        
    # ----------------------------------------------------
    # 6. Cleanup legacy assets & copy logo.png
    # ----------------------------------------------------
    print("\n--- Cleaning up legacy assets & copying logo.png ---")
    files_to_remove = [
        os.path.join(REPO_ROOT, "asset", "52770992.jpg"),
        os.path.join(REPO_ROOT, "asset", "dependencies_graph.svg"),
        os.path.join(REPO_ROOT, "asset", "sentry.svg"),
    ]
    for p in files_to_remove:
        if os.path.exists(p):
            os.remove(p)
            print(f"Deleted legacy asset: {p}")
        else:
            print(f"Legacy asset already removed: {p}")
            
    # Copy source image to asset/logo.png (1024x1024 PNG)
    logo_png_path = os.path.join(REPO_ROOT, "asset", "logo.png")
    src_img.convert("RGBA").save(logo_png_path, "PNG")
    print(f"Saved master logo: {logo_png_path} ({src_img.size})")
    
    # ----------------------------------------------------
    # 7. Update adaptive-icon background in anydpi-v26 to black
    # ----------------------------------------------------
    print("\n--- Updating adaptive icon XML background ---")
    anydpi_dir = os.path.join(REPO_ROOT, "androidApp", "src", "main", "res", "mipmap-anydpi-v26")
    for xml_name in ["ic_launcher.xml", "ic_launcher_round.xml"]:
        xml_path = os.path.join(anydpi_dir, xml_name)
        if os.path.exists(xml_path):
            with open(xml_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = content.replace("@android:color/white", "@android:color/black")
            if new_content != content:
                with open(xml_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {xml_path}: replaced @android:color/white with @android:color/black")
            else:
                print(f"{xml_path} already has correct background color.")
                
    print("\n=== ALL ASSETS SUCCESSFULLY GENERATED AND REPLACED! ===")


if __name__ == "__main__":
    main()
