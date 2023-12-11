import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    # Testa se a classe pode ser instanciada corretamente
    lasanha = Dish("Lasanha", 25.0)
    assert lasanha.name == "Lasanha"
    assert lasanha.price == 25.0

    # Testa o método __repr__
    assert repr(lasanha) == "Dish('Lasanha', R$25.00)"

    # Testa o método __eq__
    lasanha2 = Dish("Lasanha", 25.0)
    assert lasanha == lasanha2

    # Testa o método __hash__
    assert hash(lasanha) == hash("Dish('Lasanha', R$25.00)")

    # Testa se dois pratos diferentes têm o mesmo hash (deve falhar)
    pizza = Dish("Pizza", 30.0)
    assert hash(lasanha) != hash(
        pizza
    ), "Dois pratos diferentes não devem ter o mesmo hash"

    # Testa a comparação de igualdade para dois pratos diferentes (deve falhar)
    assert (
        lasanha != pizza
    ), "A comparação de igualdade deve falhar para pratos diferentes"

    # Testa a adição de dependências de ingredientes
    queijo = Ingredient("queijo mussarela")
    lasanha.add_ingredient_dependency(queijo, 200)
    assert (
        queijo in lasanha.recipe
    ), "O ingrediente deve estar presente na receita"
    assert (
        lasanha.recipe[queijo] == 200
    ), "A quantidade de queijo mussarela deve ser 200"

    # Testa o método get_restrictions
    assert lasanha.get_restrictions() == queijo.restrictions

    # Testa o método get_ingredients
    assert lasanha.get_ingredients() == {queijo}

    # Testa a criação de pratos com valores inválidos (deve falhar)
    with pytest.raises(TypeError):
        Dish("Sopa", "dez")

    with pytest.raises(ValueError):
        Dish("Sopa", -10)

    # Testes esperados para falhar
    @pytest.mark.xfail(reason="Dois pratos iguais devem ter o mesmo hash")
    def test_hash_failure_for_equal_dishes():
        lasanha = Dish("Lasanha", 25.0)
        lasanha2 = Dish("Lasanha", 25.0)
        assert hash(lasanha) == hash(
            lasanha2
        ), "Dois pratos iguais devem ter hashes iguais"

    @pytest.mark.xfail(
        reason="Dois pratos diferentes não devem ter o mesmo hash"
    )
    def test_hash_failure_for_different_dishes():
        assert hash(lasanha) != hash(pizza)

    test_hash_failure_for_equal_dishes()
    test_hash_failure_for_different_dishes()
