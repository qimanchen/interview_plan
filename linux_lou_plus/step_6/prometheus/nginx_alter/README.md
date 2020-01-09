# 先根据nginx_log配置好文件
# 验证
$ curl 'http://localhost:9090/api/v1/query?query=nginx_http_requests_total'
{"status":"success","data":{"resultType":"vector","result":
[{"metric":{"__name__":"nginx_http_requests_total",
"host":"localhost","instance":"localhost:9145","job":"nginx","status":"200"},
"value":[1526007699.725,"23"]}]}}

# 安装altermanager
wget http://labfile.oss.aliyuncs.com/courses/980/05/assets/alertmanager-0.15.0-rc.1.linux-amd64.tar.gz
tar -zxvf alertmanager-0.15.0-rc.1.linux-amd64.tar.gz
cd alertmanager-0.15.0-rc.1.linux-amd64
cp simple.yml alertmanager.yml
./alertmanager

# 配置模拟webhook，并启动
./http_ok_server.sh | tee notification.txt # 告警输出到指定文件中