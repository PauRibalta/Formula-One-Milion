from src.models.circuit import Circuit

monza = Circuit(
    "Monza",
    0.40, 0.60, 0.80,
    1.00, 0.90,
    0.60,
    0.80, 0.50,
    0.70, 0.40,
    0.70,
    0.90,
    0.15,
    0.25,
    0.85,
    0.30
)

monaco = Circuit(
    "Monaco",
    1.00, 0.40, 0.20,
    0.20, 0.60,
    0.80,
    0.40, 0.30,
    0.75, 1.00,
    0.40,
    0.10,
    0.20,
    0.18,
    1.00,
    0.70
)

silverstone = Circuit(
    "Silverstone",
    0.50, 0.90, 1.00,
    0.80, 0.85,
    0.70,
    0.70, 0.60,
    0.95, 0.90,
    0.80,
    0.60,
    0.35,
    0.22,
    0.75,
    0.55
)
circuits = [
    monza,
    monaco,
    silverstone
]