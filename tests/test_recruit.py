from recruit import requisitions


def test_create_requisition():
    my_requisition = requisitions.Requisition()
    requisition_number = my_requisition.create_requisition('admin', 'sales', 'fred', 2)
    assert requisition_number == 1

    requisition_number = my_requisition.create_requisition('admin', 'sales', 'fred', 2)
    assert requisition_number == 2

def test_submit_requisition():
    my_requisition = requisitions.Requisition()
    success = my_requisition.submit_requisition(1)
    assert success



