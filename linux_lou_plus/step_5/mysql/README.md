数据库管理系统（DBMS）的功能主要包括以下几个方面：
	数据定义
	数据组织，存储和管理
	数据操作
	数据库的运行和事务管理
	数据库的建立和维护
	通信
# 安装
	$ sudo apt-get install mysql-server
# 登录
	$ mysql -h -u -p
# 配置文件
	/etc/mysql/my.cnf
	
mysql - 客服端	$ mysql --help
mysqld - 服务器端	$ mysqld --verbose --help

SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY

create view `user_all_study_time` as
	select u.id as `user_id`, u.name as `user_name`,sum(uc.study_time) as `all_study_time`
	from `user` as `u` inner join `usercourse` as `uc` on u.id=uc.user_id
	group by `user_id`
	order by `all_study_time`;

create view `course_statistics` as
	select c.name as `course_name`, count(uc.user_id) as `user_count`,sum(uc.study_time) as `all_study_time`
	from `course` as `c` inner join `usercourse` as `uc` on c.id=uc.course_id
	group by `course_id`
	order by `all_study_time` desc;

begin

savepoint

rollback to 
commit

mysql 数据库中：
	user 用户账户，全局权限和其它非特权列

	db 数据库级别的特权

	tables_priv 表级特权

	columns_priv 列级特权

	procs_priv 存储过程和函数权限
