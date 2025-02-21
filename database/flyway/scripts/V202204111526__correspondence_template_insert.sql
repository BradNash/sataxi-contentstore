INSERT INTO contentstore.correspondencetemplate(identifier, correspondencetype, subjectheading, template, version, islatest, isactive)
VALUES
    ('TEST_EMAIL','EMAIL', 'SA Taxi Test E-Mail for {{Name}}','Hello {{Name}}. This is a test message from our Automated Service. <img src="cid:(cs://userSpecifiedKey=CAPTAIN_AWESOME)">',1,1,1);
