from ensta import Guest

guest = Guest()
profile = guest.profile("bajeintl")

if profile is None:
    print("Something went wrong.")
else:
    print(profile.biography)
    print(profile.follower_count)
    print(profile.following_count)
    print(profile.full_name)
    print(profile.profile_picture_url)
