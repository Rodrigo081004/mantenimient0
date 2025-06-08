import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Código que puede fallar
except Exception as e:
    logging.error(f"Error crítico: {str(e)}")