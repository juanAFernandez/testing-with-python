from behave import given, when, then


@given('un vendedor que vende {unidades}')
def step_ventas_del_vendedor(context, unidades):
    context.vendedor_ventas = unidades


@when('supera las 1000')
def step_calculo_porcentaje(context):
    assert calcula_plus(context.vendedor_ventas) == context.vendedor_ventas


@when('no supera las 1000')
def step_calculo_porcentaje(context):
    assert calcula_plus(int(context.vendedor_ventas)) == 0


@then('el vendedor deberia tener un plus de  {euros}')
def step_el_vendedor_deberia(context, euros):
    assert context.failed is False


def calcula_plus(ventas):
    if ventas > 1000:
        return ventas
    else:
        return 0