CREATE TABLE CONTENTSTORE.TemplateSnippets
( Id INTEGER GENERATED ALWAYS AS IDENTITY
    , TemplateIdentifier varchar(255)
    , Template varchar(2000)
    , TemplateType varchar(255)
    , IsLatest integer
    , Version integer
);

ALTER TABLE CONTENTSTORE.TemplateSnippets ALTER Id SET NOT NULL;
ALTER TABLE CONTENTSTORE.TemplateSnippets ALTER TemplateIdentifier SET NOT NULL;
ALTER TABLE CONTENTSTORE.TemplateSnippets ALTER Template SET NOT NULL;
ALTER TABLE CONTENTSTORE.TemplateSnippets ALTER TemplateType SET NOT NULL;
ALTER TABLE CONTENTSTORE.TemplateSnippets ALTER IsLatest SET NOT NULL;
ALTER TABLE CONTENTSTORE.TemplateSnippets ALTER Version SET NOT NULL;

ALTER TABLE CONTENTSTORE.TemplateSnippets
    ADD CONSTRAINT TEMPLATE_SNIPPETS_PK PRIMARY KEY
        ( Id
            )
;
