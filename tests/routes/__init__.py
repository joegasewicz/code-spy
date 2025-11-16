from bobtail import AbstractRoute, Request, Response


class HomeRoute(AbstractRoute):  # type: ignore[misc]
    def get(self, req: Request, res: Response) -> None:
        pass

    def post(self, req: Request, res: Response) -> None:
        pass

    def put(self, req: Request, res: Response) -> None:
        pass

    def delete(self, req: Request, res: Response) -> None:
        pass