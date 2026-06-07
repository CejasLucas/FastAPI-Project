from domain.entities.brand import Brand


def build_brands() -> list[Brand]:
    return [
        Brand(
            name="BOSCH",
            active=True,
            nationality="Alemania",
        ),
        Brand(
            name="MAHLE",
            active=True,
            nationality="Alemania",
        ),
        Brand(
            name="MANN-FILTER",
            active=True,
            nationality="Alemania",
        ),
        Brand(
            name="SACHS",
            active=True,
            nationality="Alemania",
        ),
        Brand(
            name="VALEO",
            active=True,
            nationality="Francia",
        ),
        Brand(
            name="SKF",
            active=True,
            nationality="Suecia",
        ),
        Brand(
            name="TRW",
            active=True,
            nationality="Estados Unidos",
        ),
        Brand(
            name="ACDELCO",
            active=True,
            nationality="Estados Unidos",
        ),
        Brand(
            name="MONROE",
            active=True,
            nationality="Estados Unidos",
        ),
        Brand(
            name="NGK",
            active=True,
            nationality="Japón",
        ),
        Brand(
            name="DENSO",
            active=True,
            nationality="Japón",
        ),
        Brand(
            name="AISIN",
            active=True,
            nationality="Japón",
        ),
        Brand(
            name="KYB",
            active=True,
            nationality="Japón",
        ),
        Brand(
            name="NISSIN",
            active=True,
            nationality="Japón",
        ),
        Brand(
            name="BREMBO",
            active=True,
            nationality="Italia",
        ),
        Brand(
            name="FEBI BILSTEIN",
            active=True,
            nationality="Alemania",
        ),
        Brand(
            name="DELPHI",
            active=True,
            nationality="Reino Unido",
        ),
        Brand(
            name="TIGGO PARTS",
            active=True,
            nationality="China",
        ),
        Brand(
            name="GREAT WALL PARTS",
            active=True,
            nationality="China",
        ),
        Brand(
            name="BYD AUTO PARTS",
            active=True,
            nationality="China",
        ),
    ]