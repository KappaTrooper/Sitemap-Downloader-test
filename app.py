from flask import Flask, render_template, request, send_file
import requests
from bs4 import BeautifulSoup
import os
import zipfile
import io

app = Flask(__name__)

# Route for the home page (form to submit the sitemap URL)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission and download the pages as a ZIP file
@app.route('/download', methods=['POST'])
def download():
    sitemap_url = request.form['sitemap_url']

    # Destination folder (in-memory)
    destination_folder = 'downloaded_pages'
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Fetch the sitemap
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }
        response = requests.get(sitemap_url, headers=headers)

        if response.status_code != 200:
            return f"Failed to fetch sitemap: {sitemap_url}. Status code: {response.status_code}"

        # Parse the sitemap
        soup = BeautifulSoup(response.content, 'xml')
        urls = [loc.text for loc in soup.find_all('loc')]

        if not urls:
            return "No URLs found in the sitemap."

        # Download each page as an HTML file and save it in the destination folder
        for url in urls:
            try:
                page_response = requests.get(url, headers=headers)
                if page_response.status_code == 200:
                    # Create a folder for each URL
                    page_folder = os.path.join(destination_folder, url.split('/')[-2])
                    if not os.path.exists(page_folder):
                        os.makedirs(page_folder)
                    # Save the page as index.html
                    filename = os.path.join(page_folder, 'index.html')
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(page_response.text)
                else:
                    print(f"Failed to download {url}. Status code: {page_response.status_code}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")

        # Zip the folder and return it as a download
        zip_filename = "downloaded_pages.zip"
        zip_io = io.BytesIO()
        with zipfile.ZipFile(zip_io, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(destination_folder):
                for file in files:
                    zf.write(os.path.join(root, file), arcname=os.path.relpath(os.path.join(root, file), destination_folder))
        zip_io.seek(0)

        # Cleanup: remove downloaded files after zipping them
        for root, dirs, files in os.walk(destination_folder):
            for file in files:
                os.remove(os.path.join(root, file))
        for dir in os.listdir(destination_folder):
            os.rmdir(os.path.join(destination_folder, dir))
        os.rmdir(destination_folder)

        return send_file(zip_io, as_attachment=True, attachment_filename=zip_filename)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
