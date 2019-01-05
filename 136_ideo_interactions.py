# model file: ../example-models/ARM/Ch.10/ideo_interactions.stan
import torch
import pyro
import pyro.distributions as dist

def init_vector(name, dims=None):
    return pyro.sample(name, dist.Normal(torch.zeros(dims), 0.2 * torch.ones(dims)))



def validate_data_def(data):
    assert 'N' in data, 'variable not found in data: key=N'
    assert 'party' in data, 'variable not found in data: key=party'
    assert 'score1' in data, 'variable not found in data: key=score1'
    assert 'x' in data, 'variable not found in data: key=x'
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]

def transformed_data(data):
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]
    inter = init_vector("inter", dims=(N)) # vector
    inter = _pyro_assign(inter, _call_func("elt_multiply", [party,x]))
    data["inter"] = inter

def init_params(data):
    params = {}
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]
    # initialize transformed data
    inter = data["inter"]
    # assign init values for parameters
    params["beta"] = init_vector("beta", dims=(4)) # vector
    params["sigma"] = pyro.sample("sigma", dist.Uniform(0))

    return params

def model(data, params):
    # initialize data
    N = data["N"]
    party = data["party"]
    score1 = data["score1"]
    x = data["x"]
    # initialize transformed data
    inter = data["inter"]
    
    # init parameters
    beta = params["beta"]
    sigma = params["sigma"]
    # initialize transformed parameters
    # model block

    score1 =  _pyro_sample(score1, "score1", "normal", [_call_func("add", [_call_func("add", [_call_func("add", [_index_select(beta, 1 - 1) ,_call_func("multiply", [_index_select(beta, 2 - 1) ,party])]),_call_func("multiply", [_index_select(beta, 3 - 1) ,x])]),_call_func("multiply", [_index_select(beta, 4 - 1) ,inter])]), sigma], obs=score1)

