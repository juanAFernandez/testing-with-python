Feature: Cálculo del incentivo salarial.

    Para calcular la cuantía del bono salarial,
    como administrador
    quiero que a cada vendedor se le aplique su bono
    en base a las ventas mensuales.

    Scenario: Vendedor supera las 1000 unidades
        Given un vendedor que vende 5000
        When supera las 1000
        Then el vendedor deberia tener un plus de  5000

    Scenario: Vendedor no supera las 1000 unidades
        Given un vendedor que vende 360
        When no supera las 1000
        Then el vendedor deberia tener un plus de  0