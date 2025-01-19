import os
import random
from faker import Faker
from file_operations import render_template


STYLE_MAP = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
}


SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]


OUTPUT_DIR = "characters"


def stylize_skills(skills, style_map):
    runic_skills = []
    for skill in skills:
        runic_skill = ""
        for char in skill:
            runic_skill += style_map.get(char, char)
        runic_skills.append(runic_skill)
    return runic_skills


def generate_character(fake, runic_skills, character_number):
    first_name = fake.first_name()
    last_name = fake.last_name()
    chosen_skills = random.sample(runic_skills, 3)

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "job": fake.job(),
        "town": fake.city(),
        "strength": fake.random_int(min=3, max=18),
        "agility": fake.random_int(min=3, max=18),
        "endurance": fake.random_int(min=3, max=18),
        "intelligence": fake.random_int(min=3, max=18),
        "luck": fake.random_int(min=3, max=18),
        "skill_1": chosen_skills[0],
        "skill_2": chosen_skills[1],
        "skill_3": chosen_skills[2],
    }

    output_path = os.path.join(
        OUTPUT_DIR,
        "character_{}.svg".format(character_number),
    )
    return context, output_path


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fake = Faker("ru_RU")
    runic_skills = stylize_skills(SKILLS, STYLE_MAP)

    for i in range(1, 11):
        context, output_path = generate_character(fake, runic_skills, i)
        render_template("charsheet.svg", output_path, context)


if __name__ == "__main__":
    main()
