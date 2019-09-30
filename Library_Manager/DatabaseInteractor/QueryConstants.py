class queries:
    insert_into_student = "INSERT INTO STUDENT_1 (student_name, roll_no, gender, department, mobile, regdate, books_issued, BID_str, current_fine, paid_fine) VALUES('%s', %s, '%s','%s', %s, %s, 0, '', 0, 0);"
    insert_into_library = "INSERT INTO BOOK_1 (title, author, type, department, regdate, SID, TID, vend_time) VALUES('%s','%s','%s','%s', %s, NULL, NULL, NULL);"

    issue_from_library = "INSERT INTO ISSUE_1 (SID, BID, out_book_tally, T_time) VALUES(%s, %s, %s, %s);"
    last_issue = "SELECT * FROM issue_1 where TID=(select max(TID) from issue_1);"

    update_issued_student = "UPDATE STUDENT_1 SET books_issued = %s, BID_str = '%s' WHERE SID = %s;"
    update_issued_student2 = "UPDATE STUDENT_1 SET books_issued = %s, BID_str = '%s', current_fine = %s WHERE SID = %s;"
    update_fine_student = "UPDATE STUDENT_1 SET paid_fine = %s WHERE SID = %s;"
    update_issued_book = "UPDATE BOOK_1 SET SID = %s, vend_time = %s, TID = %s WHERE BID = %s;"

    get_recent_SID = "SELECT SID FROM student_1 where SID=(select max(SID) from student_1);"
    get_recent_BID = "SELECT BID FROM book_1 where BID=(select max(BID) from book_1);"
    get_recent_out_book_tally = "SELECT * FROM issue_1 where TID=(select max(TID) from issue_1);"

    get_details_SID = "select * from student_1 where SID = %s;"
    get_details_BID = "select * from book_1 where BID = %s;"

    delete_book = "UPDATE BOOK_1 SET type = 'd' WHERE BID = %s;"
    delete_student = "UPDATE STUDENT_1 SET regdate = 0 WHERE SID = %s;"

    active_SID = "SELECT SID FROM student_1 WHERE regdate IN(0);"
    active_BID_d = "SELECT BID FROM book_1 WHERE type IN('d');"
    active_BID_r = "SELECT BID FROM book_1 WHERE type IN('r');"

    create_default_bd = "CREATE DATABASE LibrarySystem;"
    use_default_db = "USE LibrarySystem;"
    create_default_tables_1 = "create table student_1 ( SID int auto_increment, student_name varchar(100) not null, roll_no bigint not null, gender varchar(1) not null, department varchar(3) not null, mobile bigint not null,regdate int not null, books_issued int not null, BID_str varchar(200) not null, current_fine int not null, paid_fine int not null, primary key(SID));"
    create_default_tables_2 = "create table book_1 (BID bigint auto_increment, title varchar(100) not null, author varchar(100) not null, type varchar(1) not null, department varchar(3) not null, regdate int not null, SID int,TID bigint, vend_time int, foreign key(SID) references student_1(SID), primary key(BID));"
    create_default_tables_3 = "create table issue_1 (SID int not null, BID bigint not null, TID bigint auto_increment, out_book_tally int not null, T_time int not null, primary key(TID), foreign key(SID) references student_1(SID), foreign key(BID) references book_1(BID));"