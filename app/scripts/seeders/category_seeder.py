from app.domain.entities.category import Category


def build_categories() -> list[Category]:
    return [
        Category(
            name="FILTERS",
            description="Filtros de aceite, aire, combustible y habitáculo"
        ),
        Category(
            name="BRAKES",
            description="Pastillas, discos, campanas y componentes de freno"
        ),
        Category(
            name="SUSPENSION",
            description="Amortiguadores, espirales y tren delantero"
        ),
        Category(
            name="STEERING",
            description="Dirección, terminales y rótulas"
        ),
        Category(
            name="ENGINE",
            description="Componentes internos y externos del motor"
        ),
        Category(
            name="ELECTRICAL",
            description="Sistema eléctrico y encendido"
        ),
        Category(
            name="LUBRICANTS",
            description="Aceites, grasas y fluidos"
        ),
        Category(
            name="TRANSMISSION",
            description="Embrague, caja de cambios y transmisión"
        ),
        Category(
            name="COOLING",
            description="Radiadores, bombas de agua y refrigeración"
        ),
        Category(
            name="EXHAUST",
            description="Escape, catalizadores y silenciadores"
        ),
        Category(
            name="FUEL_SYSTEM",
            description="Bombas, inyectores y componentes de combustible"
        ),
        Category(
            name="IGNITION",
            description="Bujías, bobinas y sistema de encendido"
        ),
        Category(
            name="BATTERIES",
            description="Baterías y accesorios"
        ),
        Category(
            name="LIGHTING",
            description="Faros, lámparas y sistema de iluminación"
        ),
        Category(
            name="AIR_CONDITIONING",
            description="Aire acondicionado y climatización"
        ),
        Category(
            name="BODY_PARTS",
            description="Paragolpes, guardabarros y carrocería"
        ),
        Category(
            name="MIRRORS",
            description="Espejos interiores y exteriores"
        ),
        Category(
            name="WIPERS",
            description="Escobillas y sistema limpiaparabrisas"
        ),
        Category(
            name="WHEELS_AND_TIRES",
            description="Llantas, neumáticos y accesorios"
        ),
        Category(
            name="BEARINGS",
            description="Rulemanes y rodamientos"
        ),
        Category(
            name="BELTS_AND_TENSIONERS",
            description="Correas, tensores y poleas"
        ),
        Category(
            name="SENSORS",
            description="Sensores de motor, ABS y electrónica"
        ),
        Category(
            name="TOOLS",
            description="Herramientas y accesorios para taller"
        ),
        Category(
            name="ACCESSORIES",
            description="Accesorios y complementos para vehículos"
        ),
    ]