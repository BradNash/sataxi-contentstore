ALTER TABLE CONTENTSTORE.CONTENTLINK ADD USERSPECIFIEDKEY varchar(100) NULL;
CREATE INDEX UserSpecifiedKey_IDX ON CONTENTSTORE.CONTENTLINK(UserSpecifiedKey);

