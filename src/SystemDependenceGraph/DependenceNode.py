
class DependenceNode:
    def __init__(self):
        self.parents = []
        self.children = []
        self.inter_parents = []
        self.inter_children = []
        self.fictitious_parents = []
        self.fictitious_children = []
        self.ast = None

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.children.append(child)
    
    def add_inter_parent(self, parent):
        self.inter_parents.append(parent)

    def add_inter_child(self, child):
        self.inter_children.append(child)

    def add_fictitious_parent(self, parent):
        self.fictitious_parents.append(parent)

    def add_fictitious_child(self, child):
        self.fictitious_children.append(child)

    def set_ast(self, ast):
        self.ast = ast

    def get_parents(self):
        return self.parents
    
    def get_children(self):
        return self.children
    
    def get_inter_parents(self):
        return self.inter_parents
    
    def get_inter_children(self):
        return self.inter_children

    def get_fictitious_parents(self):
        return self.fictitious_parents
    
    def get_fictitious_children(self):
        return self.fictitious_children

class InputNode(DependenceNode):
    def __init__(self, label):
        super().__init__()
        self.label = label

    def clone(self):
        clone = InputNode(self.label)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return "IN: " + self.label

class OutputNode(DependenceNode):
    def __init__(self, label):
        super().__init__()
        self.label = label
    
    def clone(self):
        clone = OutputNode(self.label)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return  "OUT: " + self.label

class ConstNode(DependenceNode):
    def __init__(self, const_ast):
        super().__init__()
        self.value =  const_ast.value
        self.ast = const_ast

    def clone(self):
        clone = ConstNode(self.ast)
        return clone

    def __str__(self):
        return "CONST: " + self.value

class CondNode(DependenceNode):
    def __init__(self, cond_statement):
        super().__init__()
        self.cond_statement = cond_statement

    def clone(self):
        clone = CondNode(self.cond_statement)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return  "COND: " + ", ".join(self.cond_statement.get_cond_dependencies())

class AssignNode(DependenceNode):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def clone(self):
        clone = AssignNode(self.name)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return self.name

class AlwaysNode(DependenceNode):
    def __init__(self, sensList):
        super().__init__()
        self.sensList = sensList

    def get_sensList(self):
        return self.sensList

    def clone(self):
        clone = AlwaysNode(self.sensList)
        clone.ast = self.ast
        return clone
    
    def __str__(self):
        return "ALWAYS @(" + " ,".join(self.sensList) + ")"
    
class CouplingNode(DependenceNode):
    def __init__(self, invar, outvars):
        super().__init__()
        self.invar = invar
        self.outvars = outvars
    
    def get_invar(self):
        return self.invar

    def get_outvars(self):
        return self.outvars
    
    def clone(self):
        clone = CouplingNode(self.invar, self.outvars)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return self.invar + "; " + ", ".join(self.outvars)

class InstanceNode(DependenceNode):
    def __init__(self, name):
        super().__init__()
        self.modulename = name
    
    def get_modulename(self):
        return self.modulename

    def clone(self):
        clone = InstanceNode(self.modulename)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return "INSTANCE: " + self.modulename

class ModuleNode(DependenceNode):
    def __init__(self, name):
        super().__init__()
        self.modulename = name

    def get_modulename(self):
        return self.modulename

    def clone(self):
        clone = ModuleNode(self.modulename)
        clone.ast = self.ast
        return clone
    
    def __str__(self):
        return "MODULE DEF: " + self.modulename

class ParameterNode(DependenceNode):
    def __init__(self, name, ids, consts):
        super().__init__()
        self.name = name
        self.ids = ids
        self.consts = consts

    def clone(self):
        clone =  ParameterNode(self.name, self.ids, self.consts)
        clone.ast = self.ast
        return clone

    def __str__(self):
        return "PARAMETER: " + self.name +" - " + ", ".join([str(el) for el in self.ids+self.consts])


class FunctionNode(DependenceNode):
    def __init__(self, name):
        super().__init__()
        self.name = name
       
    def clone(self):
        clone = FunctionNode(self.name)
        clone.ast= self.ast
        return clone
    
    def __str__(self):
        return "FUNCTION: " + self.name