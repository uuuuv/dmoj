def map_test_cases(problem_cases):
    batch_order = 1
    sub_order = 1
    in_batch = 0
    testcases_map = []
    batch = 1
    for case in problem_cases: 
        item = {"order": case.order, "type": case.type}
        item['is_pretest'] = case.is_pretest
        item['batch_order'] = batch_order

        if case.type == 'S':
            in_batch = 1
            item['batch'] = batch

        elif case.type == 'C' and in_batch == 1:
            item['sub_order'] = sub_order
            sub_order += 1

        elif case.type == 'C' and in_batch == 0:
            item['batch_order'] = batch_order
            item['batch'] = batch
            batch_order = batch_order + 1

        else:
            in_batch = 0
            batch_order = batch_order + 1
            sub_order = 1
        
        if case.type == 'E':
            batch += 1
            
        testcases_map.append(item)

    return testcases_map