# 数据库操作
	# 数据库查看
		> show databases;
	# 创建数据库
		> create database if not exists db_name;
		> create database charset=utf8;
	# 查看数据库的创建语句
		> show create database db_name;
		> show create database db_name \G # 以行来打印
	# 修改数据库的定义
		> alter database db_name charset=latin1; # 修改字符集为latin1
	# 删除数据库
		> drop database if exists db_name; # 如果数据存在则删除，否则什么也不干
	# 选择某个数据库
		> use db_name;
		> select database(); # 查看当前使用的数据库
		> select * from mysql.user; # 指定查询mysql数据库中的user表
	mysql -uroot -p shiyanlou001; # 指定启动mysql时启用的数据库

# 语言结构和数据类型
	# 字符串
		CHAR # 长度固定，最大2555，超出的部分会被删除
		VARCHAR # 变长，最大65535，超出设定部分会丢失
		TEXT # 不需要指定长度
		BLOB # 保存二进制文件
		ENUM # 枚举，枚举以外的值会被设定为空字符串
		SET # 值可以有多个，每个用括号分开
		# 使用格式
			select "shiyan\tlou"
	# 数字
		DECIMAL(n,m) # n-浮点数总位数，m-小数位数
		FLOAT 	# 4个字节
		DOUBLE # 8个字节
		BOOL
		# 使用格式
			true,false,TRUE,FALSE,100,-100,1.2e.3,2.67
	# 日期和时间
		DATE # YYYY-MM-DD格式显示
		TIME #  HH:MM:SS/HHH:MM:SS格式显示
		DATETIME # YYYY-MM-DD HH:mm:SS
		使用格式
			DATE("11111111") -- 1111:11:11
			DATE("1111-11-11")
			DATE("1111:11:11")
			TIME("111111") -- 11:11:11
			TIME("1111") -- 00:11:11
			TIME("1 11:") -- 35:00:00 # 空格前面代表几天
	# 识别符
		`` -- 防止名称冲突
	# 注释语句
		单行：#，’--‘
		多行：/* */

# 数据表的操作
	# 显示数据表和表结构
		> show full tables in mysql; # 指定数库显示
		> show tables;
		> desc mysql.db; # 显示表结构
	# 创建表
		> create table people(
		id int primary key auto_increment,
		name varchar(64),
		age int
		);
	# 约束
		primary key
		foreign key
		default
		unique
		not null
	# 查看表创建的语句
		> show create table tbl_name;
		# 显示的结果会被优化显示--包含数据引擎
	# 修改表定义
		# 修改表名
			> alter table student rename students;
		# 添加列
			> alter table tbl_name add column (age int, grade int);
		# 删除列
			> alter table tbl_name drop grade;
		# 修改列定义-默认值
			> alter table tbl_name alter col_name set default 18;
		# 修改列定义
			> alter table tbl_name change old_col_name new_col_name column_definition;
	# 删除表
		> drop table tbl_name;
		
	# 数据表中的数据操作
		# 插入数据
			> insert into tbl_name values();
		# 更新
			> update tbl_name set col_name=value where ..
		# 删除
			> delete from tbl_name where id=4; # 不加条件删除所有行

# 数据查询
	# 导入指定mysql语句
		$ mysql -u root -p < exec_sql.txt
		or
		> source exec_sql.txt;
	# 执行查询命令
		$ mysql -u root -p shiyanlou001 -e "show tables"
	select
	where/like (%,_)
	group by
	having
	order by desc/asc
	
	limit 第几页：每页多少个
	# 子查询
	
# 联结

	> SELECT sc.s_id, sc.c_id, s_name, c_name, grade FROM student AS s, course AS c, sc WHERE s.s_id=sc.s_id AND c.c_id=sc.c_id;
	# 内联结
		> SELECT sc.s_id, sc.c_id, s_name, c_name, grade FROM sc INNER JOIN (student AS s, course AS c) USING(s_id,c_id);
		> SELECT sc.s_id, sc.c_id, s_name, c_name, grade FROM sc INNER JOIN (student AS s, course AS c) ON s.s_id=sc.s_id AND c.c_id=sc.c_id;
	# 外联结
		> SELECT student.s_id,s_name,c_id,grade FROM student LEFT JOIN sc ON student.s_id=sc.s_id;
		> SELECT student.s_id,s_name,c_id,grade FROM sc RIGHT JOIN student ON student.s_id=sc.s_id;
		> SELECT student.s_id,s_name,c_id,grade FROM sc RIGHT JOIN student USING(s_id);
	# 自然联结
		> SELECT * FROM course NATURAL JOIN sc;
