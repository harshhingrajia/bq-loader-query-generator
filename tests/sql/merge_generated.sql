MERGE INTO `my_dataset.my_table` T
USING (
  SELECT
    `MAXForecastDate`,
    `MINForecastDate`
  FROM `my_dataset.staging_table`
) AS S
ON 
WHEN MATCHED THEN
  UPDATE SET 
    MAXForecastDate = S.MAXForecastDate,    MINForecastDate = S.MINForecastDate
WHEN NOT MATCHED THEN
  INSERT (
    `MAXForecastDate`,
    `MINForecastDate`,
    `ID`
  )
  VALUES (
    S.MAXForecastDate,
    S.MINForecastDate,
    S.ID
  );