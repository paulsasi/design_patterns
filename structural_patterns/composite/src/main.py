import army

if __name__ == "__main__":
    soldier_1 = army.Soldier(name="Paul1", age=1)
    soldier_2 = army.Soldier(name="Paul2", age=1)
    soldier_3 = army.Soldier(name="Paul3", age=1)
    batallion_1 = army.Batallion((soldier_1, soldier_2, soldier_3))

    soldier_4 = army.Soldier(name="Isma1", age=2)
    soldier_5 = army.Soldier(name="Isma2", age=2)
    batallion_2 = army.Batallion((soldier_4, soldier_5))

    soldier_6 = army.Soldier(name="Mario1", age=5)
    batallion_3 = army.Batallion((batallion_2, soldier_6))

    batallion_4 = army.Batallion((batallion_1, batallion_3))


    print(f"Army age: {batallion_4.get_age()}")
    print("Send attack order")
    batallion_4.attack()