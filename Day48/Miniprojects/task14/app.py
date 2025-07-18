from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/gallery')
def gallery():
    image_folder = os.path.join(app.static_folder, 'images/gallery')
    images = os.listdir(image_folder)
    image_urls = ['images/gallery/' + img for img in images if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('gallery.html', photos=image_urls)

if __name__ == '__main__':
    app.run(debug=True)
