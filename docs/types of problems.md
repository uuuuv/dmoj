CÁC LOẠI PROBLEM VÀ CÁCH CHẤM

# Problem format
- Test data của 1 problem được lưu trong folder có tên là code của problem đó.
- Folder này có: 
    - 1 file init.yml (bắt buộc)
    - file .zip chứa input, ouput data (tùy problem)
    - file .py, .cpp là các custom checker, grader, judge (tùy problem)

Ví dụ: problem "A Plus B" có code là "aplusb" sẽ có dạng:
aplusb
....|__init.yml
....|__aplusb.zip (không nhất thiết tên phải là aplusb)

- Mỗi khi file init.yml thay đổi nội dung, judge sẽ tự động cập nhật.

# Các cách tạo test data
1. Tạo bằng site interface
- Vào problem muốn cập nhật test data > "Edit test data".
https://docs.dmoj.ca/#/site/managing_problems?id=editing-test-data  
- Output limit length: độ dài stdout. Nếu bạn in ra stdout lớn quá giới hạn này sẽ bị lỗi OLE hoặc khoảng 256mb nếu không được specified. Ví dụ: output_limit_length = 3, thí sinh print(12) thì ok, print(123) thì lỗi OLE.
OLE: Output limit exceeded.
- Output prefix length: độ dài ouput của bạn sẽ được hiển thị. output_prefix_length = 3, thí sinh print(12345) thì khi submit xong, ouput của thí sinh sẽ hiện là '123'. (chỉ là về mặt hiển thị, không ảnh hưởng kết quả thí sinh).
## pretest (preliminary tests): 
pretest thường sẽ là: 
- test case mẫu được cho trong đề bài, 0 điểm.
- 