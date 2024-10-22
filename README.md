# Sitemap Downloader

A Flask web application that allows users to download all pages listed in a sitemap as `index.html` files and package them into a ZIP file.

## Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure you have the following installed on your machine:

- **Python 3.x**
- **pip** (Python package manager)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/sitemap-downloader.git
   cd sitemap-downloader
   ```

2. **Install the required packages:**

   Run the following command to install all the necessary dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

   If the `requirements.txt` is missing or needs to be regenerated, you can manually install the packages by running:

   ```bash
   python3 -m pip install Flask requests beautifulsoup4 lxml gunicorn
   ```

   Then, to generate the `requirements.txt` file:

   ```bash
   pip freeze > requirements.txt
   ```

3. **Run the Flask app:**

   After installing the required packages, you can start the Flask app by running:

   ```bash
   python3 app.py
   ```

4. **Access the App:**

   Open your browser and navigate to `http://127.0.0.1:5000/` to use the Sitemap Downloader.

### How It Works

1. Enter a sitemap URL in the provided form.
2. Click the "Download" button.
3. The app will download all the pages listed in the sitemap, save them as `index.html`, and package them into a ZIP file for download.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can now save this text in a file called `README.md` in the root of your project folder and upload it to GitHub.

Let me know if you need more changes!