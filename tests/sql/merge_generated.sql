MERGE INTO `project_id.my_dataset.target_table` T
USING (
  SELECT
    `Sales_Id`,
    `Region`,
    `Country`,
    `Product`,
    `Sales_Amount`,
    `Sales_Date`,
    `Sales_Channel`,
    `Last_Updated`
  FROM `project_id.my_dataset.source_table`
) AS S
ON T.Sales_Id = S.Sales_Id
WHEN MATCHED THEN
  UPDATE SET
    T.Region = S.Region,
    T.Country = S.Country,
    T.Product = S.Product,
    T.Sales_Amount = S.Sales_Amount,
    T.Sales_Date = S.Sales_Date,
    T.Sales_Channel = S.Sales_Channel,
    T.Last_Updated = S.Last_Updated

WHEN NOT MATCHED THEN
  INSERT (
    `Sales_Id`,
    `Region`,
    `Country`,
    `Product`,
    `Sales_Amount`,
    `Sales_Date`,
    `Sales_Channel`,
    `Last_Updated`
  )
  VALUES (
    S.Sales_Id,
    S.Region,
    S.Country,
    S.Product,
    S.Sales_Amount,
    S.Sales_Date,
    S.Sales_Channel,
    S.Last_Updated
  );
