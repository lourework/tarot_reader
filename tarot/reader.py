import random
from .api import get_random_cards

class TarotReader:

    def daily_card(self):
        cards = get_random_cards(1)
        if not cards:
            return

        card = cards[0]

        return {
            "type": "Daily Card",
            "name": card['name'],
            "meaning": card["meaning_up"],
            "description": card['desc']
        }

    def past_present_future(self):
        cards = get_random_cards(3)
        if not cards:
            return

        positions = ["Past", "Present", "Future"]
        spread = []

        for i in range(3):
            spread.append({
                "position": positions[i],
                "name": cards[i]["name"],
                "meaning": cards[i]["meaning_up"]
            })
        
        return spread

    def yes_or_no(self):
        cards = get_random_cards(1)
        if not cards:
            return

        card = cards[0]
        orientation = random.choice(["upright", "reversed"])

        answer = "Yes" if orientation == "upright" else "No"
        meaning = card["meaning_up"] if orientation == "upright" else card["meaning_rev"]

        return {
            "name": card["name"],
            "orientation": orientation,
            "answer": answer,
            "meaning": meaning
        }