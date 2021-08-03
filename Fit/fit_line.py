import os
import numpy as np
from scipy import special
from matplotlib import pyplot as plt


def curve_fit(data, order=2):
    """
    curve fit based on least squares method

    Parameters
    ----------

    data  : input data, whoes row is feature and col is the number of data.

    order : the order to fit.

    """
    assert order > 0, "the order is not zero and negative!"
    assert data.shape[0] == order, " the feature of data must equal to order"
    assert data.shape[1] > order, " The number of sample points is too small "
    A = np.vander(data[0, :], order)
    b = data[1, :][:, None]
    b = np.dot(A.T, b)
    A = np.dot(A.T, A)
    return np.linalg.solve(A, b)

def line_fit_ransac(data, param):
    """
    linear fitting based on ransac 

    Parameters
    ----------

    data  : input data, whoes row is feature and col is the number of data.

    param :the parameters for ransac.


    Example
    ----------
    noise=np.random.normal(0.0,1.0,100)
    data=np.linspace(1, 100, 100, dtype=float)
    data=np.vstack((data,data))
    data[1,:]=data[1,:]+noise
    params = {'threshold_distance': 0.4,
          'inner_ratio': .95,
          'max_inner_nums': -1
          }
    inner_index, line_coefficients_ransac = line_fit_ransac(data,params)
    
    """

    line_coefficients = []
    # step1 judge whether the number of the data is bigger than the number of the minimum points of the model
    max_inner_nums = np.copy(param['max_inner_nums'])
    sample_nums = 2
    size_data = data.shape[1]
    assert size_data >= sample_nums, " The number of sample points is too small "

    # step2 compute the max iterations
    max_iteration = np.longlong(special.comb(size_data, sample_nums))
    iterations = np.copy(max_iteration)
    for i in range(iterations):
        # step3 random pick the minimum points of the model
        minimum_model_index = np.random.randint(0, size_data, sample_nums)
        point1 = data[:,minimum_model_index[0]][:, None]
        point2 = data[:,minimum_model_index[1]][:, None]

    # step4 The direction vector of the line
        vector_uv = np.array((point2-point1))
        print(vector_uv.shape)
        if(np.all(vector_uv == 0)):
            continue
        if(vector_uv[0] == 0):
            distance = abs((data[0, :] - point1[0, :]))
        else:
            vector_uv_temp=vector_uv[::-1] 
            vector_uv_temp[0]=-vector_uv_temp[0]
            distance = abs(((data - point1).T).dot(vector_uv_temp)) / \
                np.linalg.norm(vector_uv, axis=0)

    # step5 compute the probability of inner point and update the interations
        inner_index = distance < param['threshold_distance']
        inner_nums = np.sum(inner_index == True)
        inner_probability = inner_nums / size_data
        if(inner_nums > max_inner_nums):
            max_inner_nums = inner_nums
            iterations = np.log(1-inner_probability) / \
                np.log(1-pow(inner_probability, sample_nums))
            if(vector_uv[0] == 0):
                line_coefficients = np.array([0, 0, point1[0, 0]])
            else:
                line_coefficients = np.array([vector_uv[1]/vector_uv[0],point1[1]-vector_uv[1]/vector_uv[0]*point1[0]])
        if(inner_probability > param['inner_ratio']):
            break
    print("iterations:", iterations)

    # step6 linear fitting based on the least square method
    index = np.argwhere(inner_index == True)
    line_coefficients_ransac = curve_fit(data[:,index[:,0]],order=2)
    if(line_coefficients[1] < 0):
        line_coefficients = - np.asarray(line_coefficients)
    return inner_index, line_coefficients_ransac

if __name__ == '__main__':
    noise=np.random.normal(0.0,1.0,100)
    data=np.linspace(1, 100, 100, dtype=float)
    data=np.vstack((data,data))
    data[1,:]=data[1,:]+noise
    plt.figure()
    plt.plot(data[0,:],data[1,:])
    params = {'threshold_distance': 0.4,
          'inner_ratio': .95,
          'max_inner_nums': -1
          }
    inner_index, line_coefficients_ransac = line_fit_ransac(data,params)
    y=data[0,:]*line_coefficients_ransac[0]+line_coefficients_ransac[1]
    plt.plot(data[0,:],y,'r')
    plt.show()