# 数据库编程

# python 数据库API介绍
	apilevel -- 全局变量，显示数据库模块的API版本号
	threadsafety -- 全局变量，指定数据库模块的线程安全等级
		3 -- 模块完全是线程安全的
		1 -- 模块具有部分线程安全性，线程可以共享该模块，但不能共享连接
		0 -- 表示线程完全不能共享该模块
	paramstyle -- 指定当SQL语句需要参数时的，参数的风格
		format -- python标准化的格式化字符串参数
		pyformat -- 在SQL语句中使用拓展的格式代码参数
		qmark -- 使用问号（？）代表参数
		numeric
		named
		
	# 数据库API的核心类
		connect() -- 用于连接数据库，并返回连接对象
			# 连接对象具有的方法和属性
				cursor(factory=Cursor) -- 打开游标，返回一个游标对象
					# 该游标对象用于执行各种SQL语句 -- DDL, DML, select
					# 游标对象具有的方法和属性
						execute(sql[, parameters]) -- 执行SQL语句，parameters 为SQL语句中的参数指定值
						executemany(sql, seq_of_parameters) -- 重复执行SQL语句， seq_of_parameters, 序列中多少个元素，sql语句执行多少次
						executemany(sql_script) -- 直接包含多条sql语句的sql脚本
						fetchone() -- 获取查询集的下一行，若没有下一行，返回None
						fetchmany(size=cursor.arraysize) -- 返回查询集的下N行
						fetchall() -- 返回所有查询结果（列表）
						close() -- 关闭游标
						arraysize -- 设置或获取fetchmany()默认获取的记录条数
						description -- 只读，获取最后一次查询返回的所有列的信息，列标题
						connection -- 返回创建游标的数据库连接对象
						rowcount -- 获取update语句所修改的记录的条数
						executescript(sql语句执行脚本 -- 多条sql语句)
					
					# 游标本身是个迭代对象，可以直接通过for循环获取每个查询的结果
				commit() -- 提交事务
				rollback() -- 回滚事务
				close() -- 关闭连接
				isolation_level  -- 返回或设置事务的隔离级别
				in_transaction -- 判断当前是否处于事务中
				
				# 为简化编程
				execute(sql[, parameters])
				executemany(sql[,parameters])
				executescript(sql_script)
				
				create_function(name,num_params, func) -- 注册自定义函数
					name -- 自定义函数名称
					num_params -- 参数个数
					func -- 自定义参数对应的函数
				create_aggregate() -- 自定义聚集函数
					name
					num_params
					aggregate_class -- 聚集函数实现类，step(self, params), finalize(self) 必须实现的两个方法
				create_collation(name, callable) -- 自定义比较函数
					callable -- 指定自定义比较函数对应的函数，该函数包含两个参数，并对这两个参数进行比较
					
		
		# 主要两个功能
			1. 数据库连接， 获取游标，控制事务
			2. 游标：执行各种sql语句
			
	# 操作数据库的基本流程
		1. 调用connect()打开数据库连接，并返回数据库连接对象
		2. 通过数据库连接对象打开连接
		3. 使用游标执行sql语句
		4. 关闭游标
		5. 关闭数据库连接


# 操作SQLite数据库
	DDLs/sqlite3.dll
	SQLite -- 嵌入式的数据库引擎, 只是一个文件，不需要服务器进程
	SQLite内部只支持NULL、INTEGER、REAL（浮点数）、TEXT（文本）、BLOB（大二进制对象）
	SQLite允许把各种类型的数据保存到任何类型的字段中
	SQLite允许存入数据时忽略底层数据列实际的数据类型
	
	# 可视化界面
		http://www.sqliteexpert.com/download.html --- SQLite Expert
		
# MYSQL
	MySQL默认使用UTF-8字符串
	
	pip工具管理模块
		1. 查看已安装的模块
			pip show packagename -- 显示包的详细描述信息
		2. 卸载已安装的模块
			pip uninstall packagename
			
			pip list
		3. 安装
			pip install packagename
	
	# mysql-connector-python -- 操作mysql
		import mysql.connector
		mysql.connector.connect(user='root', password="...", host='localhost', port='3306', database='python', use_unicode=True)
		