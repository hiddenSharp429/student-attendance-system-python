```javascript
// index.js
Page({
    getInfo() {
        // 请求的接口地址
        var apiUrl = 'http://43.136.80.11:5000/student_manager/view_all_students'; # 后面这个参数可能会不同，具体参考api调用文档

        wx.request({
            url: apiUrl,
            method: 'GET',
            success: function (res) {
                if (res.statusCode === 200) {
                    // 接受参数
                    var students = res.data.students;
    
                    // 展开各个学生的信息
                    for (var i = 0; i < students.length; i++) {
                        console.log(students[i]);
                    }
                } else {
                    // 捕捉状态报错
                    console.error('Error:', res.statusCode, res.data);
                }
            },
            fail: function (error) {
                // 捕捉请求报错
                console.error('Request failed:', error);
            }
        });
    
    }
})