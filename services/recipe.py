import grpc

from messages.recipe_pb2 import RecipeServicer
from messages.recipe_pb2 import RecipeResponse

RECIPE_LIST = [
    {"id": 0, "title": "Teste 1", "description": "Teste"}
]


def filter_recipe(id):
    return [recipe for recipe in RECIPE_LIST if recipe["id"] == id]


class RecipeService(RecipeServicer):

    def GetRecipe(self, request, context):
        if request.id:
            recipes = filter_recipe(request.id)
            if recipes:
                return RecipeResponse(title=recipes[0]["title"], description=recipes[0]["description"])
            msg = 'Recipe ID not found'
            context.set_details(msg)
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return RecipeResponse()
        msg = 'Must pass ID'
        context.set_details(msg)
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        return RecipeResponse()
