CREATE TABLE CONTENTSTORE.CorrespondenceTemplate
( Id INTEGER GENERATED ALWAYS AS IDENTITY
    ,Identifier varchar(255)
    , CorrespondenceType varchar(100)
    , SubjectHeading varchar(255)
    , Template varchar(2000)
    , Version integer
    , IsLatest integer
    , IsActive integer
);

ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER Id SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER Identifier SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER CorrespondenceType SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER Template SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER Version SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER IsLatest SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceTemplate ALTER IsActive SET NOT NULL;

ALTER TABLE CONTENTSTORE.CorrespondenceTemplate
    ADD CONSTRAINT CORRESPONDENCE_TEMPLATE_PK PRIMARY KEY
        ( Id
            )
;
