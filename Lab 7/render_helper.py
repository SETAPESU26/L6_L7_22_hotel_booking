import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal_screenshot(output_path, title, lines_with_colors, width=1100, font_size=15):
    """
    Renders a realistic dark-mode Windows Terminal window screenshot.
    lines_with_colors: list of (text, color_tuple)
    """
    font_path = "C:/Windows/Fonts/consola.ttf"
    title_font_path = "C:/Windows/Fonts/segoeui.ttf"
    if not os.path.exists(title_font_path):
        title_font_path = font_path

    font = ImageFont.truetype(font_path, font_size)
    title_font = ImageFont.truetype(title_font_path, 13)

    line_height = int(font_size * 1.45)
    header_height = 40
    padding_x = 24
    padding_y = 18

    content_height = len(lines_with_colors) * line_height
    height = header_height + padding_y * 2 + content_height

    # Terminal background (#0c0c0c)
    bg_color = (12, 12, 12)
    header_color = (31, 31, 31)
    border_color = (55, 55, 55)

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([0, 0, width, header_height], fill=header_color)
    draw.line([0, header_height, width, header_height], fill=border_color, width=1)

    # Window title
    draw.text((padding_x, 11), title, font=title_font, fill=(204, 204, 204))

    # Window control buttons (minimize, maximize, close)
    btn_w = 46
    btn_h = header_height
    # Close button (red hover-like)
    draw.text((width - 30, 11), "✕", font=title_font, fill=(160, 160, 160))
    # Maximize
    draw.text((width - 76, 10), "◻", font=title_font, fill=(160, 160, 160))
    # Minimize
    draw.text((width - 122, 10), "―", font=title_font, fill=(160, 160, 160))

    # Content lines
    y = header_height + padding_y
    for text, color in lines_with_colors:
        draw.text((padding_x, y), text, font=font, fill=color)
        y += line_height

    # Outer border
    draw.rectangle([0, 0, width - 1, height - 1], outline=border_color, width=1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved screenshot: {output_path}")

if __name__ == "__main__":
    print("Test render function ready.")
