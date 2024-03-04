# The impacts of unrepresentative data

## Samples v populations - what is lack of representation?
From a statistical perspective, any data analysis relies on the sample of data providing a suitable representation of the population about which you are trying to provide insights. A perfect representation of the data population is often not possible and so it is important to understand any bias or other limitations that might result from an imperfect representation of the data population. In the worst cases, any results can be rendered useless in terms of actionable insights (although this might not be realised). In many cases, however, the data can be sufficient for drawing insights as long as the conditions under which the insights can be interpreted is understood. Sometimes the data is simply not suitable for the required insights and the scope of the project may need to change. 

## Why you might have data that is not representative of a population? 

There are many reasons why data may lack representation of what you want to make insights into. Sometimes this is obvious but sometimes it can go unnoticed. It is important to carefully define what insights are required and what the data is required to represent. 

Some examples of unrepresentative data are given here: 

* **In defect classification, not all defects are present in the data.**
    * A possible solution to this is to produce a stratified data design such that the data is purposely acquired so that it contains a specific amount of each defect. Another possible solution is to produce synthetic data (making sure this is representative). If this cannot be achieved then the analysis will be limited to comparing defect-free and defect. 
    * This is true for any image classification. To classify a particular object the training data must contain it. 

* **Not enough data is available.**
    * For some AI methods, particularly deep learning, there is not enough data to train the model sufficiently for any insight. Synthetic data can help but a common fix is transfer learning where already existing big data is used to inform early layers of AI models. In either case, it's possible that the data is not representative and insights not useful. Hold-out test sets are required to test whether the model can represent different objects or data streams. 
    * Another possible solution is to choose an analysis technique that is less reliant on big data. 

* **The data is collected during a limited time frame.**
    * Data collection can be tricky when limited resources are available and this often leads to data collection taking place over a limited period of time. This can be fine so long as that limited period of time is representative of all time. For example, does the ambient temperature change or the background humidity and could this affect the outcome. In some cases, this might be fine when considering trends or changes in data rather than the raw values but if the trend or responses depend on underlying conditions then samples of data must be collected for a selection of conditions. 

* **The process is too stable or consistent.**
    * When the aim is to do process control or improve some processes it may happen that the data is collected during a particularly stable time and no errors or potential improvement opportunities occur. In some cases, it might be necessary to design faults into the process such that the data is known to contain certain faults. In some cases, the lack of failures may be information enough. 



*Page created by LL - Mar 2024*