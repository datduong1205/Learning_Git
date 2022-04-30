'''             Phần 1              '''

dic1 = {
    "Name" : "Duong Le Minh Dat",
    "Member" : 69,
}

print(dic1)
print(type(dic1))

dic2 = {
    key: value for key, value in [("name", "Tao Nguyen Bao Tran"), ("member", 96)]
}

print(dic2)
print(type(dic2))

dic3 = dict()
print(dic3)
print(type(dic3))

print(dic1["Name"])
print(dic1.get("Luv", "Tao Nguyen Bao Tran"))

dic4 = dict(SpaceX = "Elon Musk", Facebook = "Mark Zuckerberg")
print(dic4)


iter_ = ("Name1", "Number", 12, True)
dic5 = dict.fromkeys(iter_, "TranTao")
print(dic5)
print(dic5["Name1"])
print(dic5[True])


dic5["Number"] = 21
print(dic5["Number"])

# Nếu gán vào 1 key không có sẵn trong dict, key sẽ được tự động thêm vào dict
dic5["Love"] = "Forever"
print(dic5["Love"])
print(dic5)

dic6 = dict(T= 21, D= 12, W= "Lover")
print(dic6)

dic6["T"] = dic6["T"] + 1
dic6["W"] = dic6["W"] + " Forever"
print(dic6)

'''             Phần 2              '''

d = {"Team":"Dat", (1,2):69, "Hello":"BaoTranYeuDau"}
print(d)


# .copy: tạo ra 1 vùng nhớ mới để d2 trỏ vào, không trùng với d
d2 = d.copy()
print(d2)

# .clear: xóa hết dữ liệu
d2.clear()
print(d2)

# .get: lấy ra value từ dictionary theo key
value = d.get("Team")
print(value)

value2 = d.get((1,2))
print(value2)

# nếu nhập key không có, sẽ tự lấy giá trị default
value3 = d.get("none", "Tran")
print(value3)

# .items: trả ra 1 tuples với giá trị đầu là KEY, sau là VALUE
value4 = list(d.items())
print(value4[0])

# .keys: lấy ra danh sách KEY thuộc dictionary
value5 = d.keys()
print(value5)

# .values: lấy ra danh sách VALUE thuộc dictionary
value6 = d.values()
print(value6)

# .pop: lấy KEY ra khỏi dict
value7 = d.pop("Team", "Tran")
print(value7)
print(d)

# .popitem: nếu không truyền dữ liệu, sẽ pop ngẫu nhiên
value8 = d.popitem()
print(value8) 
print(d)

# .setdefault: trả về VALUE của KEY trong dict
value9 = d.setdefault((1,2))
print(value9)
print(d)

# nếu KEY chưa tồn tại, sẽ tự động thêm vào dict
value10 = d.setdefault("WhatsUpGuys", "Eyyo")
print(value10)
print(d)

# .update: add thêm KEY vào DIC nếu KEY chưa tồn tại
# còn có tác dụng chỉnh sửa VALUE 
value11 = d.update(Team="Azota")
print(value11)
print(d)


