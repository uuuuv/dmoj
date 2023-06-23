# Edit test data cho problem

Có 2 cách:
- Bằng site interface
- Tạo bằng tay

## Tạo bằng site interface
https://docs.dmoj.ca/#/site/managing_problems?id=editing-test-data  

Ý nghĩa các fields: 

- Output limit length: độ dài stdout. Nếu thí in ra stdout lớn quá giới hạn này sẽ bị lỗi OLE hoặc khoảng 256mb nếu không được specified. Ví dụ: output_limit_length = 3, thí sinh print(12) thì ok, print(123) thì lỗi OLE (3 ký tự trở lên).

OLE: Output limit exceeded.

- Output prefix length: độ dài ouput của thí sinh sẽ được hiển thị. output_prefix_length = 3, thí sinh print(12345) thì khi submit xong, ouput của thí sinh sẽ hiện là '123'. (chỉ là về mặt hiển thị, không ảnh hưởng kết quả thí sinh).

2 trường trên giúp hạn chế những trường hợp ouput tốn bộ nhớ. VD: 
```python
while True: 
    print('aaaaaaaa')
```

### Tạo standard test data
[standard test data](./images/standard.jpg)
Sau khi nhấn submit, site sẽ:
- Tạo folder có tên là code của problem trong DMOJ_PROBLEM_DATA_ROOT
- Upload file zip vào trong folder này
- Tạo file init.yml theo những gì ta đã nhập.

Sau khi tạo xong, judge sẽ cập nhật data này để chấm điểm.
Phần site sẽ có thông tin các test cases của problem để hiển thị.

### Tạo batched test data
[Batched test data](./images/batched-cases.jpg)

### Tạo generators test data
[Generator test data 1](./images/generator-1.jpg)
[Generator test data 2](./images/generator-2.jpg)
Generator arguments là mảng chứa các tham số sẽ được convert thành Python str.

## Tạo bằng tay
- Tạo bằng tay tức là:
    - Tự tạo folder có tên là code của problem muốn tạo.
    - Tự copy file zip nếu có vào
    - Tự viết file init.yml

- Trường hợp dùng custom judge cần tạo bằng tay, vì site interface không có mục nào để nhập custom judge cả.
- Judge có watchdog dùng để theo dõi sự thay đổi trong DMOJ_PROBLEM_DATA_ROOT, nên khi có thay đổi, judge sẽ cập nhật.
- Tạo bằng tay thì site sẽ không nhận biết được điều này do site không có cơ chế trên.
- Do đó tạo bằng tay sẽ không hiển thị trước được có bao nhiêu test cases, input và expected ouput data là gì. Nhưng vẫn submit và chấm điểm bình thường.
- Mình đã làm chức năng "Update test data (beta)" để dùng cho trường hợp này. Khi tạo bằng tay xong, click vào nút này thì site sẽ lưu data vào, như vậy sẽ có data hiển thị trước.

Ví dụ trường hợp này là 1 problem sử dụng custom judge: 
```yml
custom_judge: seed2.py
unbuffered: true
archive: seed2.zip
pretest_test_cases:
- {in: seed2.1.in, points: 20}
- {in: seed2.2.in, points: 20}
- {in: seed2.3.in, points: 20}
- {in: seed2.4.in, points: 20}
- {in: seed2.5.in, points: 20}
```
- problem trên có 5 test cases, có input data, không có expected output data, có điểm.
- Tạo bằng tay sẽ không hiển thị được thông tin trên cho thí sinh. 
- Chỉ cần click "Update test data (beta)" là xong.

