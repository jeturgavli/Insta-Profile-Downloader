import instaloader 

Instagram_Profile_Download = instaloader.Instaloader()

account = input('Enter the Instagram Account Username: ')

Instagram_Profile_Download.download_profile(account, profile_pic_only = True)