from app import app, db
from models import Hero, Power, HeroPower

def seed_heroes(heroes_data):
    print(":female_superhero: Seeding heroes...")
    for hero_data in heroes_data:
        hero = Hero(**hero_data)
        db.session.add(hero)
        db.session.commit()
    print("Hero seeding completed.")

def seed_powers(powers_data):
    print(":female_superhero: Seeding powers...")
    for power_data in powers_data:
        power = Power(**power_data)
        db.session.add(power)
    db.session.commit()
    print("Power seeding completed.")

def seed_hero_powers(hero_power_data ):
    print(":female_superhero: Seeding hero_powers...")
    for hero_power_data in heroes_power_data:
        hero_power_data = HeroPower(**hero_power_data)
        db.session.add(hero_power_data)
        db.session.commit()
        print("HeroPower seeding completed.")

if __name__ == '__main__':
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Peter Parker", "super_name": "Spider-Man"},
        {"name": "Tony Stark", "super_name": "Iron Man"},
        {"name": "Bruce Wayne", "super_name": "Batman"},
        {"name": "Diana Prince", "super_name": "Wonder Woman"},
        {"name": "Clark Kent", "super_name": "Superman"},
        {"name": "Natasha Romanoff", "super_name": "Black Widow"},
        {"name": "Steve Rogers", "super_name": "Captain America"},
        # Add more hero data here
    ]

    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
        {"name": "telekinesis", "description": "can move or manipulate objects with the mind"},
        {"name": "invisibility", "description": "renders the wielder unseen by the naked eye"},
        {"name": "teleportation", "description": "allows the wielder to instantly transport from one location to another"},
        {"name": "mind control", "description": "exerts control over the thoughts and actions of others"},
        {"name": "shape-shifting", "description": "can alter the physical form or appearance"},
        {"name": "telepathy", "description": "can read minds and communicate mentally with others"},
        # Add more power data here
    ]

    heroes_power_data = [
        {'strength': 'Average', 'hero_id': 1, 'power_id': 1},
        {'strength': 'Strong', 'hero_id': 2, 'power_id': 2},
        {'strength': 'Weak', 'hero_id': 3, 'power_id': 3},
        {'strength': 'Average', 'hero_id': 1, 'power_id': 4},
        {'strength': 'Strong', 'hero_id': 2, 'power_id': 5},
        {'strength': 'Weak', 'hero_id': 3, 'power_id': 6},
        {'strength': 'Average', 'hero_id': 4, 'power_id': 1},
        {'strength': 'Strong', 'hero_id': 5, 'power_id': 2},
        {'strength': 'Weak', 'hero_id': 6, 'power_id': 3},
        {'strength': 'Average', 'hero_id': 7, 'power_id': 4},
        {'strength': 'Strong', 'hero_id': 8, 'power_id': 5},
        {'strength': 'Weak', 'hero_id': 9, 'power_id': 6},
        {'strength': 'Average', 'hero_id': 10, 'power_id': 7},
        {'strength': 'Strong', 'hero_id': 1, 'power_id': 8},
        {'strength': 'Weak', 'hero_id': 2, 'power_id': 9},
        # Add more hero power data here
    ]

    with app.app_context():
        seed_heroes(heroes_data)
        seed_powers(powers_data)
        seed_hero_powers(heroes_power_data)
