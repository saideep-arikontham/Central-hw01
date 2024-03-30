Building on the random-number generation exercise that we worked on in class, 
create a graphic to demonstrate Equation 3.7 in ISL.
Use pseudo-random numbers from a uniform distribution on the interval [0,1),
for which the variance should should be 1/12.
And investigate the dependence on the number of samples used to estimate 
the standard error (e.g., try 10, 100 and 1000).

IMPORTANT: use the formatting and repo layout (with a Makefile) in [git-intro](https://github.com/ds5110/git-intro).


### Solution:

There are three python files in the src folder. The "readit.py" file has a function to generate pseudo random uniform numbers which will be used in the other two python files. The result images are present in the figs folder.

##### estimate_mean_graphs.py:

- An array of size (1000,50) (n=1000 rows) is taken and mean is calculated for each of the records for each array. Therefore we have a result of 1000 means where each is an estimate mean. This array of 1000 estimate means will be in a normal distribution. And when you average these 1000 values, you get a value which is closer to the actual mean 0.5. The resultant probability density is represented in the [n_means_density_plot image in figs folder](https://github.com/ds5110/hw01-central-Saideep-18/blob/main/figs/n_means_density_plot.png)



- I have also taken n=10 and n=100 as well but when plotted, the distribution is not a normal distribution. The average of n estimate means is not closer to the actual mean when compared with the average mean on n=1000 records.


##### std_error.py

- For variance of single estimate mean, I have taken arrays of fixed samples but different number of features (=10, =100, =1000). In each case after calculating the variance of each sample, we will have 1000 variance values as an array. But as the number of features increases, the mean of the variance is closer to the variance of the [0,1) i.e., 1/12.
- The standard error, which is variance/n would then be 0.00008333 for the entire 2d array data when rows=1000 and features=1000. The line plot indicating the change of average of variance when features=10, features=100 and features=1000 is represented in the [variance image in the figs folder](https://github.com/ds5110/hw01-central-Saideep-18/blob/main/figs/variance.png)




