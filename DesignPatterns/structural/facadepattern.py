class JavaSkill:
    # subsystem 1
    def skill_set_java(self):
        return "Java skill added"


class SeleniumSkill:
    # subsystem2
    def skill_selenium(self):
        return "selenium skill added"


class JenkinsSkill:
    # subsystem3
    def skill_jenkins(self):
        return "Jenkins skill added"


class FacadeFullStackSDET:
    def __init__(self):
        self.java = JavaSkill()
        self.selenium = SeleniumSkill()
        self.jenkins = JenkinsSkill()

    def full_stack_sdet(self):
        result = self.java.skill_set_java()
        result += self.selenium.skill_selenium()
        result += self.jenkins.skill_jenkins()
        return result


facade_sdet = FacadeFullStackSDET()
print(facade_sdet.full_stack_sdet())
