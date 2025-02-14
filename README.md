### 项目开发过程
1. 创建项目
    1. 根目录执行
    ```
    poetry init  # 一直回车
    ```
2. git 托管
    ```
    git init
    ```
3. 创建虚拟环境
    ```
    python3 -m venv venv # 创建虚拟环境

    source venv/bin/activate # 激活虚拟环境
    ```
4. 安装 fastapi
    ```
    poetry add fastapi
    ```
5. 安装 uvicorn
    ```
    poetry add "uvicorn[standard]"
    ```
6. 定义 main.py 后启动项目
    ```
    uvicorn main:app --reload
    ```