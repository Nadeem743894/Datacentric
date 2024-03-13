# Correlation analysis 

Correlation analysis can verify whether relationships in pairwise scatter plots are statistically significant. It’s important
to note here that the default correlation analysis in most software will be looking for a straight-line relationship between 
two variables – i.e., the Pearson’s correlation coefficient. An absolute value of 1 suggests a perfect straight line fit 
between two variables with the positive showing the variables increase together and the negative showing one 
increases as the other decreases. A value of 0 does not necessarily mean there is no dependency, but that dependency 
cannot be described by a straight line. 


A more flexible correlation measure is given by the Spearman’s correlation that 
compares rank and so works with any monotonic relationship, but this will often require an argument to the function. 
Correlation analysis includes a p-value, a value <0.1 shows statistical significance to the given correlation, i.e., the 
correlation is unlikely to have occurred by chance. 


*Page created by LL - Mar 2024*