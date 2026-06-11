from domain.entities.brand import Brand


def build_brands() -> list[Brand]:
    return [
        Brand(
            name="BOSCH",
            active=True,
            nationality="Germany",
        ),
        Brand(
            name="MAHLE",
            active=True,
            nationality="Germany",
        ),
        Brand(
            name="MANN-FILTER",
            active=True,
            nationality="Germany",
        ),
        Brand(
            name="SACHS",
            active=True,
            nationality="Germany",
        ),
        Brand(
            name="VALEO",
            active=True,
            nationality="France",
        ),
        Brand(
            name="SKF",
            active=True,
            nationality="Sweden",
        ),
        Brand(
            name="TRW",
            active=True,
            nationality="United States",
        ),
        Brand(
            name="ACDELCO",
            active=True,
            nationality="United States",
        ),
        Brand(
            name="MONROE",
            active=True,
            nationality="United States",
        ),
        Brand(
            name="NGK",
            active=True,
            nationality="Japan",
        ),
        Brand(
            name="DENSO",
            active=True,
            nationality="Japan",
        ),
        Brand(
            name="AISIN",
            active=True,
            nationality="Japan",
        ),
        Brand(
            name="KYB",
            active=True,
            nationality="Japan",
        ),
        Brand(
            name="NISSIN",
            active=True,
            nationality="Japan",
        ),
        Brand(
            name="BRIDGESTONE",
            active=True,
            nationality="Japan",
        ),
        Brand(
            name="MICHELIN",
            active=True,
            nationality="France",
        ),
        Brand(
            name="BREMBO",
            active=True,
            nationality="Italy",
        ),
        Brand(
            name="FEBI BILSTEIN",
            active=True,
            nationality="Germany",
        ),
        Brand(
            name="DELPHI",
            active=True,
            nationality="United Kingdom",
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
        Brand(
            name="GOODYEAR",
            active=True,
            nationality="United States",
        ),
    ]