<img src="Images/goat-vaccination.jpg" width="100%" height="100%">

## Flatiron GOATs Vaccination Prediction
Data sourced from [DataDriven](https://www.drivendata.org/competitions/66/flu-shot-learning/page/210/)

**Authors**:

- [Danielle Rossman](https://github.com/dmrossm)
- [Matthew Turner](https://github.com/austint1121)
- [Hyunwook Paul Shin](https://github.com/hps1795)


## Overview

 
***
## Business Problem
The mayor of Goat city  is ordering Covid vaccines, and is fully aware that not everyone will choose to get vaccinated. Goat city wants to know how many Covid vaccines they should be ordering. We want to show them that using a survey to predict if a person will get a vaccine is a valid way of estimating how many vaccines to order.

***

## Data
**Data sourced from [DataDriven](https://www.drivendata.org/competitions/66/flu-shot-learning/page/210/)**

Datadriven's description of the dataset says:

>Vaccines for H1N1 were first publicly available in the United States in October 2009, when the United States government began a vaccination campaign. We will look at data from the National 2009 H1N1 Flu Survey collected to monitor vaccination rates during that campaign. This phone survey asked people whether they had received H1N1 and seasonal flu vaccines, in conjunction with information they shared about their lives, opinions, and behaviors. A better understanding of how these characteristics have been associated with personal vaccination patterns may provide guidance for future public health efforts.

Full documentation of the dataset can be found on the [CDC website]((https://www.cdc.gov/nchs/nis/data_files_h1n1.htm))
***

## Methods
### Preproccessing 
For the preproccessing, all of the columns are categorical, however, some of them are numerical, and some of them are strings. We will want to handle these these columns differently when imputing missing values.

- **Numerical Categories**
    - Use Sklearn's Iterative Imputer to fill in the missing values
- **String Categories**
    - Fill missing values with a new value: 'unknown'
    - One hot encode the results
- **Categories with more then 10 unique categories**
  - We will frequency code these instead, so we don't have an overwhelming amount of columns in the dataframe.

***

### Modeling

## Results
***

## Conclusions
(can be used here and/or in final notebook)
- Our final model was able to predict the number of vaccines used during the 2009 H1N1 epidemic (for the sample provided), with an error that was equivalent to a total dollar cost of ~$21,000. Given the average budget of most local public health departments this is a highly tolerable error in terms of monetary cost. 
- Of note, in choosing to minimize fatalities, we thus prioritized life over monetary loss. Also of note, underestimating the number of needed vaccines would not only have cost more lives, but would have created additional monetary burden in the form of hospital bills for unvaccinated/infected patients. As hospital costs are exponentially greater than the cost of vaccines, we feel that our choice to design a model that restricted the chance of those wishing to be vaccinated from encountering a vaccine shortage was optimal.
- We now feel, that given the ~80% accuracy of this model, we can feel confident in advising Goat City to conduct an updated survey, targeting the same demographic features, but shifting the survey questions regarding vaccines and likelihood of illness to focus on the current COVID-19 epidemic. We would then advise Goat City to use the model we have created with the provided H1N1 survey data to now predict the number of vaccines needed for COVID-19. 
- Once again, because we have built a model that will tolerate overestimation of vaccines needed far more readly than underestimation, we feel that in using this model to predict vaccines needed, there is relatively low likelihood of encountering vaccine shortage. This will position optimally Goat City to slow and hopefully halt local spread of infection, while also giving its health department vital knowledge on how many individuals may need to be swayed, via public health education campaigns and extremely convenient vaccine clinics, to choose to become vaccinated.


***

## Information

Please review our full analysis in [our Jupyter Notebook](https://github.com/austint1121/Flatiron_GOATS_Vaccination_Prediction/blob/main/Final%20Notebook.ipynb)
or our [presentation](https://github.com/austint1121/Flatiron_GOATS_Vaccination_Prediction/main/presentation.pdf)

## Repository Structure

```
├── Notebooks                           <- Directory containing individual group members' notebooks
│   ├── Danielle                  
│   │   └── ...
│   ├── Matthew                  
│   │   └── ...
│   └── Paul                  
│       └── ...
│
├── Images                              <- Folder containing graphs and images from notebooks and presentation
│   └── ...
├── presentation.pdf                    <- PDF version of project presentation
├── Final Notebook.ipynb                <- Narrative documentation of project in Jupyter notebook
└── README.md                           <- Top-level README 
              

``` 
