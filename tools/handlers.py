class Handlers:
    def select(self, conector, model):
        return conector.execute(model.select().where(model.c.id == id)).first() == None
