ALTER TABLE ContentStore.ContentData ALTER COLUMN TmStamp SET DEFAULT (CURRENT_TIMESTAMP);
ALTER TABLE ContentStore.ContentLink ALTER COLUMN TmStamp SET DEFAULT (CURRENT_TIMESTAMP);
ALTER TABLE ContentStore.ContentMetadata ALTER COLUMN TmStamp SET DEFAULT (CURRENT_TIMESTAMP);

ALTER TABLE ContentStore.ContentData ADD CONSTRAINT FK_ContentStore_ContentData_ContentStore_ContentLink_ContentLinkID FOREIGN KEY(ContentLinkID) REFERENCES ContentStore.ContentLink (ContentLinkID);
ALTER TABLE ContentStore.ContentMetadata ADD CONSTRAINT FK_ContentStore_ContentMetadata_ContentStore_ContentLink_ContentLinkID FOREIGN KEY(ContentLinkID) REFERENCES ContentStore.ContentLink (ContentLinkID);