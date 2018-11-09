#from equivalent_rep import *
#from gurobi_model import *
#from reading import *
import cplex

for p in range(1,9):
    for v in range(0,10):
        for n in range(5,15,5):
  
            cpx_ori = cplex.Cplex('ori-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            cpx_dia = cplex.Cplex('dia-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            cpx_lin = cplex.Cplex('lin-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            cpx_pos = cplex.Cplex('pos-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            cpx_neg = cplex.Cplex('neg-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            cpx_tri = cplex.Cplex('tri-n''%s''p''%s''v''%s''.lp' % (n, p, v))

            cpx_ori.set_log_stream(None)
            cpx_ori.set_error_stream(None)
            cpx_ori.set_warning_stream(None)
            cpx_ori.set_results_stream(None)

            cpx_dia.set_log_stream(None)
            cpx_dia.set_error_stream(None)
            cpx_dia.set_warning_stream(None)
            cpx_dia.set_results_stream(None)

            cpx_lin.set_log_stream(None)
            cpx_lin.set_error_stream(None)
            cpx_lin.set_warning_stream(None)
            cpx_lin.set_results_stream(None)

            cpx_pos.set_log_stream(None)
            cpx_pos.set_error_stream(None)
            cpx_pos.set_warning_stream(None)
            cpx_pos.set_results_stream(None)

            cpx_neg.set_log_stream(None)
            cpx_neg.set_error_stream(None)
            cpx_neg.set_warning_stream(None)
            cpx_neg.set_results_stream(None)

            cpx_tri.set_log_stream(None)
            cpx_tri.set_error_stream(None)
            cpx_tri.set_warning_stream(None)
            cpx_tri.set_results_stream(None)

            cpx_ori.parameters.timelimit.set(10800.0)
            cpx_dia.parameters.timelimit.set(10800.0)
            cpx_lin.parameters.timelimit.set(10800.0)
            cpx_pos.parameters.timelimit.set(10800.0)
            cpx_neg.parameters.timelimit.set(10800.0)
            cpx_tri.parameters.timelimit.set(10800.0)

            t = cpx_ori.get_time()
            cpx_ori.solve()
            t_ori = cpx_ori.get_time() - t
            z_ori = cpx_ori.solution.get_objective_value()

            t = cpx_dia.get_time()
            cpx_dia.solve()
            t_dia = cpx_dia.get_time() - t
            z_dia = cpx_dia.solution.get_objective_value()

            t = cpx_lin.get_time()
            cpx_lin.solve()
            t_lin = cpx_lin.get_time() - t
            z_lin = cpx_lin.solution.get_objective_value()

            t = cpx_pos.get_time()
            cpx_pos.solve()
            t_pos = cpx_pos.get_time() - t
            z_pos = cpx_pos.solution.get_objective_value()

            t = cpx_neg.get_time()
            cpx_neg.solve()
            t_neg = cpx_neg.get_time() - t
            z_neg = cpx_neg.solution.get_objective_value()

            t = cpx_tri.get_time()
            cpx_tri.solve()
            t_tri = cpx_tri.get_time() - t
            z_tri = cpx_tri.solution.get_objective_value()

            z = min(z_ori,z_dia,z_lin,z_pos,z_neg,z_tri)
            z_test = 0
            if (z_ori == z) and (z_dia == z) and (z_lin == z) and (z_pos == z) and (z_neg == z) and (z_tri == z):
                z_test = 1
            else:
                z_test = 0
                    
            with open('_______Results.txt', 'a') as the_file:
                the_file.write('%s'' qap-n''%s''p''%s''v''%s %s %s %s %s %s %s %s %s %s %s %s %s %s\n' % (z_test, n, p, v, n, z_ori, z_dia, z_lin, z_pos, z_neg, z_tri, t_ori, t_dia, t_lin, t_pos, t_neg, t_tri))

            #print("Objective value = ",z_ori)
            #print("Time elapsed = ", t_ori)
            #print("Objective value = ", z_dia)
            #print("Time elapsed = ", t_dia)
            #print("Objective value = ", z_lin)
            #print("Time elapsed = ", t_lin)
            #print("Objective value = ", z_pos)
            #print("Time elapsed = ", t_pos)
            #print("Objective value = ", z_neg)
            #print("Time elapsed = ", t_neg)
            #print("Objective value = ", z_tri)
            #print("Time elapsed = ", t_tri)
