from Repo.repo_problems import RepoProblems
from UI.console import Console
from UI.ui import UI
from Service.service_students import ServiceStudents
from Service.service_problems import ServiceProblems
from Repo.repo_students import RepoStudents
from Validators.validate_problem import ValidateProblem
from Validators.validate_student import ValidateStudent

if __name__ == '__main__':
	console = Console()
	repo_students = RepoStudents()
	repo_problems = RepoProblems()
	validators = ValidateStudent()
	validatorp = ValidateProblem()
	service_students = ServiceStudents(repo_students, validators)
	service_problems = ServiceProblems(repo_problems, validatorp)
	ui = UI(console, service_students, service_problems)
	ui.start()
	

