from uvicorn import Config, Server

from resources.settings import settings


def main() -> None:
    server = Server(
        Config(
            "src.entrypoints.fastapi.application:get_app",
            workers=settings.WORKERS,
            host=settings.HOST,
            port=settings.PORT,
            reload=settings.RELOAD,
            factory=True,
        ),
    )
    server.run()


if __name__ == "__main__":
    main()
