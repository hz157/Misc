# Json 文件说明
> 该项目中Json文件用于存放执行参数，截至2022年11月14日，共有3个json文件，分别为👇

- config.json 脚本执行参数
- mail.json 邮件配置参数
- users.json 用户参数

### config.json
```json
[
    {
        "email": "False", // 是否启用邮件通知，True 启用，False 弃用
        "week": "True" // 是否执行周末打卡，True 启用，False 弃用
    }
]
```

### mail.json 
```json
[
    {
    "account" : "your mail account", // 邮箱账号
    "password" : "your mail password", // 邮箱密码
    "server" : "your mail server", // 邮件服务器地址
    "pop_port" : "pop3 port", // 邮件服务器pop3 端口
    "imap_port" : "imap port", // 邮件服务器imap端口
    "smtp_port" : "smtp port" // 邮件服务器 smtp端口
    }
]

```

### users.json
支持多个用户名
```json
[
    {
        "name": "姓名",
        "stucode": "学号",
        "password": "密码",
        "schoolcode": "学校代码",
        "mail" : "邮箱",
        "contact" : "电话",
        "position" : "打卡地址"
    },
     {
        "name": "姓名",
        "stucode": "学号",
        "password": "密码",
        "schoolcode": "学校代码",
        "mail" : "邮箱",
        "contact" : "电话",
        "position" : "打卡地址"
    }
]

```