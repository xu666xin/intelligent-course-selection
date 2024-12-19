from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from course import CourseSystem


class LanguageDrivenCourseSystem:
    """基于自然语言的课程管理系统"""

    def __init__(self, model) -> None:
        """
        初始化语言驱动的课程系统
        
        Args:
            model: 语言模型实例
        """
        self.model = model
        self.course_system = CourseSystem()

        # 定义处理查询的 Prompt 模板
        self._setup_prompt_template()
        self.query_chain = LLMChain(llm=self.model, prompt=self.query_prompt)

    def _setup_prompt_template(self) -> None:
        """设置用于处理用户查询的 Prompt 模板"""
        self.query_prompt = PromptTemplate(
            input_variables=["query"],
            template="""
            你是一个专业的教务助手，负责帮助学生处理选课相关事务。请根据学生的自然语言输入，解析并生成相应的操作指令。

            你可以处理以下类型的请求：
            1. 查看课程列表
            2. 新增选课
            3. 修改课程信息
            4. 退课操作

            示例对话：
            学生说: "我想选修一门课程，课程名称是深度学习，这是一门关于神经网络的进阶课程"
            输出: {{"action": "add", "name": "深度学习", "type": "选修", "description": "神经网络的进阶课程"}}

            学生说: "帮我看看现在开设了哪些课"
            输出: {{"action": "list"}}

            学生说: {query}
            请直接输出 JSON 格式的操作指令，无需其他解释。
            """
        )

    def handle_query(self, user_input: str) -> dict:
        """
        处理用户的自然语言输入
        
        Args:
            user_input: 用户输入的自然语言查询
            
        Returns:
            dict: 处理结果或错误信息
        """
        # 使用语言模型处理用户输入
        action_json = self.query_chain.run({"query": user_input})
        print(f"生成的操作指令：{action_json}")

        try:
            action = eval(action_json)
        except Exception as e:
            return {
                "error": "解析操作指令失败",
                "details": str(e)
            }

        return self._execute_action(action)

    def _execute_action(self, action: dict) -> dict:
        """
        执行解析后的操作
        
        Args:
            action: 解析后的操作指令
            
        Returns:
            dict: 操作结果或错误信息
        """
        if action["action"] == "list":
            return self.course_system.list_courses()

        elif action["action"] == "add":
            return self.course_system.add_course(
                name=action["name"],
                course_type=action["type"],
                description=action["description"]
            )

        elif action["action"] == "update":
            return self.course_system.update_course(
                course_id=action["id"],
                name=action.get("name"),
                course_type=action.get("type"),
                description=action.get("description")
            )

        elif action["action"] == "delete":
            return self.course_system.delete_course_by_name(
                course_name=action["name"]
            )

        return {"error": "未识别的操作指令"}
