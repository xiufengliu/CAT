# CAT 

### 1. Discription

**CAT** is an ready-to-use tool for studying climate change adaptation using behavioral economic. It was built based on[ oTree ](https://www.otree.org/ " oTree "), a framework for  behavioral experiments in economics, market research, psychology, and related fields. The CAT consists of seven treatment apps (incl. *Control, Ambiguity, Loss, Myopia, Coordination, Ambigious Coordination, and Communication*), and a survey app. 

### 2. Installation
The installaton procudure includes the followings:
- Install the [ oTree ](http- s://www.otree.org/ " oTree "). The guidline of installation of oTree can be found at [here](http://otree.readthedocs.io/en/latest/ "here"). 
- Copy all the apps of CAT to the directory of oTree. 
- Configure database connection, user account, and sessions for experiments in the file *setting.py *
- Since a speical *glyphicons* icon (flooded home) is used, the [glyph patch](https://github.com/xiufengliu/CAT/raw/master/glphy.tar.gz "glyph patch") should be extracted to the otree core static directory, e.g., for oTree in python3.5, 
` /usr/local/lib/python3.5/dist-packages/otree/static` , then add the line `<link rel="stylesheet" href="{% static 'glyph/css/glyphicons.css' %}">` to the file `/usr/local/lib/python3.5/dist-packages/otree/templates/otree/includes/InternalStyles.html`


### 3. Online demo
**TODO**: Setting up in google cloud 

### 4. Experimental manual
- The user manual can be found [here](https://github.com/xiufengliu/CAT/blob/master/doc/Script.pdf "here")
- The pilot experimental instruction can be found at [here](https://github.com/xiufengliu/CAT/blob/master/doc/Instructions.pdf "here")


