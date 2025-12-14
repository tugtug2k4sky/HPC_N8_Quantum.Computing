# Tạo thư mục outputs nếu chưa tồn tại
import logging
import os
import time

os.makedirs("outputs", exist_ok=True)

# Tạo filename với định dạng ngày tháng
filename = f"outputs/logs_{time.strftime('%y-%m-%d_%H-%M-%S', time.localtime())}.log"

# Thiết lập logging
logging.basicConfig(
    filename=filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="w",
)

logger = logging.getLogger()

class Logger:
    @staticmethod
    def log(message):
        logger.info(message)