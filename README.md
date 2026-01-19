# GPT Model Analysis Streamlit App

A Streamlit application that displays a styled table analyzing GPT model strengths and limitations with interactive hover effects.

## Features

- Styled table with color-coded categories (green for "WHY IT WORKS", red for "LIMITATIONS")
- Interactive hover effects on table rows
- Clean, modern UI design

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd GPT-streamlit-app
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Local Development

Run the Streamlit app locally:

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`.

## Deployment

### Option 1: Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select your repository and branch
6. Set the main file path to `app.py`
7. Click "Deploy"

Your app will be live at `https://<your-app-name>.streamlit.app`

**Note**: Make sure your `.streamlit/config.toml` file is committed to the repository (it's already configured to disable telemetry).

### Option 2: Heroku

1. Install the Heroku CLI: [heroku.com](https://devcenter.heroku.com/articles/heroku-cli)

2. Create a `Procfile` in the root directory:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

3. Create a `setup.sh` file:
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

4. Login to Heroku and create an app:
```bash
heroku login
heroku create <your-app-name>
```

5. Deploy:
```bash
git push heroku main
```

### Option 3: Docker

1. Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. Build and run:
```bash
docker build -t GPT-streamlit-app .
docker run -p 8501:8501 GPT-streamlit-app
```

### Option 4: AWS EC2 / Other VPS

1. SSH into your server
2. Install Python 3.9+ and pip
3. Clone your repository
4. Install dependencies: `pip install -r requirements.txt`
5. Run with Streamlit: `streamlit run app.py --server.port=8501 --server.address=0.0.0.0`
6. Use a process manager like `systemd` or `supervisor` to keep it running
7. Optionally, use nginx as a reverse proxy

## Configuration

The app uses `.streamlit/config.toml` to disable telemetry. This file is already configured and committed to the repository.

## Project Structure

```
GPT-streamlit-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Requirements

- Python 3.8+
- Streamlit >= 1.28.0
- Pandas >= 2.0.0

## License

This project is open source and available under the MIT License.
