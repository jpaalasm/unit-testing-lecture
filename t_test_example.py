
import numpy
import scipy.stats
import pylab


def two_tail_t_test(group_1_values, group_2_values):
    group_1_mean = numpy.mean(group_1_values)
    group_2_mean = numpy.mean(group_2_values)
    
    group_1_var = numpy.var(group_1_values, ddof=1)
    group_2_var = numpy.var(group_2_values, ddof=1)
    
    N1 = len(group_1_values)
    N2 = len(group_2_values)
    
    pooled_std = numpy.sqrt(((N1 - 1) * group_1_var + (N2 - 1) * group_2_var) / float(N1 + N2 - 2))
    t_value = (group_1_mean - group_2_mean) / (pooled_std * numpy.sqrt(1.0 / N1 + 1.0 / N2))
    
    degrees_of_freedom = N1 + N2 - 2
    p_value = scipy.stats.t.sf(abs(t_value), degrees_of_freedom) * 2
    
    return p_value


def main():
    N1 = 200
    N2 = 50
    variance = 1.0
    
    mean_1 = 0.0
    mean_2 = 0.4
    
    numpy.random.seed(1)
    group_1_values = scipy.stats.norm.rvs(mean_1, variance, size=N1)
    group_2_values = scipy.stats.norm.rvs(mean_2, variance, size=N2)
    
    p_value = two_tail_t_test(group_1_values, group_2_values)
    
    p_value2 = scipy.stats.ttest_ind(group_1_values, group_2_values)[1]
    
    print p_value, p_value2
    
    axes = pylab.subplots(3, 1, sharex=True)[1]
    
    axes[0].set_title("p=%.9f" % p_value)
    
    bins = numpy.linspace(-4, 4, 15)
    
    axes[0].vlines(group_1_values, 0, 1, color="red")
    axes[0].vlines(group_2_values, -1, 0, color="blue")
    axes[1].hist(group_1_values, bins, color="red")
    axes[2].hist(group_2_values, bins, color="blue")
    
    pylab.show()


if __name__ == "__main__":
    main()
