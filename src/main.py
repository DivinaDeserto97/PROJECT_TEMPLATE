from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from tools.hello import say_hello


@dataclass
class AppConfig:
    app_env: str
    debug: bool
    server_ip: str
    server_port: int
    log_level: str
    loop_interval_seconds: int


def load_config() -> AppConfig:
    """Konfiguration aus .env laden und dev/start ableiten."""
    load_dotenv()

    app_env = os.getenv("APP_ENV", "dev").strip().lower()
    if app_env != "dev":
        app_env = "start"

    env_log_level = os.getenv("LOG_LEVEL", "").strip().upper()
    if env_log_level:
        log_level = env_log_level
    else:
        log_level = "DEBUG" if app_env == "dev" else "INFO"

    server_ip = os.getenv("SERVER_IP", "127.0.0.1")
    server_port = int(os.getenv("SERVER_PORT", "3000"))

    loop_interval_seconds = 2 if app_env == "dev" else 60

    return AppConfig(
        app_env=app_env,
        debug=app_env == "dev",
        server_ip=server_ip,
        server_port=server_port,
        log_level=log_level,
        loop_interval_seconds=loop_interval_seconds,
    )


def setup_logging(config: AppConfig) -> logging.Logger:
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_path = logs_dir / "app.log"

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    logging.basicConfig(level=getattr(logging, config.log_level, logging.INFO))
    logger = logging.getLogger("app")

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Logging initialisiert (Level=%s)", config.log_level)
    logger.info("Log-Datei: %s", log_path.resolve())
    return logger


def main() -> None:
    config = load_config()
    logger = setup_logging(config)

    text = say_hello("Projekt")
    print(text)

    print(f"Modus: {config.app_env}")
    print(f"Server: {config.server_ip}:{config.server_port}")
    print(f"Intervall: {config.loop_interval_seconds}s")

    logger.info("Anwendung gestartet (%s)", config.app_env)

    for i in range(3):
        logger.debug("Simulierter Tick %s", i)
        print(f"Tick {i}")

    logger.info("Programm sauber beendet.")


if __name__ == "__main__":
    main()
