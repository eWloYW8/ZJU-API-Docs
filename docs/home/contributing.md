## 引言

本项目仍处于起步阶段，我们欢迎任何形式的贡献，包括但不限于：

- 新增接口文档
- 补全接口参数或响应字段说明
- 修复拼写、语法或结构问题
- 在 Issues 提出改进建议（包括内容、排版、结构、项目规划等）

!!! warning "注意事项"
    在开始之前，请确保具备基本的 Git 与 Markdown 使用经验，并遵守本项目的结构与规范。

## 项目结构简介

本项目基于 [MkDocs](https://www.mkdocs.org/) 构建，使用 `docs/` 目录存放所有文档内容，API 文档按照模块分类存放。当前结构如下：

```

ZJU-API-Docs/
├── docs/
│   ├── index.md              # 项目简介
│   ├── home/                 # 首页
│   ├── zjuam/                # 统一身份认证
│   ├── courses/              # 学在浙大
│   ├── webvpn/               # WebVPN
│   └── classroom/            # 智云课堂
├── mkdocs.yml                # MkDocs 配置文件
└── ...

```

## 本地构建

在提交文档前，你可以在本地构建并预览整个站点，以确保内容格式正确、结构清晰。

### 环境

- Python 3.7+
- pip
- Git

### 构建和预览

1. 克隆仓库：

    ```bash
    git clone https://github.com/ewloyw8/ZJU-API-Docs.git
    cd ZJU-API-Docs
    ```

2. 安装依赖：

    ```bash
    pip install -r requirements.txt
    ```

    ```bash
    mkdocs serve
    ```

默认将在 `http://127.0.0.1:8000/` 启动本地预览服务。你可以在浏览器中访问它，查看文档实时效果。


## 接口文档示例结构

---
### 示例：获取 PPT 信息

获取智云课堂平台指定课程的 PPT 信息

{{ badge("GET", "green", "tiny") }}`https://classroom.zju.edu.cn/pptnote/v1/schedule/search-ppt`

#### Cookie
| 名称 | 必填 | 描述 |
|------|-----|------|
| _token | 是 | 用于鉴权，可通过 [待补充] 获得 |

#### 参数
| 名称 | 必填 | 默认值 | 描述 |
|------|-----|-------|------|
| course_id | 是 | | 课程 ID |
| sub_id | 是 | | 课堂 ID |
| page | 否 | 1 | 查询页码 |
| per_page | 否 | 10 | 每页结果数量 |

#### 响应

格式：JSON

| 名称 | 描述 |
|------|------|
| code | 返回码，`0`表示成功 |
| list | 包含一张 PPT 图片详细信息的列表 |
| message | 返回消息 |
| total | PPT 总数量 |


??? info "响应内容示例"
    ```json
    {
        "code": 0,
        "list": [
            {
                "content": "{\"detecttype\":\"ppt\",\"is_key\":false,\"pptimgurl\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/5e8f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/1747200084000.jpg\",\"status\":\"running\",\"taskid\":\"5e8f0f4d-2181-403a-9376-6ec573b8a8ea\",\"pptthumb\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/5e8f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/s_1747200084000.jpg\",\"created\":\"1747200084000\"}",
                "course_id": 60889,
                "create_time": "2025-05-14 13:18:51",
                "created_sec": 0,
                "default": 1,
                "id": 6563405,
                "sub_id": 1326369,
                "update_time": "2025-05-14 13:18:51"
            },
            {
                "content": "{\"detecttype\":\"ppt\",\"is_key\":false,\"pptimgurl\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/5e8f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/1747200157480.jpg\",\"status\":\"running\",\"taskid\":\"5e8f0f4d-2181-403a-9376-6ec573b8a8ea\",\"pptthumb\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/5e9f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/s_1747200157480.jpg\",\"created\":\"1747200157480\"}",
                "course_id": 60889,
                "create_time": "2025-05-14 13:20:03",
                "created_sec": 0,
                "default": 1,
                "id": 6563421,
                "sub_id": 1326369,
                "update_time": "2025-05-14 13:20:03"
            }
        ],
        "msg": "查询成功",
        "total": 296
    }
    ```

---

以上为一个 API 的示例结构

??? info "示例源码"
    ````markdown
    ### 示例：获取 PPT 信息

    获取智云课堂平台指定课程的 PPT 信息

    {% raw %}{{ badge("GET", "green", "tiny") }}{% endraw %}`https://classroom.zju.edu.cn/pptnote/v1/schedule/search-ppt`

    #### Cookie
    | 名称 | 必填 | 描述 |
    |------|-----|------|
    | _token | 是 | 用于鉴权，可通过 [待补充] 获得 |

    #### 参数
    | 名称 | 必填 | 默认值 | 描述 |
    |------|-----|-------|------|
    | course_id | 是 | | 课程 ID |
    | sub_id | 是 | | 课堂 ID |
    | page | 否 | 1 | 查询页码 |
    | per_page | 否 | 10 | 每页结果数量 |

    #### 响应

    格式：JSON

    | 名称 | 描述 |
    |------|------|
    | code | 返回码，`0`表示成功 |
    | list | 包含一张 PPT 图片详细信息的列表 |
    | message | 返回消息 |
    | total | PPT 总数量 |


    ??? info "响应内容示例"
        ```json
        {
            "code": 0,
            "list": [
                {
                    "content": "{\"detecttype\":\"ppt\",\"is_key\":false,\"pptimgurl\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/5e8f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/1747200084000.jpg\",\"status\":\"running\",\"taskid\":\"5e8f0f4d-2181-403a-9376-6ec573b8a8ea\",\"pptthumb\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/5e8f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/s_1747200084000.jpg\",\"created\":\"1747200084000\"}",
                    "course_id": 60889,
                    "create_time": "2025-05-14 13:18:51",
                    "created_sec": 0,
                    "default": 1,
                    "id": 6563405,
                    "sub_id": 1326369,
                    "update_time": "2025-05-14 13:18:51"
                },
                {
                    "content": "{\"detecttype\":\"ppt\",\"is_key\":false,\"pptimgurl\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/    5e8f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/1747200157480.jpg\",\"status\":\"running\", \"taskid\":\"5e8f0f4d-2181-403a-9376-6ec573b8a8ea\",\"pptthumb\":\"https:\\/\\/video.cmc.zju.edu.cn\\/ai3\\/ppt\\/   5e9f0f4d-2181-403a-9376-6ec573b8a8ea\\/2025051405\\/s_1747200157480.jpg\",\"created\":\"1747200157480\"}",
                    "course_id": 60889,
                    "create_time": "2025-05-14 13:20:03",
                    "created_sec": 0,
                    "default": 1,
                    "id": 6563421,
                    "sub_id": 1326369,
                    "update_time": "2025-05-14 13:20:03"
                }
            ],
            "msg": "查询成功",
            "total": 296
        }
        ```
    ````

总结 API 信息过程较为繁琐，可以使用 AI 工具分析响应内容、撰写文档

!!! warning "编辑规范"
    * 所有文档必须使用 UTF-8 编码，使用标准 Markdown 格式
    * 表格对齐不强制，但需确保语义清晰
    * 接口文档应说明请求方式、URL等核心信息，**对于暂时不明确的信息可省略**，仅有极少的信息也可提交贡献
    * 示例数据请使用脱敏/模拟信息，**不要上传真实 Cookie、Token 或个人信息**
    * **禁止包含 API 存在的鉴权漏洞和违法用途**
    * 文档命名请使用全小写英文，单词间用 `-` 分隔，如 `login-status.md`

## 提交规范

本项目采用 **[约定式提交规范](https://www.conventionalcommits.org/zh-hans/v1.0.0/)** 来规范 Git 提交记录。

请在提交 API 文档或其他内容时，尽量遵守以下格式。

### 提交格式

```text
<type>([scope]): <subject>
```

* `type`：用于说明提交的类别（必填）
* `scope`：可选，说明影响的模块、文件夹或功能块
* `subject`：简要描述修改内容，建议使用中文


### 常用类型（type）

| 类型       | 含义说明                      |
| -------- | ------------------------- |
| feat     | 添加新功能或文档内容（如新增接口）         |
| fix      | 修复错误，如参数描述错误、字段类型错误等      |
| docs     | 修改说明文档，如 `README`、结构优化等   |
| style    | 改进格式、排版、空格、拼写等（不影响内容逻辑）   |
| refactor | 内容结构调整，但不影响接口本身           |
| chore    | 项目构建、依赖更新、mkdocs 配置等杂项    |
| perf     | 提升渲染/加载效率等                |


### 示例

```text
feat(auth): 添加统一身份认证登录接口文档
fix: 修复智云课堂课程列表响应字段拼写错误
docs: 更新贡献指南和本地构建说明
style: 调整表格缩进与对齐格式
refactor: 拆分智云课堂接口为多个文件
chore: 配置 mkdocs-material 主题支持
```

## 帮助资源

* [MkDocs 官方文档](https://www.mkdocs.org/)
* [Markdown 基础语法](https://www.markdownguide.org/basic-syntax/)
* [Git 入门教程](https://learngitbranching.js.org/)
* [Microsoft Edge DevTools 文档](https://learn.microsoft.com/zh-cn/microsoft-edge/devtools-guide-chromium/landing/)
* [HTTP 教程](https://www.runoob.com/http/http-tutorial.html)

## 致谢

感谢每一位为本项目贡献内容、提出建议的朋友。

如有任何问题，欢迎通过 GitHub Issue 与我们交流。
