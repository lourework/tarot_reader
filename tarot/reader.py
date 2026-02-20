import random
from .api import get_random_cards
from .custom_meanings import CUSTOM_MEANINGS


class TarotReader:

    def daily_card(self):
        cards = get_random_cards(1)
        if not cards:
            return

        card = cards[0]
        custom = self.get_custom_meaning(card["name"])

        result = {
            "type": "Daily Card",
            "name": card['name'],
            "api_meaning": card["meaning_up"],
            "description": card['desc']
        }

        if custom: 
            result["movie_or_tvshow"] = custom["movie_or_tvshow"]
            result["description_show"] = custom["description_show"]
            result["general_advice"] = custom["general_advice"]

        return result

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
        custom = self.get_custom_reading(card["name"])
        orientation = random.choice(["upright", "reversed"])

        answer = "Yes" if orientation == "upright" else "No"

        result = {
            "name": card["name"],
            "orientation": orientation,
            "answer": answer,
            "api_meaning": card["meaning_up"]
        }

        if custom:
            result.update({
                "movie_or_tvshow": custom["movie_or_tvshow"],
                "description_show": custom["description_show"],
                "general_advice": custom["general_advice"]
            })

        return result
    
    def get_custom_meaning(self, card_name):
        return CUSTOM_MEANINGS.get(card_name, None)