# 视图
	# 创建视图
		>  CREATE VIEW all_info AS SELECT sc.s_id,sc.c_id,s_name,c_name,grade,s_age,s_sex,c_time 
		FROM student,course,sc WHERE student.s_id=sc.s_id AND course.c_id=sc.c_id;
		> select * from all_info;
	# 修改视图定义
		> ALTER VIEW all_info AS SELECT sc.s_id, sc.c_id, s_name, c_name, grade 
		FROM student, course, sc WHERE student.s_id=sc.s_id AND course.c_id=sc.c_id;
	# 删除
		> DROP VIEW all_info;
		
# 事务
	# ACID
	# autocommit -- 默认自动提交
	
	# 使用事务
		start [work]
		savepoint identifier # 保存点
		rollback [work]
		commit [work]

# SQL高级特性 - 约束索引
	约束：
		表级
			> CREATE TABLE test1(field1 INT, field2 INT, CONSTRAINT primary_key_test1 PRIMARY KEY(field1,field2));
			> CREATE TABLE test2(field1 INT, field2 INT, CONSTRAINT unique_field1 UNIQUE(field1),CONSTRAINT unique_field2 UNIQUE(field2));
		列级: default, not null
			> CREATE TABLE test1(field1 int PRIMARY KEY, field2 int PRIMARY KEY);
		# 删除主键
			> ALTER TABLE tbl_name DROP PRIMARY KEY
		# 增加主键
			> ALTER TABLE tbl_name ADD [CONSTRAINT [symbol]] PRIMARY KEY
		# 查看unique
			> SHOW INDEX FROM tbl_name
		# 删除unique
			> ALTER TABLE test2 DROP KEY unique_field1;
		# 外键
			> CREATE TABLE sc(
				s_id INT,
				c_id INT,
				grade INT,
				PRIMARY KEY (s_id, c_id),   # s_id, c_id 共同构成主键
				FOREIGN KEY (s_id) REFERENCES student(s_id), # 外键
				FOREIGN KEY (c_id) REFERENCES course(c_id)  # 外键
			) default charset=utf8;
		# 删除指定外键
			> ALTER TABLE sc DROP FOREIGN KEY sc_ibfk_1;
		# 添加外键定义
			> ALTER TABLE sc ADD CONSTRAINT sc_ibfk_1 FOREIGN KEY(s_id) REFERENCES student(s_id) ON DELETE CASCADE;
	# 索引
		# 显示索引
			> SHOW INDEX FROM sc\G
		# 创建索引
			> CREATE UNIQUE INDEX unique_field1 USING BTREE ON test_index(field1);
			> CREATE INDEX index_field2 ON test_index(field2);
		# 删除索引
			> DROP INDEX index_name ON tbl_name
# 权限管理
	# 创建新用户
		> CREATE USER syl001@localhost IDENTIFIED BY "shiyanlou";
	# 删除
		> DROP USER "syl002"@"localhost";
	# 修改密码
		> ALTER USER user IDENTIFIED BY 'new_password'; # 5.7.6之后
		> SET PASSWORD FOR user = PASSWORD('new_password');
	# 修改权限
		> GRANT INSERT(name), UPDATE(name) ON shiyanlou002.test TO "syl001"@localhost;
		> REVOKE INSERT(name) ON shiyanlou002.test FROM "syl001"@"localhost";
# 数据备份
	# mysqldump
		$ mysqldump -u root -p shiyanlou001> dump.sql # 备份shiyanlou001数据库
		$ mysqldump [options] --databases db_name > backup_file.sql
		# 恢复
		$ mysql -uroot -p < dump.sql
	# 通过二进制日志备份
		log-bin=mysql_bin_log
		/var/lib/mysql/mysql_bin_log.index
		/var/lib/mysql/mysql_bin_log.000001
		$ mysqlbinlog mysql_bin_log.000001 > new_sql.txt
		$ mysql -u root -p < new_sql.txt