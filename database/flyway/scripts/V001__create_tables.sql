CREATE TABLE ContentStore.ContentData(
	ContentDataID BIGSERIAL,
	ContentLinkID bigint NOT NULL,
	ContentData bytea NOT NULL,
	ContentLength int NOT NULL,
	UsrID varchar(64) NOT NULL,
	TmStamp timestamp NOT NULL,
    CONSTRAINT PK_ContentStore_ContentData PRIMARY KEY (ContentDataID)
);
CREATE TABLE ContentStore.ContentLink(
	ContentLinkID BIGSERIAL,
	ContentType smallint NOT NULL,
	SourceType smallint NOT NULL,
	SourceID varchar(64) NULL,
	CreatedDate timestamp NOT NULL,
	LetterTemplate varchar(128) NULL,
	UsrID varchar(64) NOT NULL,
	TmStamp timestamp NOT NULL,
    CONSTRAINT PK_ContentStore_ContentLink PRIMARY KEY (ContentLinkID)
);
CREATE TABLE ContentStore.ContentMetadata(
	MetaDataID BIGSERIAL,
	ContentLinkID bigint NOT NULL,
	MetaType varchar(32) NOT NULL,
	MetaValue varchar(128) NOT NULL,
	UsrID varchar(64) NOT NULL,
	TmStamp timestamp NOT NULL,
    CONSTRAINT PK_ContentStore_ContentMetadata PRIMARY KEY (MetaDataID)
);