# INSTALLATION

1. Bản này dùng với judge docker. Hiện đang chạy trên nhánh `feature/fe-user-problem`.
2. Làm theo hướng dẫn https://docs.dmoj.ca/#/judge/setting_up_a_judge, các bước cần lưu ý:

- Thay `git clone https://github.com/DMOJ/site.git` bằng clone bản này về: `git clone https://github.com/uuuuv/dmoj.git`.
- Đổi tên thư mục dmoj > site cho đồng bộ với hướng dẫn: `mv dmoj site`
- `cd site`
- KHÔNG `git checkout v4.0.0`.
- Thay vào đó checkout nhánh đang làm `git switch feature/fe-user-problem` (nhánh `main` chưa có gì)
- Đổi `python3 manage.py loaddata language_small` thành `python3 manage.py loaddata language_all` để cài đặt tất cả các ngôn ngữ lập trình. Nếu chọn small thì chỉ có khoảng 20 ngôn ngữ.
- Do đã có sẵn file cấu hình, nên khi chạy test 'runserver', 'celery', 'bridged' có thể bị lỗi thiếu dependencies. Cuối trang có 2 dependencies, ta cài trước luôn. Bạn cũng có thể xóa các file cấu hình rồi tạo lại theo hướng dẫn.
  `npm install qu ws simplesets`
  `pip3 install websocket-client`
- Các bước còn lại làm tương tự, sửa lại cấu hình cho phù hợp.
- Copy thư mục `funix/static/funix` vào thư mục `STATIC_ROOT` trong `local_settings.py`.
- Cấc trúc thư mục hiện tại của bản này tương ứng với file cấu hình: \\r\\n
  /projects \\r\\n
  |\_\_\_\_\_foj \\r\\n
  ............|\_\_\_\_\_site \\r\\n
  ............|\_\_\_\_\_venv \\r\\n
  ............|\_\_\_\_\_static \\r\\n
  ............|\_\_\_\_\_tmp \\r\\n
  ............|\_\_\_\_\_problems \\r\\n
  ............|\_\_\_\_\_cache \\r\\n

# SỦ DỤNG

1. Vào danh sách problems: domain/problems/
2. Chọn problem: domain/problem/<problem_code>
3. Click 'Submit solution'. Sẽ vào trang đề bài và code.

- Chưa đăng nhập thì ở phần editor sẽ hiển thị yêu cầu đăng nhập.
- Nếu chưa submit lần nào thì sẽ chỉ hiển thị nút `submit`.
- Nếu đã submit trước đó thì editor sẽ load code của lần mới nhất, và hiển thị nút `resubmit` thay vì `submit`.

4. Nếu muốn đến 1 submission cũ (không phải mới nhất) thì tới route:  
   domain/problem/<problem_code>/resubmit/<submission_id>
   Để đến được route này:

- Vào danh sách submission của bạn.
- Chọn xem kết quả 1 submission bằng click `view`.
- Tại trang submission status vừa được chuyển tới, click `resubmit`. Xong.

# Hardware requirements

From @Xyene:

1. You'll need more hosts for a contest where correct solutions can take several minutes to judge (e.g. IOI (The International Olympiad of Informatics) - style hundreds of test cases).
2. What DMOJ is doing:

- they run dmoj on a baremental host for most of the year:
  6-core (12-thread) AMD Ryzen 5 3600X @ 3.8GHz, with 16 GB 3200 MHz CL16 dual-channel RAM.
- Each judgeruns in a QEMU instance allocated 2GB RAM and 1 physical core (2 threads).
- When they need to run a contest that requireds more judges, they have some scripts to spin some up in the cloud.
- The cloud judges just mount all problem data over NFS (Network File System).
- So, just mount the NFS volume, start docker, and the judge connects.
- If you're planning on running a contest, one thing to keep in mind is that the most load you'll face be at the start of the contest, as everyone rushes to hit the "Join contest" button at the same time. That'll be frontend load more than it will be database load. ton at the same time. That'll be frontend load more than it will be database load. The frontend can render ~ 4 requests/second/core (conservatively, but you should lower bound it at 100ms/req). You can tell how long things take on your setup by reading uwsgi logs.
