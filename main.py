from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
import uvicorn

app = FastAPI()

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"

schema = strawberry.Schema(query=Query)
graphql_router = GraphQLRouter(schema)

app.include_router(graphql_router, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)