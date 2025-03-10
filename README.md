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
    source venv/bin/activate # macOS/Linux
    source venv/Scripts/activate # Windows
    uvicorn main:app --reload
    ```

### 启动项目
    - 数据库准备
        ```
        1. 拉取数据库镜像
        docker pull harbor.iluvatar.com.cn:10443/library/mariadb:v0.2-sql
        2. 启动数据库容器
        sudo docker run --name mydb -e MYSQL_ROOT_PASSWORD=admin12345 -p 3306:3306 -d 524adc4c89c3 
        3. 创建数据库
        CREATE DATABASE FastAdmin
            DEFAULT CHARACTER SET = 'utf8mb4';
        ```
    - Python 环境配置
        ```
        1. python3 -m venv venv # 创建虚拟环境

        2. 进入虚拟环境
           source venv/bin/activate # Mac
           venv/Scripts/activate # Windows
        3. 退出 虚拟环境
           deactivate

        3. 安装python依赖包
           poetry install
        ```
    - 启动FastAPI
        ```
        uvicorn main:app --reload
        ```
        