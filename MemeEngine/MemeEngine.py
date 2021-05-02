"""Meme Generator."""
import os
from PIL import Image, ImageDraw, ImageFont

class MemeEngine:
    """Combine texts and pictures to make a meme."""
    
    def __init__(self, output_dir):
        """Save and create the output directory path."""
        self.output_dir = output_dir
        self.count = 1
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    
    def make_meme(self, img_path, text, author, width=500) -> str: #generated image path
        """Put text on top of the image."""
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f"tmp-{self.count}.jpg")
        self.count += 1
        if width:
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)
        
        width, height = img.size
        text = text.upper()
        author = author.upper()

        if text and author:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./_data/Fonts/impact.ttf', size=30)
            w_t, h_t = draw.textsize(text, font=font)
            w_b, h_b = draw.textsize(author, font=font)
            draw.text(((width-w_t)/2, (height-h_t)*0.1), text, font=font, fill='white')
            draw.text(((width-w_b)/2, (height-h_b)*0.9), author, font=font, fill='white')

        img.save(outfile, "JPEG")
        return outfile
