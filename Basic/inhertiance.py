from selenium.webdriver.common.devtools.v85.css import get_computed_style_for_node

from OOPs_Concept import function


class childclass(function):
    num2 = 300

    def __init__(self):
        function.__init__(self, 2, 6)

    def getcompletedata(self):
        return self.num + self.num2 + self.Summation()


obj = childclass()
print(obj.getcompletedata())