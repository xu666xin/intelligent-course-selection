class CourseSystem:
    """课程管理系统类，提供课程的基本操作功能"""
    
    def __init__(self):
        """初始化课程系统，设置初始课程数据"""
        self.courses = [
            {
                "id": 1,
                "name": "网球基础",
                "type": "选修",
                "description": "体育类课程，学习网球基本技巧"
            },
            {
                "id": 2,
                "name": "高等数学",
                "type": "必修",
                "description": "理工科基础课程，微积分与极限"
            },
            {
                "id": 3,
                "name": "Java程序设计",
                "type": "必修",
                "description": "计算机核心课程，面向对象编程"
            },
            {
                "id": 4,
                "name": "创新思维",
                "type": "选修",
                "description": "通识教育课程，培养创造性思维"
            },
            {
                "id": 5,
                "name": "数据结构",
                "type": "必修",
                "description": "计算机基础课程，算法与数据组织"
            },
            {
                "id": 6,
                "name": "英语口语",
                "type": "选修",
                "description": "语言类课程，提升口语交际能力"
            },
            {
                "id": 7,
                "name": "机器学习导论",
                "type": "选修",
                "description": "人工智能入门课程，算法基础"
            },
            {
                "id": 8,
                "name": "电路原理",
                "type": "必修",
                "description": "电子工程基础，电路分析方法"
            },
        ]
        self.next_id = len(self.courses) + 1

    def list_courses(self) -> list:
        """
        列出所有课程
        
        Returns:
            list: 所有课程的列表
        """
        return self.courses

    def add_course(self, name: str, course_type: str, description: str) -> dict:
        """
        添加新课程
        
        Args:
            name: 课程名称
            course_type: 课程类型（必修/选修）
            description: 课程描述
            
        Returns:
            dict: 新添加的课程信息
        """
        new_course = {
            "id": self.next_id,
            "name": name,
            "type": course_type,
            "description": description,
        }
        self.courses.append(new_course)
        self.next_id += 1
        return new_course

    def update_course(self, course_id: int, name: str = None, 
                     course_type: str = None, description: str = None) -> dict:
        """
        更新课程信息
        
        Args:
            course_id: 课程ID
            name: 新的课程名称（可选）
            course_type: 新的课程类型（可选）
            description: 新的课程描述（可选）
            
        Returns:
            dict: 更新后的课程信息或错误信息
        """
        for course in self.courses:
            if course["id"] == course_id:
                if name:
                    course["name"] = name
                if course_type:
                    course["type"] = course_type
                if description:
                    course["description"] = description
                return course
        return {"error": f"未找到课程 ID 为 {course_id} 的课程"}

    def delete_course(self, course_id: int) -> dict:
        """
        根据ID删除课程
        
        Args:
            course_id: 要删除的课程ID
            
        Returns:
            dict: 操作结果信息
        """
        for course in self.courses:
            if course["id"] == course_id:
                self.courses.remove(course)
                return {"status": "success", "removed": course}
        return {"error": f"未找到课程 ID 为 {course_id} 的课程"}

    def delete_course_by_name(self, course_name: str) -> dict:
        """
        根据名称删除课程
        
        Args:
            course_name: 要删除的课程名称
            
        Returns:
            dict: 操作结果信息
        """
        for course in self.courses:
            if course["name"] == course_name:
                self.courses.remove(course)
                return {"status": "success", "removed": course}
        return {"error": f"未找到课程名称为 {course_name} 的课程"}



