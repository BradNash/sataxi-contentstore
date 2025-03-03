CREATE TABLE CONTENTSTORE.CorrespondenceEvent
( Id INTEGER GENERATED ALWAYS AS IDENTITY
    ,EventType varchar(255)
    , Identifier varchar(255)
);



ALTER TABLE CONTENTSTORE.CorrespondenceEvent ALTER Id SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceEvent ALTER EventType SET NOT NULL;
ALTER TABLE CONTENTSTORE.CorrespondenceEvent ALTER Identifier SET NOT NULL;

ALTER TABLE CONTENTSTORE.CorrespondenceEvent
    ADD CONSTRAINT CORRESPONDENCE_EVENT_PK PRIMARY KEY
        ( Id
            )
;

ALTER TABLE CONTENTSTORE.CorrespondenceEvent
    ADD CONSTRAINT CORRESPONDENCE_EVENT_FK01 FOREIGN KEY
        ( Id
            ) REFERENCES CONTENTSTORE.CorrespondenceTemplate MATCH FULL
;
