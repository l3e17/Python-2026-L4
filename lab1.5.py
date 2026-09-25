color_list = ["Blue", "Orange","Green", "Red","Black"]

fav_color = input("What is your favorite color?:").title()#title returns a string where the FIRST character will be uppercase RED-->Red
if fav_color in color_list:
    vi_tri = color_list.index(fav_color)#color list use index to find the index of the fav color input
    print(f"Your colod is at index {vi_tri} in my list")
else:
    print(f"Cannot find your color")