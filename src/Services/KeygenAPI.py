import execjs
try:
    from src.Services.ResultModel import Result
except ModuleNotFoundError:
    from Services.ResultModel import Result

class ApiClient():
    def __init__(self):
        with open("src/bundle.js", 'r') as f:
            js_code = f.read()
        
        self.js_ctx = execjs.compile(js_code)



    def get_solutions_for_model(self,model: str) -> list[Result]:        
        solvers:list = self.js_ctx.call("keygen.get_keys",model)
        solutions = []
        for solution in solvers:
            solver = solution[0]
            passwords = solution[1]
            solutions.append( Result(solver,passwords) )
        return solutions
            