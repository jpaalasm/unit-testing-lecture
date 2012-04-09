
import numpy
import scipy.stats
import pylab


def two_tail_t_test(group_1_values, group_2_values):
    group_1_mean = numpy.mean(group_1_values)
    group_2_mean = numpy.mean(group_2_values)
    
    group_1_var = numpy.var(group_1_values)
    group_2_var = numpy.var(group_2_values)
    
    N1 = len(group_1_values)
    N2 = len(group_2_values)
    
    pooled_std = numpy.sqrt(((N1 - 1) * group_1_var + (N2 - 1) * group_2_var) / (N1 + N2 - 2))
    t_value = (group_1_mean - group_2_mean) / (pooled_std * numpy.sqrt(1.0 / N1 + 1.0 / N2))
    
    degrees_of_freedom = N1 + N2 - 2
    p_value = scipy.stats.t.sf(abs(t_value), degrees_of_freedom) * 2
    
    return p_value



def main():
    N = 50
    variance = 1.0
    
    mean_1 = 0.0
    mean_2 = 0.9
    
    group_1_values = scipy.stats.norm.rvs(mean_1, variance, size=N)
    group_2_values = scipy.stats.norm.rvs(mean_2, variance, size=N)
    
    p_value = two_tail_t_test(group_1_values, group_2_values)
    
    axes = pylab.subplots(2, 1, sharex=True)[1]
    
    axes[0].set_title("p=%.3f" % p_value)
    
    bins = numpy.linspace(-4, 4, 15)
    
    axes[0].hist(group_1_values, bins)
    axes[1].hist(group_2_values, bins)
    
    pylab.show()
    
    

if __name__ == "__main__":
    main()


