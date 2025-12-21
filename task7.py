import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)

def greet(name: str) -> str:
    logger.info(f"Вызывается greet с именем: {name}")
    if not isinstance(name, str) or not name.strip():
        logger.warning("Получено пустое или некорректное имя")
        return "Привет, незнакомец!"
    result = f"Привет, {name}!"
    logger.debug(f"Сформирован результат: {result}")
    return result
