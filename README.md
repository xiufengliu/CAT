# CAT 

### 1. Description

**CAT** is a ready-to-use tool for studying climate change adaptation using behavioral economic. It was built based on[ oTree ](https://www.otree.org/ " oTree "), a framework for behavioral experiments in economics, market research, psychology, and related fields. The CAT consists of seven treatment apps (incl. *Control, Ambiguity, Loss, Myopia, Coordination, Ambiguous Coordination, and Communication*), and a survey app. 

### 2. Installation
The installation procudure includes the followings:
- Install the [ oTree 1.3.9 ](http- s://www.otree.org/ " oTree "). The guidline of installation of oTree can be found at [here](http://otree.readthedocs.io/en/latest/ "here"). 
- Copy all the apps of CAT to the directory of oTree. 
- Configure database connection, user account, and sessions for experiments in the file *setting.py *
- Since a speical *glyphicons* icon (flooded home) is used, the [glyph patch](https://github.com/xiufengliu/CAT/raw/master/glphy.tar.gz "glyph patch") should be extracted to the otree core static directory, e.g., for oTree in python3.5, 
` /usr/local/lib/python3.5/dist-packages/otree/static` , then add the line `<link rel="stylesheet" href="{% static 'glyph/css/glyphicons.css' %}">` to the file `/usr/local/lib/python3.5/dist-packages/otree/templates/otree/includes/InternalStyles.html`


### 3. Online demo
[Demo](https://otree.scicloud.site/demo/ "Demo")

### 4. Experimental manual
- The user manual can be found [here](https://github.com/xiufengliu/CAT/blob/master/doc/Script.pdf "here")
- The pilot experimental instruction can be found at [here](https://github.com/xiufengliu/CAT/blob/master/doc/Instructions.pdf "here")

### 5. Publication
- von Bülow, C. W., & Liu, X. (2020). Ready-Made oTree Applications for the Study of Climate Change Adaptation Behavior. Journal of Behavioral and Experimental Economics, 101590.  [[PDF]](https://www.sciencedirect.com/science/article/pii/S2214804320301257?dgcid=author "PDF")

