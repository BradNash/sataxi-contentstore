INSERT INTO contentstore.correspondencetemplate(identifier, correspondencetype, subjectheading, template, version, islatest, isactive)
VALUES ('MECHANICAL_REASON_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request to cancel deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Supplier:</th> <th>{{SUPPLIER}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('ASSET_CHANGE_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request to cancel deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Supplier:</th> <th>{{SUPPLIER}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('LEAD_REFERRAL_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for vehicle Finance</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th >{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Client ID no.:</th> <th>{{CLIENT_ID_NO}}</th> </tr> <tr> <th>Vehicle Description:</th> <th>{{VEHICLE_DESCRIPTION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('PAYMENT_ARRANGEMENT_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Alternate Contact No:</th> <th>{{ALTERNATE_CONTACT_NO}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('PASSENGER_LIABILITY_REQUEST_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('PREMIUM_REDUCTION_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('POLICY_DOCUMENT_REQUEST_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('TERRITORIAL_LETTER_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('NEW_CLAIM_REGISTRATION_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('CLAIM_FOLLOW_UP_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('3RD_PARTY_CLAIM_ENQUIRY_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('3RD_PARTY_CLAIM_REGISTRATION_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('3RD_PARTY_CLAIM_FOLLOW_UP_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('CLAIM_FOLLOW_UP_PRE_AUTH_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('CLAIM_FOLLOW_UP_POST_AUTH_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('TOWING_REQUEST_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('ACCIDENT_REPORT_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('NO_CLAIMS_LETTER_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('POLICY_CANCELLATION_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('POLICY_SUBSTITUTION_EMAIL', 'EMAIL', 'SA Taxi Query', '<!DOCTYPE html> <html> <head> <style> table { border-collapse: collapse; width: 100%; } tr { text-align: left; } </style> <title>{{TITLE}}</title> {% include "SATAX_EMAIL_HEADER_LATEST" %} <br /> </head> <body>To whom it may Concern<br /> <p>Please refer to Case no. {{CASE_NUMBER}} for a request for payment arrangement on deal number {{DEAL_NUMBER}}</p> <table> <tr> <th>Client Name:</th> <th>{{CLIENT_NAME}}</th> </tr> <tr> <th>Client Contact:</th> <th>{{CLIENT_CONTACT}}</th> </tr> <tr> <th>Chassis Number:</th> <th>{{CLIENT_NUMBER}}</th> </tr> <tr> <th>Engine Number:</th> <th>{{ENGINE_NUMBER}}</th> </tr> <tr> <th>Policy Number:</th> <th>{{POLICY_NUMBER}}</th> </tr> <tr> <th>Vehicle Registration:</th> <th>{{VEHICLE_REGISTRATION}}</th> </tr> </table> <br /> {{AGENT_NAME}}<br /> Customer Service Centre<br /> SA Taxi </body> <footer> {% include "SATAX_EMAIL_FOOTER_LATEST" %} </footer> </html>', 1, 1, 1),
       ('INSTALLMENT_CHANGE_SMS', 'SMS', NULL, 'SA Taxi: Dear {{FULLNAME}}, per your request the due date for the account {{ACCOUNT_NUMBER}} has been changed to the 1st of every month. Your next instalment of R {{AMOUNT}} is due on the {{DUE_DATE}}', 1, 1, 1),
       ('DEBIT_ORDER_ACTIVATION_SMS','SMS', NULL,'SA Taxi: Dear {{FULLNAME}}, per your request a debit order has been activated and will take effect from the {{DUE_DATE}} for R {{AMOUNT}}',1,1,1),
       ('DEBIT_ORDER_CANCELLATION_SMS','SMS', NULL,'SA Taxi: Dear {{FULLNAME}}, the debit order for account {{ACCOUNT_NUMBER}} has been cancelled. Your next installment of R {{AMOUNT}} is due on the {{DUE_DATE}}. For queries , please contact us on 0861829448',1,1,1),
       ('SETTLEMENT_QUOTATION_SMS','SMS', NULL,'SA Taxi: Dear {{FULLNAME}},settlement amount for account {{ACCOUNT_NUMBER}} is R{{AMOUNT}} is until {{DUE_DATE}}. If you pay this your contract comes to an end. Tracker and insurance will not be paid for.',1,1,1),
       ('MIDRAND_BRANCH_SMS','SMS', NULL,'Dear {{FULLNAME}},our Johannesburg branch address is:- 179 15th Road Randjespark Midrand     Our telephone number is 086-182-9448 -SA Taxi',1,1,1),
       ('CAPE_TOWN_BRANCH_SMS','SMS', NULL,'Dear {{FULLNAME}},our Cape Town branch address is:- Corner Main and Old Stanhope Road Claremont     Our telephone number is(021)674-5148 -SA Taxi',1,1,1),
       ('NELSPRUIT_BRANCH_SMS', 'SMS', NULL,'Dear {{FULLNAME}},our Nelspruit branch address is:- The Grove Shopping Centre Corner R40 White River Road and Gorge Street Riverside',1,1,1),
       ('DURBAN_BRANCH_SMS','SMS', NULL,'Dear {{FULLNAME}},our Durban branch address is:- 2945 Florida Road Level 2 West Wing Morningside Durban  Our telephone number is (031)752-6872 -SA taxi',1,1,1),
       ('POLOKWANE_BRANCH_SMS','SMS', NULL,'Dear {{FULLNAME}},our Polokwane branch address is:- 2945XXXXXXXXX XXXXXXXXXXXX XXXXXXXXXXXX Polokwane       Our telephone number is (000)000-0000 -SA Taxi',1,1,1),
       ('SERVICE_CAMPAIGN_SMS','SMS', NULL,'Dear {{FULLNAME}},we have attempted to contact you regarding a campaign that SA Taxi is running. Kindly contact us back on:- Telephone Number :  (011)550-9640',1,1,1),
       ('TEST_SMS','SMS', NULL,'Hello {{Name}}. This is a test message from our Automated Service.',1,1,1),
       ('ABSA_BANK_SMS','SMS', NULL,'SA Taxi: Our banking details at ABSA for your payment is:- Account Number  4080665404  Branch Code  632005  Please use {{ACCOUNT_NUMBER}} as your reference',1,1,1),
       ('NEDBANK_BANK_SMS','SMS', NULL,'SA Taxi: Our banking details at Nedbank for your payment is:- Account Number  1043477160  Branch Code  019593  Please use {{ACCOUNT_NUMBER}} as your reference',1,1,1),
       ('FNB_BANK_SMS','SMS', NULL,'SA Taxi: Our banking details at FNB for your payment is:- Account Number  6239669323  Branch Code  255805  Please use {{ACCOUNT_NUMBER}} as your reference',1,1,1),
       ('STD_BANK_BANK_SMS','SMS', NULL,'SA Taxi: Our banking details at Standard Bank for your payment is:- Account Number  00300463499  Branch Code  007205  Please use {{ACCOUNT_NUMBER}} as your reference',1,1,1);