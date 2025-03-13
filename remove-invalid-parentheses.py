class Solution:
    # tc O(2^n * n), sc O(n).
    def removeInvalidParentheses(self, s: str) -> List[str]:
        expression = s
        def rec(i, oc, cc):
            nonlocal max_len

            if oc < cc:
                return
            
            if i == len(expression):
                if oc == cc:
                    valid_expression = "".join(path)
                    if len(valid_expression) > max_len:
                        max_len = len(valid_expression)
                        res.clear()
                        res.append(valid_expression)
                    elif len(valid_expression) == max_len and valid_expression not in res:
                        res.append(valid_expression)
                return
            
            if expression[i] not in ["(", ")"]:
                path.append(expression[i])
                rec(i + 1, oc, cc)
                path.pop()
            else:
                rec(i + 1, oc, cc)  # Exclude
                path.append(expression[i])
                if expression[i] == "(":
                    rec(i + 1, oc + 1, cc)  # Include (
                elif cc < oc:
                    rec(i + 1, oc, cc + 1)  # Include )
                path.pop()
        
        res = []
        path = []
        max_len = 0
        rec(0, 0, 0)
        
        return res if res else [""]