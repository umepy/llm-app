# mount GCS Fuse
gcsfuse llm-app /app/data

# Run streamlit
poetry run streamlit run app.py --server.port 8080 
