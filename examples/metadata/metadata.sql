SELECT 
    JM.WorkflowID, 
    JRD.WorkflowRunID, 
    JRD.RunDate, 
    JRD.RunStartTime
FROM `WorkflowRunDetail` JRD
INNER JOIN `WorkflowMaster` JM 
    ON JRD.WorkflowID = JM.WorkflowID
WHERE JM.WorkflowName = '{DAG_ID}' 
    AND JRD.status = 'R' 
LIMIT 1