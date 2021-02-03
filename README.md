***
<h1 align="center">GRANITE - GeneRic softwAre iNterface requIremenTs gEnerator</h1>

***

<p align="center">
<a href="https://www.codefactor.io/repository/github/thibfrgsgmz/granite/overview/main"><img src="https://www.codefactor.io/repository/github/thibfrgsgmz/granite/badge/main" alt="CodeFactor" /></a>
<a href="https://www.codacy.com/gh/ThibFrgsGmz/granite/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ThibFrgsGmz/granite&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/1240f67d2d0443b2adc4dd7ed49f6361"/></a>
<a href="https://frontend.code-inspector.com/project/18606/dashboard"><img src="https://www.code-inspector.com/project/18606/status/svg" alt="CodeInspector" /></a>
<a href="https://frontend.code-inspector.com/project/18606/dashboard"><img src="https://www.code-inspector.com/project/18606/score/svg" alt="CodeInspector" /></a>
</p>


<p align="center">
<a href="https://lgtm.com/projects/g/ThibFrgsGmz/granite/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/ThibFrgsGmz/granite.svg?logo=lgtm&logoWidth=18"/></a>
<a href="https://lgtm.com/projects/g/ThibFrgsGmz/granite/alerts/"><img alt="Total alerts" src="https://img.shields.io/lgtm/alerts/g/ThibFrgsGmz/granite.svg?logo=lgtm&logoWidth=18"/></a>

</p>

<p align="center">
<a href="https://deepsource.io/gh/ThibFrgsGmz/granite/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/ThibFrgsGmz/granite.svg/?label=active+issues&show_trend=true"/></a>
<a href="https://deepsource.io/gh/ThibFrgsGmz/granite/?ref=repository-badge" target="_blank"><img alt="DeepSource" title="DeepSource" src="https://deepsource.io/gh/ThibFrgsGmz/granite.svg/?label=resolved+issues&show_trend=true"/></a>
</p>
<p align="center">
  <a href="https://www.python.org/downloads/release/python-386/">
    <img src=
    "https://img.shields.io/badge/CODED%20IN-python%203-8.svg?&logo=python&style=for-the-badge&colorA=EAE8E8&colorB=3C25D6" 
    alt="Python" />
  </a>
  <a href=
    "https://code.visualstudio.com/">
    <img src=
    "https://img.shields.io/badge/MADE%20WITH-VISUAL%20STUDIO%20CODE-blue?&logo=visual-studio-code&style=for-the-badge" 
    alt="Python" />
  </a>
</p>

<p align="center">
  <a href=
  "https://google.com/v2/click/16413/119403?link=1227">
      <img src=
      "https://img.shields.io/badge/SOFTWARE-%20NOT%20MAINTAINED%20%E2%86%92-gray.svg?colorA=655BE1&colorB=4F44D6&style=for-the-badge"/>
  </a>
</p>

<p align="center">
  <a href="https://forthebadge.com">
    <img src=
    "https://forthebadge.com/images/badges/built-with-love.svg" 
    alt="BuildWithLove" />
  </a>
  <a href="https://forthebadge.com">
    <img src=
    "https://forthebadge.com/images/badges/built-by-developers.svg" 
    alt="BuildByDev" />
  </a>
</p>

<p align="center">
  <a href=
  "https://forthebadge.com">
    <img src=
    "https://forthebadge.com/images/badges/works-on-my-machine.svg" alt="BuildByDev" />
  </a>
</p>


<p align= "center"> GRANITE is a tool for generating an interface requirements document, along with the associated source code, from an abstract description of interfaces. These interface requirements are written in Markdown, the associated source code is in C language, and the abstract description is in XML language. 
This process makes it possible to put in phase at the level of the interfaces two softwares, an embedded software and an EGSE for example.
This avoids misunderstandings or software implementations that differ from the requirement document, whether by suppliers, systems integrators or the test facilities team. </p>


# Visual Studio Code Setup


> **1- Youtube Video : VS Code Presentation:
> https://www.youtube.com/watch?v=7EXd4_ttIuw&t=1s&ab_channel=MicrosoftVisualStudio**

## Virtual Environement (venv)

Some applications may require different versions of packages to work properly.
If we had to include all these different versions of packages in the same application or environment, we may have conflicts: iIt may be that some code doesn't work, something is broken.
That's why a virtual environment is recommended for Python developers.

### Create a Virtual Environment from the Terminal
Type the following command into the command line:

```py
py -3 -m venv .venv
```
- py is the short for Python
- -3 for the Python version we are going to use
- -m to say we are going to pass a module that we want to use
- venv is the short for Virtual Environment 
- .venv is the name of our Virtual Environement we want to use


