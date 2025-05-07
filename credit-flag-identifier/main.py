import re

def get_card_flag(card_number: str) -> str:
    """Identifica a bandeira de um cartão com base no número usando regex."""

    # Remove espaços e hifens
    card_number = re.sub(r"[ \-]", "", card_number)

    patterns = {
        "Visa Electron": r"^(4026|417500|4844|4913|4917)\d{10}$",
        "Visa": r"^4\d{12,18}$",
        "Mastercard": r"^(5[1-5]\d{14}|222[1-9]\d{12}|22[3-9]\d{13}|2[3-6]\d{14}|27[01]\d{13}|2720\d{12})$",
        "American Express": r"^3[47]\d{13}$",
        "Elo": r"^(401178|431274|5067\d{2}|627780|636297)\d{10}$",
        "Diners Club": r"^(30[0-5]|36|38|39)\d{11,13}$",
        "Discover": r"^(6011\d{12}|65\d{14}|64[4-9]\d{13}|622(12[6-9]|1[3-9]\d|[2-8]\d{2}|9[01]\d|92[0-5])\d{10})$",
        "Hipercard": r"^(38|60)\d{14}$",
        "JCB": r"^35(2[89]|[3-8][0-9])\d{12}$",
        "Aura": r"^50\d{14}$",
        "UnionPay": r"^62\d{14,17}$",
        "Maestro": r"^(5[06-9]|6[0-9])\d{10,17}$",
        "Cabal": r"^(58|60)\d{12,17}$",
        "Verve": r"^(5060(9[9]|[0-8]\d)|5079(6[0-4]|[0-5]\d)|6500(2[0-7]|[0-1]\d))\d{10,13}$",
        "InstaPayment": r"^63[7-9]\d{13}$",
        "InterPayment": r"^636\d{13}$",
        "Laser": r"^(6304|6706|6771|6709)\d{12,15}$",
        "Switch": r"^(4903|4905|4911|4936|564182|633110|6333|6759)\d{10,15}$",
        "Solo": r"^(6334|6767)\d{12,15}$",
        "UATP": r"^1\d{14}$",
        "RuPay": r"^(60|6521|6522)\d{12,15}$",
        "Troy": r"^9792\d{12}$",
        "Mir": r"^220[0-4]\d{12,15}$"
    }

    for brand, pattern in patterns.items():
        if re.match(pattern, card_number):
            return brand

    return "Bandeira não identificada"

# Exemplo de uso:
if __name__ == "__main__":
    number = input("Digite o número do cartão: ")
    print("Bandeira:", get_card_flag(number))
