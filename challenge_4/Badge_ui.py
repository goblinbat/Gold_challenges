
import badge_repo

def main_menu():
    print('\n\nKomodo Security\n')
    usin = input('Select what you would like to do: \n'
                    '1) Add a Badge\n'
                    '2) Update a Badge\n'
                    '3) View All Badges\n'
                    '4) Exit\n'
                    '> ')
    print('\n\n')
    if usin == '1':
        doors = []
        badgeid = input('What is the badge id?: ')
        door1 = input('What is a door this badge can access?: ')
        doors.append(door1)
        while True:
            yn = input('Would you like to add another door? (y/n): ')
            if yn == 'y':
                andoor = input('What is another door this badge can access?: ')
                doors.append(andoor)
            elif yn == 'n':
                badge_repo.BadgeRepo.create_badge(badgeid, doors)
                break
            else:
                print('invalid input, try again')
        print('badge added')
    elif usin == '2':
        update_menu()
    elif usin == '3':
        print('Badge id \t\t\tDoor Access')
        for bag in badge_repo.badges:
            print(f'{bag.badgeid} \t\t\t\t{bag.doors}')
        ex = input('\n\npress any key to return to menu: ')
        if ex == True:
            main_menu()
    elif usin == '4':
        exit(0)
    else:
        print('invalid input')
        pass


def update_menu():
    upd8 = input('\nUpdate how?\n'
                        '1) Add Door Access\n'
                        '2) Remove Door Access\n'
                        '3) Delete Badge\n'
                        '4) Return to Main Menu\n'
                        '> ')
    if upd8 == '1':
        bagid = input('update door access of which badge? (enter id): ')
        found_match = False
        for b in badge_repo.badges:
            if bagid == b.badgeid:
                found_match = True
        if found_match == False:
            print('badge does not exist')
            update_menu()
        new_dor = input('add access to which door?: ')
        for b in badge_repo.badges:
            if bagid == b.badgeid:
                for door in b.doors:
                    if new_dor == door:
                        print('Badge already has access to that door')
                        break
                else:
                    badge_repo.BadgeRepo.add_door(bagid, new_dor)
                    print('updated!')
    elif upd8 == '2':
        try:
            bagid = input('update door access of which badge? (enter id): ')
        except Exception:
            print('badge does not exist')
        try:
            new_dor = input('remove access to which door?: ')
        except Exception:
            print(f'badge {bagid} does not have access to that door')
        badge_repo.BadgeRepo.delete_door(bagid, new_dor)
        print('deleted!')
    elif upd8 == '3':
        bagid = input('delete which badge?: ')
        badge_repo.BadgeRepo.delete_badge(bagid)
        print('deleted!')
    elif upd8 == '4':
        main_menu()
    else:
        print('invalid input')
        update_menu()
    main_menu()
        

if __name__=='__main__':
    while True:
        main_menu()

