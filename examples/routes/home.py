from bobtail import AbstractRoute, Request, Response


class HomeRoute(AbstractRoute):  # type: ignore[misc]
    def get(self, req: Request, res: Response) -> None:
        res.set_body({"title": "Welcome to my sit!"})

    def post(self, req: Request, res: Response) -> int:
        pass

    def put(self, req: Request, res: Response) -> None:
        pass

    def delete(self, req: Request, res: Response) -> None:
        pass
