class Requisition:
    def __init__(self):
        self.requisition_number = 0
    def create_requisition(self, job_title, department, manager_name, number_openings = 1 ) :
        self.job_title = job_title
        self.department = department
        self.manager_name = manager_name
        self.number_openings = number_openings
        self.requisition_number +=1
        return self.requisition_number

    def submit_requisition(self,requisition_number):
        return True

    def approve_requisition(self):
        return True
    def reject_requisition(self):
        return True
    def is_requisition_approved():
        return

if __name__ == '__main__':
    job_title = input('Enter Job Title ')
    department = input('Enter department ')
    manager_name = input('Enter manager name ')
    number_openings = input('Enter # of openining')
    requisition = Requisition()
    requisition_number = requisition.create_requisition(job_title, department, manager_name, number_openings )
    print(requisition_number)

    requisition.submit_requisition(requisition_number)

    requisition.approve_requisition()
