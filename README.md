## An Empirical Evaluation of GitHub Copilot's Code Generation
*Requirements:*
- [python-decouple package](https://pypi.org/project/python-decouple/) (Can be installed with Pyhton Package Installer, pip using command: *pip install python-decouple*)
- [openai package](https://pypi.org/project/openai/) (Can be installed with Pyhton Package Installer, pip using command: *pip install openai*)
- [Sonarqube API](https://docs.sonarqube.org/latest/extend/web-api/) and [OpenAI API](https://openai.com/api/) keys

*Experiment Steps:*
- Create an .env file using .env.example file for Sonarqube API and OpenAI API keys
- Run [preparation.py](https://github.com/ease22-sub39/An-Empirical-Evaluation-of-GitHub-Copilot-s-Code-Generation/blob/main/preparation.py)
  --> *python preparation.py*
- Generate code manually using the prompt_i.py files under the code-generation folder
- Run [experiment.py](https://github.com/ease22-sub39/An-Empirical-Evaluation-of-GitHub-Copilot-s-Code-Generation/blob/main/experiment.py)
 --> *python experiment.py*
##
Our result tables can be seen [here](https://github.com/ease22-sub39/An-Empirical-Evaluation-of-GitHub-Copilot-s-Code-Generation/blob/main/misc/Copilot_Results.pdf) (pdf format) and [here](https://github.com/ease22-sub39/An-Empirical-Evaluation-of-GitHub-Copilot-s-Code-Generation/blob/main/misc/Copilot_Results.xlsx) (xlsx format).

The list of the articles on GitHub Copilot we checked can be seen [here](https://github.com/ease22-sub39/An-Empirical-Evaluation-of-GitHub-Copilot-s-Code-Generation/blob/main/misc/article_names_and_links.pdf).
