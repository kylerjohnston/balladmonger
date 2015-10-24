exclusions = ['CHAPTER (\d*|M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3}))\.*\n',
    'Chapter \d*\n', '^\d*\n',
    '\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}',
    '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\.?\n',
    '^[^\w\d\s]*\n', '^(CLOV|HAMM|NAGG|NELL)\s\([\w\s\d]*\):',
    '^(HAMM|NAGG|NELL|CLOV):', '^-\s',
    '^(Merryn|Lear|Hygd|Physician|Goneril|Cordeil|Gormflaith|The Younger Woman|The Elder Woman).*\.\n', '^Scene:.+\.\n', '^ACT I{0,3}V{0,1}\. Scene \w\.\n',
    '^Enter.*\.\n', '\[.*\n*.*\]', 'Exeunt\.'
    '(Kent|Glou|Edm|Lear|France|Bur|Corn|Alb|Edg|Cur|Old Man|Doct|Fool|Osw|Capt|Gent|Her|\d\. Serv|Gon|Reg|Cor|Knight)(\.+|,+)\s?\n?', 'THE \w+ BOOKE\n', 'OF THE\n',
    'HISTORIE OF ENGLAND\.\n', '^THE \w+ CHAPTER\.\n', '^\^\).*\n', '^\*\).*\n'
    ]