Select **Yes** in the incoming Pop-up windows:
```
We noticed a new virtual environement has been created. Do you want to select it from the workspace folder ? 
```

### Activate the Virtual Environment inside the Terminal
Type in the command line:
```
.venv\Scripts\activate
```

## Setup environment
"pip install" the project in editable state to prefix the main folder at each importation

Install the high-level granite package using pip.
The trick is to use the -e flag during installation: this way it is installed in a changeable state, and all changes made to the .py files will be automatically included in the installed package.

In the root directory, run
```ps
pip install -e . 
```
(note the dot, it means "current directory")

You can also see that it is installed using:
```ps
pip freeze
```
Link: https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder?rq=1

## Troubleshooting
### Python was not found

```js
Error : Python was not found but can be installed from the Microsoft Store: https://go.microsoft.com/fwlink?linkID=208264
```
**Solution**

You don't have the command python installed into your PATH on Windows which is the default if you didn't get your copy of Python from the Windows Store. If you selected your Python interpreter in VS Code (look in the status bar), then I would disable/uninstall Code Runner. That way the Python extension is what provides the ability to run Python (the Play button will be green instead of white).

Link: https://stackoverflow.com/questions/60842487/python-was-not-found-but-can-be-installed-from-the-microsoft-store-march-2020

### Unable to load the file ...\Scripts\Activate.ps1

```js
Error : .venv\Scripts\activate : Impossible de charger le fichier 
C:\Users\FARGES\Documents\VS_Code\ML_ApplePrice\Venv\Scripts\Activate.ps1, car l’exécution de     
scripts est désactivée sur ce système. Pour plus d’informations, consultez about_Execution_Policies à l’adresse 
https://go.microsoft.com/fwlink/?LinkID=135170.
Au caractère Ligne:1 : 1
+ Venv\Scripts\activate
    + CategoryInfo          : Erreur de sécurité : (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess**
```

**Solution**

Open your PowerShell in as administrator and enter the following command:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
```

### RuntimeError: The current Numpy installation fails to pass a sanity check due to a bug in the windows runtime [duplicate]

```
RuntimeError: The current Numpy installation ('...\\venv\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime.
```

**Solution**

This error occurs when using python3.9 and numpy1.19.4 So uninstalling numpy1.19.4 and installing 1.19.3 will work.
The temporary solution is to use numpy 1.19.3.
```
(.venv) PS C:\Users\FARGES\Documents\VS_Code\ML_ApplePrice> pip install numpy==1.19.3
```
From this Microsoft thread https://developercommunity.visualstudio.com/content/problem/1207405/fmod-after-an-update-to-windows-2004-is-causing-a.html fix will be available around January 2021

Stackoverflow links :

1- https://stackoverflow.com/questions/64729944/runtimeerror-the-current-numpy-installation-fails-to-pass-a-sanity-check-due-to

2- https://stackoverflow.com/questions/64654805/how-do-you-fix-runtimeerror-package-fails-to-pass-a-sanity-check-for-numpy-an


# Study Case

> **Youtube Video of the Tutorial:https://www.youtube.com/watch?v=sAuGH1Kto2I&ab_channel=sentdex**

### **BeautifulSoup** 

Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

> Website: https://www.crummy.com/software/BeautifulSoup/

> GitHub: https://github.com/waylan/beautifulsoup

Install BeautifulSoup by typing in the command line of the Virtual Environment:

```
(Venv) PS C:\Users\FARGES\Documents\VS_Code\ML_ApplePrice> pip install bs4
```

### ERROR: bs4.FeatureNotFound

At the moment of executing the application the following error could appears:

```
File "c:/Users/FARGES/Documents/VS_Code/XmlScraping4ICDs/main.py", line 10, in <module>
    soup = bs.BeautifulSoup(source,'lxml')
  File "C:\Users\FARGES\Documents\VS_Code\XmlScraping4ICDs\__venv__\lib\site-packages\bs4\__init__.py", line 246, in __init__
    % ",".join(features))
bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
```

**Solution**

I suspect this is related to the parser BS will use to read HTML. Their document is here, but if you're like me (under OSX), you might be stuck with something that requires a bit of work:

You will notice that in the BS4 documentation page above they point out that by default BS4 will use the HTML parser built into Python. Assuming you are running OSX, the version of Python provided by Apple is 2.7.2 which is not forgiving for character formatting. I encountered the same problem, so I updated my version of Python to work around it. By doing this in a virtualenv, you minimize the disruption to other projects.

If you find it difficult, you can switch to the LXML parser :

`pip install lxml`



Links :

1- https://stackoverflow.com/questions/63404192/pip-install-tensorflow-cannot-find-file-called-client-load-reporting-filter-h

2- https://www.howtogeek.com/266621/how-to-make-windows-10-accept-file-paths-over-260-characters/
