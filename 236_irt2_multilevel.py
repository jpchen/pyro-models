# model file: ../example-models/misc/irt/irt2_multilevel.stan
import torch
import pyro
import pyro.distributions as dist

def init_vector(name, dims=None):
    return pyro.sample(name, dist.Normal(torch.zeros(dims), 0.2 * torch.ones(dims)))



def validate_data_def(data):
    assert 'J' in data, 'variable not found in data: key=J'
    assert 'K' in data, 'variable not found in data: key=K'
    assert 'N' in data, 'variable not found in data: key=N'
    assert 'jj' in data, 'variable not found in data: key=jj'
    assert 'kk' in data, 'variable not found in data: key=kk'
    assert 'y' in data, 'variable not found in data: key=y'
    # initialize data
    J = data["J"]
    K = data["K"]
    N = data["N"]
    jj = data["jj"]
    kk = data["kk"]
    y = data["y"]

def init_params(data):
    params = {}
    # initialize data
    J = data["J"]
    K = data["K"]
    N = data["N"]
    jj = data["jj"]
    kk = data["kk"]
    y = data["y"]
    # assign init values for parameters
    params["delta"] = pyro.sample("delta"))
    params["alpha"] = pyro.sample("alpha", dims=(J)))
    params["beta"] = pyro.sample("beta", dims=(K)))
    params["log_gamma"] = pyro.sample("log_gamma", dims=(K)))
    params["sigma_alpha"] = pyro.sample("sigma_alpha", dist.Uniform(0))
    params["sigma_beta"] = pyro.sample("sigma_beta", dist.Uniform(0))
    params["sigma_gamma"] = pyro.sample("sigma_gamma", dist.Uniform(0))

    return params

def model(data, params):
    # initialize data
    J = data["J"]
    K = data["K"]
    N = data["N"]
    jj = data["jj"]
    kk = data["kk"]
    y = data["y"]
    
    # init parameters
    delta = params["delta"]
    alpha = params["alpha"]
    beta = params["beta"]
    log_gamma = params["log_gamma"]
    sigma_alpha = params["sigma_alpha"]
    sigma_beta = params["sigma_beta"]
    sigma_gamma = params["sigma_gamma"]
    # initialize transformed parameters
    # model block

    alpha =  _pyro_sample(alpha, "alpha", "normal", [0., sigma_alpha])
    beta =  _pyro_sample(beta, "beta", "normal", [0., sigma_beta])
    log_gamma =  _pyro_sample(log_gamma, "log_gamma", "normal", [0., sigma_gamma])
    delta =  _pyro_sample(delta, "delta", "cauchy", [0., 5])
    sigma_alpha =  _pyro_sample(sigma_alpha, "sigma_alpha", "cauchy", [0., 5])
    sigma_beta =  _pyro_sample(sigma_beta, "sigma_beta", "cauchy", [0., 5])
    sigma_gamma =  _pyro_sample(sigma_gamma, "sigma_gamma", "cauchy", [0., 5])
    for n in range(1, to_int(N) + 1):
        y[n - 1] =  _pyro_sample(_index_select(y, n - 1) , "y[%d]" % (to_int(n-1)), "bernoulli_logit", [(_call_func("exp", [_index_select(log_gamma, kk[n - 1] - 1) ]) * ((_index_select(alpha, jj[n - 1] - 1)  - _index_select(beta, kk[n - 1] - 1) ) + delta))], obs=_index_select(y, n - 1) )

