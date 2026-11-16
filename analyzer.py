# MAKEUP PRODUCT PROFIT ANALYZER
# Name: Furaha Simone Akinyi
# Admission Number: 24zad109524
# Project: Makeup Product Profit Analyzer
# Method Family: Rules
# Intended Users: Small makeup businesses and sellers
def makeup_profit(buying_price, quantity, shipping, selling_price):
    """Calculate profit after including shipping."""
    total_cost = (buying_price * quantity) + shipping
    revenue = selling_price * quantity
    return revenue - total_cost


def naive_profit(buying_price, quantity, shipping, selling_price):
    """Baseline: deliberately ignores shipping."""
    return (selling_price - buying_price) * quantity


def money_label(amount):
    """Rule-based classification using IF-THEN rules."""
    if amount > 0:
        return "profit"
    elif amount < 0:
        return "loss"
    else:
        return "even"


# 1. MAKEUP PRODUCT CATALOGUE
# Each product has five input values.


MAKEUP_CASES = [
    ("blush", 500, 10, 1120, 1300),
    ("bronzer", 700, 10, 1120, 1500),
    ("concealer", 600, 10, 1200, 1200),
    ("lipgloss", 350, 10, 900, 750),
    ("foundation", 850, 10, 1300, 1500),
    ("setting powder", 450, 10, 1000, 900),
    ("mascara", 400, 10, 1100, 850),
    ("lip liner", 250, 10, 800, 550),
    ("highlighter", 600, 10, 1000, 1100),
    ("beauty blender", 200, 10, 800, 450),
]

# 2. ORIGINAL CATALOGUE COMPARISON


def loss_called_profit(cases, profit_fn):
    mistakes = 0

    print(f"{'Product':<20} {'Full':>8} {'Method':>8}  Labels")

    for name, buying_price, quantity, shipping, selling_price in cases:

        full = makeup_profit(
            buying_price, quantity, shipping, selling_price
        )

        got = profit_fn(
            buying_price, quantity, shipping, selling_price
        )

        full_label = money_label(full)
        got_label = money_label(got)

        slip = full_label == "loss" and got_label == "profit"
        mistakes += int(slip)

        print(
            f"{name:<20} {full:8.0f} {got:8.0f} "
            f"{full_label} vs {got_label}"
            + ("  SLIP" if slip else "")
        )

    print(f"Losses labelled profit: {mistakes} of {len(cases)}")
    return mistakes


# 3. TWENTY TEST CASES WITH EXPECTED ANSWERS
# Format:
# product, buying price, quantity, shipping,
# selling price, expected profit, expected label


TEST_CASES = [
    ("blush", 500, 10, 1120, 1300, 6880, "profit"),
    ("blush", 500, 10, 1500, 600, -500, "loss"),

    ("bronzer", 700, 10, 1120, 1500, 6880, "profit"),
    ("bronzer", 700, 10, 2000, 900, 0, "even"),

    ("concealer", 600, 10, 1200, 1200, 4800, "profit"),
    ("concealer", 600, 10, 2500, 800, -500, "loss"),

    ("lipgloss", 350, 10, 900, 750, 3100, "profit"),
    ("lipgloss", 350, 10, 2000, 500, -500, "loss"),

    ("foundation", 850, 10, 1300, 1500, 5200, "profit"),
    ("foundation", 850, 10, 2000, 1000, -500, "loss"),

    ("setting powder", 450, 10, 1000, 900, 3500, "profit"),
    ("setting powder", 450, 10, 3000, 700, -500, "loss"),

    ("mascara", 400, 10, 1100, 850, 3400, "profit"),
    ("mascara", 400, 10, 2000, 600, 0, "even"),

    ("lip liner", 250, 10, 800, 550, 2200, "profit"),
    ("lip liner", 250, 10, 1500, 400, 0, "even"),

    ("highlighter", 600, 10, 1000, 1100, 4000, "profit"),
    ("highlighter", 600, 10, 2000, 550, -2500, "loss"),

    ("beauty blender", 200, 10, 800, 450, 1700, "profit"),
    ("beauty blender", 200, 10, 1000, 150, -1500, "loss"),
]

# 4. EVALUATE THE AGENT AND BASELINE


def evaluate_agent(cases, profit_fn):

    correct_calculations = 0
    correct_classifications = 0
    false_positives = 0

    print("\nProduct              Expected   Actual   Expected label   Actual label")

    for name, buying, quantity, shipping, selling, expected_profit, expected_label in cases:

        actual_profit = profit_fn(buying, quantity, shipping, selling)
        actual_label = money_label(actual_profit)

        calculation_correct = actual_profit == expected_profit
        classification_correct = actual_label == expected_label

        if calculation_correct:
            correct_calculations += 1

        if classification_correct:
            correct_classifications += 1

        if expected_label == "loss" and actual_label == "profit":
            false_positives += 1

        print(
            f"{name:<20} {expected_profit:>8.0f} "
            f"{actual_profit:>8.0f} "
            f"{expected_label:<16} {actual_label}"
        )

    total = len(cases)

    calculation_accuracy = correct_calculations / total * 100
    classification_accuracy = correct_classifications / total * 100

    print("\nPERFORMANCE MEASURES")
    print(f"Calculation accuracy: {correct_calculations}/{total} ({calculation_accuracy:.1f}%)")
    print(f"Classification accuracy: {correct_classifications}/{total} ({classification_accuracy:.1f}%)")
    print(f"False positives: {false_positives}")
    
    return false_positives


# 5. RUN THE PROJECT

print("MAKEUP PRODUCT PROFIT ANALYZER")

print("\nFULL CALCULATION - CATALOGUE")
loss_called_profit(MAKEUP_CASES, makeup_profit)

print("\nNAIVE BASELINE - CATALOGUE")
loss_called_profit(MAKEUP_CASES, naive_profit)

print("\nRULE-BASED AGENT - 20 TEST CASES")
agent_mistakes = evaluate_agent(TEST_CASES, makeup_profit)

print("\nNAIVE BASELINE - 20 TEST CASES")
baseline_mistakes = evaluate_agent(TEST_CASES, naive_profit)

print("\nFINAL EVALUATION")
print("Target: 20/20 correct calculations and at least 19/20 correct classifications.")
print(f"Agent false positives: {agent_mistakes}")
print(f"Baseline false positives: {baseline_mistakes}")
