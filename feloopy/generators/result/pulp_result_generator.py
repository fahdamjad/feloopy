import pulp as pulp_interface

def Get(model_object, result, input1, input2=None):

   directions = +1 if input1[1][input1[2]]=='min' else -1
   input1 = input1[0]

   match input1:

    case 'variable':
        return input2.varValue
    
    case 'status':
        return pulp_interface.LpStatus[result[0]]
         
    case 'objective':
        return directions*pulp_interface.value(model_object.objective)

    case 'time':
        return (result[1][1]-result[1][0])