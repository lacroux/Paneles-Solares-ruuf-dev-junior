from typing import List, Dict
import json


def calculate_panels(panel_width: int, panel_height: int,roof_width: int, roof_height: int) -> int:

    """
    Calcular la máxima cantidad de paneles que caben en el techo.
    Permite rotación y combinaciones mixtas.
    """
    max_panels = 0

    # Caso 1: una sola orientación
    max_panels = max(
        max_panels,
        (roof_width // panel_width) * (roof_height // panel_height),
        (roof_width // panel_height) * (roof_height // panel_width)
    )

    # Caso 2: combinaciones mixtas
    for cols in range(roof_width // panel_width + 1):
        used_width = cols *  panel_width
        remaining_width = roof_width - used_width

        panels_1 = cols * (roof_height // panel_height)
        panels_2 = (remaining_width // panel_height) * (roof_height // panel_width)

        max_panels = max(max_panels, panels_1 + panels_2)

    for cols in range(roof_width // panel_height + 1):
        used_width = cols * panel_height
        remaining_width = roof_width - used_width

        panels_1 = cols * (roof_height // panel_width)
        panels_2 = (remaining_width // panel_width) * (roof_height // panel_height)

        max_panels = max(max_panels, panels_1 + panels_2)

    return max_panels

def run_tests() -> None:

    """
    Carga los casos de prueba desde test_cases.json
    y valida la función calculate_panels.
    """

    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]

    print("Corriendo tests:")
    print("-------------------")

    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"],
            test["panel_h"],
            test["roof_w"],
            test["roof_h"]
        )

        passed = result == test["expected"]

        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    run_tests()


if __name__ == "__main__":
    main()
