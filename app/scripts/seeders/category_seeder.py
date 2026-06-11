from app.domain.entities.category import Category


def build_categories() -> list[Category]:
    return [
        Category(
            name="FILTERS",
            description="Oil, air, fuel, and cabin filters"
        ),
        Category(
            name="BRAKES",
            description="Brake pads, discs, drums, and brake components"
        ),
        Category(
            name="SUSPENSION",
            description="Shock absorbers, springs, and front suspension components"
        ),
        Category(
            name="STEERING",
            description="Steering components, tie rod ends, and ball joints"
        ),
        Category(
            name="ENGINE",
            description="Internal and external engine components"
        ),
        Category(
            name="ELECTRICAL",
            description="Electrical and ignition system components"
        ),
        Category(
            name="LUBRICANTS",
            description="Oils, greases, and fluids"
        ),
        Category(
            name="TRANSMISSION",
            description="Clutch, gearbox, and transmission components"
        ),
        Category(
            name="COOLING",
            description="Radiators, water pumps, and cooling system components"
        ),
        Category(
            name="EXHAUST",
            description="Exhaust systems, catalytic converters, and mufflers"
        ),
        Category(
            name="FUEL_SYSTEM",
            description="Fuel pumps, injectors, and fuel system components"
        ),
        Category(
            name="IGNITION",
            description="Spark plugs, ignition coils, and ignition system components"
        ),
        Category(
            name="BATTERIES",
            description="Batteries and battery accessories"
        ),
        Category(
            name="LIGHTING",
            description="Headlights, bulbs, and lighting system components"
        ),
        Category(
            name="AIR_CONDITIONING",
            description="Air conditioning and climate control components"
        ),
        Category(
            name="BODY_PARTS",
            description="Bumpers, fenders, and body components"
        ),
        Category(
            name="MIRRORS",
            description="Interior and exterior mirrors"
        ),
        Category(
            name="WIPERS",
            description="Wiper blades and windshield wiper system components"
        ),
        Category(
            name="WHEELS_AND_TIRES",
            description="Wheels, tires, and related accessories"
        ),
        Category(
            name="BEARINGS",
            description="Bearings and wheel bearings"
        ),
        Category(
            name="BELTS_AND_TENSIONERS",
            description="Belts, tensioners, and pulleys"
        ),
        Category(
            name="SENSORS",
            description="Engine, ABS, and electronic sensors"
        ),
        Category(
            name="TOOLS",
            description="Workshop tools and equipment"
        ),
        Category(
            name="ACCESSORIES",
            description="Vehicle accessories and add-ons"
        ),
    ]