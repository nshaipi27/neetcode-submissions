class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        answer = [] # list
        for token in tokens:
            if token == "+":
                n1, n2 = answer.pop(), answer.pop()
                answer.append(n1+n2)
            elif token == "-":
                n1, n2 = answer.pop(), answer.pop()
                answer.append(n2-n1)
            elif token == "*":
                n1, n2 = answer.pop(), answer.pop()
                answer.append(n1*n2)
            elif token == "/":
                n1, n2 = answer.pop(), answer.pop()
                answer.append(int(n2 / n1))
            else:
                answer.append(int(token))
        return answer[0]
        

