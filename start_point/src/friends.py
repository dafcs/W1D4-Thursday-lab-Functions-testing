#1
def get_name(person):
    return person["name"]

#2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

#3
def likes_to_eat(person,food):
    ite_li = person["favourites"]["snacks"]
    for snack in ite_li:
        if snack == food:
            return True
    else:
        return False
    
#4
def add_friend(person,friend):
    fre_li = person["friends"]
    fre_li.append(friend)
    return len(fre_li)

#5
def remove_friend(person,friend):
    fre_li = person["friends"]
    fre_li.remove(friend)
    return len(fre_li)

#6
def total_money(peoplelist):
    total_monies = 0
    for i in peoplelist:
        total_monies += i["monies"]
    return total_monies

#7
def lend_money(person1,person2,val):
    person1["monies"] = person1["monies"] - val
    person2["monies"] = person2["monies"] + val

#8
def all_favourite_foods(givenlist):
    made_list = []
    for l in givenlist:
        for snack in l["favourites"]["snacks"]:
            made_list.append(snack)
    return made_list

#9
def find_no_friends(peoplelist):
    no_friend = []
    for people in peoplelist:
        if len(people["friends"]) == 0:
            no_friend.append(people)
    return no_friend

#10
def unique_favourite_tv_shows(peoplelist):
    fav_shows = []
    for people in peoplelist:
        if not people["favourites"]["tv_show"] in fav_shows:
            fav_shows.append(people["favourites"]["tv_show"])
    return fav_shows

