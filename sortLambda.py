

spells = [#(ability, damage, mana)
            ("Fireball", 50, 40),
            ("Ice Shard", 30, 25),
            ("Lightning", 70, 50),
            ("Wind Slash", 20, 10),
            ("Dark Nova", 55, 50)
            ]

def dmg_per_mana(s):
    return s[1]/s[2]

efficient_spells = sorted(
    spells,
    key=lambda s: s[1]/s[2],
    reverse=True
)

for s in efficient_spells:
    print(f'{s[0]}: {s[1]/s[2]}')

print(efficient_spells)