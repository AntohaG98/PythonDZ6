# Задача 4
# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# Пример:
# 2 + 2 => 4;
# 1 + 2 * 3 => 7;
# 1 - 2 * 3 => -5;

from math import sin,cos,log,exp
 
def calc(formula):
    
    def parse(formula):
        res=[]
        tmp=''
        for s in formula:
            if s in (',','(',')','+','-','*','/','^'):
                if len(tmp)>0:
                    res.append(tmp)
                res.append(s)
                tmp=''
            else:
                tmp=tmp+s
        if len(tmp)>0:
            res.append(tmp)
        return res
        
    def prty_arn(op):
        ops=['(','+','-','*','/','^','sin','cos','log','exp']
        prt=[0,1,1,2,2,3,3,3,3,3]
        arn=[0,2,2,2,2,2,1,1,1,1]
        k=ops.index(op)
        return (prt[k],arn[k])
    
    def exec_op(op):
        
        (_,arn)=prty_arn(op)
        
        if arn==2:
            a2=stack_n.pop()
            a1=stack_n.pop()
        else:
            a1=stack_n.pop()
 
        if op=='+':
            return a1+a2
        elif op=='-':
            return a1-a2
        elif op=='*':
            return a1*a2
        elif op=='/':
            return a1/a2
        elif op=='^':
            return a1**a2
        elif op=='sin':
            return sin(a1)
        elif op=='cos':
            return cos(a1)
        elif op=='exp':
            return exp(a1)
        elif op=='log':
            return log(a1)
        return None
 
    arr_lex=parse(formula)
    stack_o=[]
    stack_n=[]
    
    for lex in arr_lex:
        
        if '9'>=lex[0]>='0':
            
            stack_n.append(float(lex))
            
        elif lex=='(':
            
            stack_o.append(lex)
            
        elif lex==')':
            
            while len(stack_o)>0:
                op=stack_o.pop()
                if op=='(':
                    break
                stack_n.append(exec_op(op))
            else:
                return (None,'Несбалансированы скобки-1')
 
        else:
            
            if len(stack_o)==0:
                stack_o.append(lex)
            else:
                
                (pn,_)=prty_arn(lex)
                (po,_)=prty_arn(stack_o[-1])
                
                if pn>po:
                    stack_o.append(lex)
                else:
                    while True:
                        op=stack_o.pop()
                        stack_n.append(exec_op(op))
                        if len(stack_o)==0 or stack_o[-1] != po:
                            break
                    stack_o.append(lex)
                    
    while len(stack_o)>0:
        op=stack_o.pop()
        stack_n.append(exec_op(op))
 
    if len(stack_n)==1:
        
        return (stack_n[0],'OK')
        
    else:
        
        return (None,'Несбалансированы скобки-2')
 
####################################################
 
print(calc("5+7-sin(7*3)"))
print(eval("5+7-sin(7*3)"))