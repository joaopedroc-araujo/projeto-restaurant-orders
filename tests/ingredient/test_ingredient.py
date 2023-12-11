from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Testa se a classe pode ser instanciada corretamente
    queijo = Ingredient("queijo mussarela")
    assert queijo.name == "queijo mussarela"
    assert queijo.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    # Testa o método __repr__
    assert repr(queijo) == "Ingredient('queijo mussarela')"

    # Testa o método __eq__
    queijo2 = Ingredient("queijo mussarela")
    assert queijo == queijo2

    # Testa o método __hash__
    assert hash(queijo) == hash("queijo mussarela")

    # Testa se os dois ingredientes iguais têm o mesmo hash
    queijo3 = Ingredient("queijo mussarela")
    assert hash(queijo) == hash(
        queijo3
    ), "Dois ingredientes iguais devem ter o mesmo hash"

    # Testa se dois ingredientes diferentes têm o mesmo hash (deve falhar)
    bacon = Ingredient("bacon")
    assert hash(queijo) != hash(
        bacon
    ), "Dois ingredientes diferentes não devem ter o mesmo hash"

    # Testa a comparação de igualdade para dois ingredientes
    # diferentes (deve falhar)
    assert (
        queijo != bacon
    ), "A comparação de igualdade deve falhar para ingredientes diferentes"
