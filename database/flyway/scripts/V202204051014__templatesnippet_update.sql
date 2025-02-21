DELETE FROM CONTENTSTORE.TEMPLATESNIPPETS;

INSERT INTO contentstore.templatesnippets(templateidentifier, TemplateType, template, islatest, version)
VALUES ('SATAX_EMAIL_HEADER', 'HEADER', '<h1>SaTaxi</h1>', 0, 1),
       ('SATAX_EMAIL_FOOTER', 'FOOTER', '<h1>Disclaimer | All Rights Reserved</h1>', 0, 1),
       ('SATAX_EMAIL_HEADER', 'HEADER', '<h2>SaTaxi</h2>', 1, 2),
       ('SATAX_EMAIL_FOOTER', 'FOOTER', '<h2>Disclaimer | All Rights Reserved</h2>', 1, 2);
