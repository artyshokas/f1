from sqlalchemy.orm import sessionmaker
from f1_model import engine, Team, Driver, Part


session = sessionmaker(bind=engine)()


while True:
    choice = int(input("1 - Enter Data \n 2 - View Data \n 3 - Delete Data \n 4 - EXIT \n"))
    if choice == 1:
        entry = int(input("1 - Enter Team \n 2 - Enter Part \n 3 - Enter Driver \n 4 - MENU \n"))
        if entry == 1:
            team_name = input("Enter Team name: ")
            origin = input("Enter Team country: ")
            team = Team(team_name=team_name, origin=origin)
            session.add(team)
            session.commit()
        if entry == 2:
            part_name = input("Part Name: ")
            manufacturer = input("Manufacturer: ")
            teams = session.query(Team).all()
            for team in teams:
                print(team)
            team_id = int(input("Enter Team ID: "))
            part = Part(part_name=part_name, manufacturer=manufacturer, team_id=team_id)
            session.add(part)
            session.commit()
        if entry == 3:
            driver_name = input("Name: ")
            driver_surname = input("Surname: ")
            teams = session.query(Team).all()
            for team in teams:
                print(team)
            team_id = int(input("Enter Team ID: "))
            driver = Driver(driver_name=driver_name, driver_surname=driver_surname, team_id=team_id)
            session.add(driver)
            session.commit()
        if entry == 4:
            choice = int(input("1 - Enter Data \n 2 - View Data \n 3 - Delete Data \n 4 - EXIT \n"))
    if choice == 2:
        view = int(input("1 - View Team \n 2 - View Driver \n 3 - View Parts \n 4 - MENU \n"))
        if view == 1:
            teams = session.query(Team).all()
            for team in teams:
                print(team)
        if view == 2:
            drivers = session.query(Driver).all()
            for driver in drivers:
                print(driver)
        if view == 3:
            parts = session.query(Part).all()
            for part in parts:
                print(part)
        if view == 4:
            choice = int(input("1 - Enter Data \n 2 - View Data \n 3 - Delete Data \n 4 - EXIT \n"))
    if choice == 3:
        delete = int(input("1 - Delete Team \n 2 - Delete Driver \n 3 - Delete Part \n 4 - EXIT \n"))
        if delete == 1:
            teams = session.query(Team).all()
            for team in teams:
                print(team)
            deleting = int(input("Team ID to Delete: "))
            session.query(Team).filter(Team.id == deleting).delete()
            session.commit() 
        if delete == 2:
            drivers = session.query(Driver).all()
            for driver in drivers:
                print(driver)
            deleted = int(input("Driver ID to Delete: "))
            session.query(Driver).filter(Driver.id == deleting).delete()
            session.commit()
        if delete == 3:
            parts = session.query(Part).all()
            for part in parts:
                print(part)
            deleting = int(input("Part ID to Delete: "))
            session.query(Part).filter(Part.id == deleting).delete()
            session.commit()
            print(f"Part {deleting} successfully deleted ")
        if delete == 4:
            choice = int(input("1 - Enter Data \n 2 - View Data \n 3 - Delete Data \n 4 - EXIT \n"))
    if choice == 4:
        print("QUIT")
        break
