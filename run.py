import subprocess
import os


def activate_venv_and_run_app():
    try:
        # 构建激活虚拟环境的命令
        if os.name == "nt":
            activate_cmd = "venv\\Scripts\\activate.bat"
        else:
            # 使用 . 代替 source 或者显式使用 bash
            shell = os.getenv("SHELL", "/bin/bash")  # 提供默认值
            if shell.endswith("sh"):
                activate_cmd = ". venv/bin/activate"
            else:
                activate_cmd = "source venv/bin/activate"

        # 启动应用的命令
        start_cmd = ["uvicorn", "main:app", "--reload"]

        # 使用 shell=True 执行命令
        command = f"{activate_cmd} && {' '.join(start_cmd)}"
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the app: {e}")


if __name__ == "__main__":
    activate_venv_and_run_app()
