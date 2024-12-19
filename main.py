#!/usr/bin/env python3
"""
智能选课系统入口程序
"""

import os
from typing import NoReturn
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from languagedriven import LanguageDrivenCourseSystem


def initialize_model() -> ChatOpenAI:
    """
    初始化语言模型
    
    Returns:
        ChatOpenAI: 配置好的语言模型实例
    """
    return ChatOpenAI(
        model="Qwen2.5-14B",
        openai_api_base=os.getenv("OPENAI_API_BASE"),
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )


def run_interactive_session(system: LanguageDrivenCourseSystem) -> NoReturn:
    """
    运行交互式选课会话
    
    Args:
        system: 语言驱动的课程系统实例
    """
    print("\n欢迎使用智能选课系统！")
    print("您可以通过自然语言进行选课、查询课程、删除课程等操作。")
    print("输入 '退出' 或 'exit' 结束程序。\n")
    
    while True:
        user_input = input("\n请输入您的需求（例如：查询所有选修课）：")
        if user_input.lower() in ["退出", "exit"]:
            print("\n感谢使用，再见！")
            break
            
        result = system.handle_query(user_input)
        print("\n系统响应：", result)


def main() -> None:
    """主程序入口"""
    # 加载环境变量
    load_dotenv()
    
    try:
        # 初始化系统组件
        model = initialize_model()
        course_system = LanguageDrivenCourseSystem(model)
        
        # 启动交互式会话
        run_interactive_session(course_system)
        
    except Exception as e:
        print(f"\n程序运行出错：{str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
