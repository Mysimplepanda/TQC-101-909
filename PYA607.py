print("The 1st student:")
st_stu=[int(input()) for i in range(5)]
print("The 2nd student:")
nd_stu=[int(input()) for i in range(5)]
print("The 3rd student:")
rd_stu=[int(input()) for i in range(5)]


print("Student 1")
print(f"#Sum {sum(st_stu)}")
print(f"#Average {sum(st_stu)/5:.2f}")
print("Student 2")
print(f"#Sum {sum(nd_stu)}")
print(f"#Average {sum(nd_stu)/5:.2f}")
print("Student 3")
print(f"#Sum {sum(rd_stu)}")
print(f"#Average {sum(rd_stu)/5:.2f}")
