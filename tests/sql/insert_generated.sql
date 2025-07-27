INSERT INTO `project_id.my_dataset.target_table` (
  `Sales_Id`,
  `Region`,
  `Country`,
  `Product`,
  `Sales_Amount`,
  `Sales_Date`,
  `Sales_Channel`,
  `Last_Updated`
)
SELECT
  `Sales_Id`,
  `Region`,
  `Country`,
  `Product`,
  `Sales_Amount`,
  `Sales_Date`,
  `Sales_Channel`,
  `Last_Updated`
FROM `project_id.my_dataset.source_table`;
