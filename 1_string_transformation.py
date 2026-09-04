booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

fields = [field.strip() for field in booking.split("|")]
event_code, username, room, time_, email, vip_tags = fields

name = "_".join(word.capitalize() for word in username.split("_"))
room_upper = room.upper()
email_domain = email.split("@")[1].lower()
vip_count = vip_tags.count("VIP")

valid_event_code = event_code.startswith("EVT-") and event_code[4:].isdigit()
valid_username = "_" in username and all(ch.islower() or ch == "_" for ch in username)
valid_room = room[:-4].isalpha() and room[-4] == "-" and room[-3:].isdigit()
valid_time = (
    len(time_) == 5
    and time_[2] == ":"
    and time_[:2].isdigit()
    and time_[3:].isdigit()
    and 0 <= int(time_[:2]) <= 23
    and 0 <= int(time_[3:]) <= 59
)
valid_email = "@" in email and "." in email.split("@")[1]

print(f"Event code: {event_code}")
print(f"Name: {name}")
print(f"Room: {room_upper}")
print(f"Time: {time_}")
print(f"Email domain: {email_domain}")
print(f"VIP tag count: {vip_count}")
print(f"Valid event code: {valid_event_code}")
print(f"Valid username: {valid_username}")
print(f"Valid room: {valid_room}")
print(f"Valid time: {valid_time}")
print(f"Valid email: {valid_email}")

######### EXPECTED OUTPUT #########
""" Event code: EVT-2026
Name: Alice_Wong
Room: ROOM-305
Time: 14:30
Email domain: unimail.edu
VIP tag count: 2
Valid event code: True
Valid username: True
Valid room: True
Valid time: True
Valid email: True """

