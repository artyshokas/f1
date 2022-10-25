from sqlalchemy.orm import sessionmaker
from f1_model import engine, Team, Driver, Part
from pprint import pprint


session = sessionmaker(bind=engine)()


while True:
    try:
        choice = int(input("1 - Enter Data \n2 - View Data \n3 - Delete Data \n4 - EXIT \n"))
        if choice == 1:
            entry = int(input("1 - Enter Team \n2 - Enter Part \n3 - Enter Driver \n4 - MENU \n"))
            if entry == 1:
                team_name = input("Enter Team name: ")
                origin = input("Enter Team country: ")
                team = Team(team_name=team_name, origin=origin)
                session.add(team)
                session.commit()
                print(f"Team {team} added")
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
                print(f"Part {part} added")
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
                print(f"Driver {driver} added")
            if entry == 4:
                choice = int(input("1 - Enter Data \n2 - View Data \n3 - Delete Data \n4 - EXIT \n"))
        if choice == 2:
            view = int(input("1 - View Team \n2 - View Driver \n3 - View Parts \n4 - MENU \n"))
            if view == 1:
                teams = session.query(Team).all()
                for team in teams:
                    print(team)
                team_id = int(input("Enter Team ID: "))
                if team_id:
                    team = session.query(Team).get(team_id)
                    print(team)
            if view == 2:
                drivers = session.query(Driver).all()
                for driver in drivers:
                    print(driver)
                driver_id = int(input("Enter Driver ID for details: "))
                if driver_id:
                    driver = session.query(Driver).get(driver_id)
                    row_select = session.query(Driver) \
                     .with_entities(Driver.team_id) \
                         .filter(Driver.id == driver_id).all()
                    for row in row_select:
                        team_id = row.team_id
                    team = session.query(Team).get(team_id)
                    print(driver, team)
            if view == 3:
                parts = session.query(Part).all()
                for part in parts:
                    print(part)
                part_id = int(input("Enter Part ID for details: "))
                if part_id:
                    part = session.query(Part).get(part_id)
                    row_select = session.query(Part) \
                        .with_entities(Part.team_id) \
                            .filter(Part.id == part_id).all()
                    for row in row_select:
                        team_id = row.team_id
                    team = session.query(Team).get(team_id)
                    print(part, team)
            if view == 4:
                choice = int(input("1 - Enter Data \n2 - View Data \n3 - Delete Data \n4 - EXIT \n"))
        if choice == 3:
            delete = int(input("1 - Delete Team \n2 - Delete Driver \n3 - Delete Part \n4 - EXIT \n"))
            if delete == 1:
                teams = session.query(Team).all()
                for team in teams:
                    print(team)
                deleting = int(input("Team ID to Delete: "))
                session.query(Team).filter(Team.id == deleting).delete()
                session.commit()
                print(f"Team {deleting} successfully deleted ")
            if delete == 2:
                drivers = session.query(Driver).all()
                for driver in drivers:
                    print(driver)
                deleting = int(input("Driver ID to Delete: "))
                session.query(Driver).filter(Driver.id == deleting).delete()
                session.commit()
                print(f"Driver {deleting} successfully deleted ")
            if delete == 3:
                parts = session.query(Part).all()
                for part in parts:
                    print(part)
                deleting = int(input("Part ID to Delete: "))
                session.query(Part).filter(Part.id == deleting).delete()
                session.commit()
                print(f"Part {deleting} successfully deleted ")
            if delete == 4:
                choice = int(input("1 - Enter Data \n2 - View Data \n3 - Delete Data \n4 - EXIT \n"))
        if choice == 4:
            print("QUIT")
            break
    except ValueError:
        print("Error: Please choose from Option list")
