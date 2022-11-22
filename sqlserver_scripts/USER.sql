IF NOT EXISTS (
  SELECT *
  FROM   sys.columns
  WHERE  object_id = OBJECT_ID(N'[dbo].[USER]')
         AND name = 'Django_LAST_LOGIN'
)
  ALTER TABLE [USER] ADD Django_LAST_LOGIN smalldatetime
GO

IF NOT EXISTS (
  SELECT *
  FROM   sys.columns
  WHERE  object_id = OBJECT_ID(N'[dbo].[USER]')
         AND name = 'Django_USERNAME'
)
  ALTER TABLE [USER] ADD Django_USERNAME varchar(61)
GO

UPDATE [USER]
SET Django_USERNAME=COALESCE(i.FORENAME + ' ', '') + i.SURNAME
FROM individual i
WHERE i.name_key=[USER].name_key