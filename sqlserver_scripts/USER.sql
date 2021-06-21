ALTER TABLE [USER] ADD Django_LAST_LOGIN smalldatetime
GO
ALTER TABLE [USER] ADD Django_USERNAME varchar(61)
GO

UPDATE [USER]
SET Django_USERNAME=COALESCE(i.FORENAME + ' ', '') + i.SURNAME
FROM individual i
WHERE i.name_key=[USER].name_key