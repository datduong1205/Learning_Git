'''Viết chương trình nhập vào từ file input một câu chào hỏi làm quen với độ dài bất kỳ, mỗi từ nằm trên một dòng.
 Xuất ra file output câu chào hỏi vừa nhận được trên 1 dòng duy nhất, các từ cách nhau 1 khoảng trắng. (có xử lý ngoại lệ) '''

try:
    with open("sayhi.inp", mode="r", encoding="utf8") as file_inp:
        storeInput = file_inp.read()
        print(storeInput)

        Splitstore = storeInput.splitlines()
        print(Splitstore)

        result = " ".join(Splitstore)
        print(result)

        SplitSpace = result.split()
        print(SplitSpace)

        Finalresult = " ".join(SplitSpace)
        print(Finalresult)

    with open("sayhi.out", mode="wb") as file_out:
        file_out.write(Finalresult.encode("utf8"))

    print("Done!")

except FileNotFoundError:
    print("File Not Found")
    
    with open("sayhi.out", mode="w") as FileNotFound:
        FileNotFound.write("File Not Found")



