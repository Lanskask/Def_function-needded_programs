def from_file_plot_3d(var, variable_name, i): # file_name
    import matplotlib.pyplot as plt
    import numpy as np
    import re
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm

    __author__ = 'Alena'

    # ----- Uncomment -----
    cwd = os.getcwd()
    dats_file_path = "/Graphs/DATs_"+variable_name+'_'+str(i)+'_'+str(var)
    os.chdir( os.getcwd()+ dats_file_path )
    # ---------------------

    def file_len(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i - 2

    file_name = "field_c.dat"
    input_file = open(file_name)

    regex = re.compile('  | ')

    n = file_len(file_name)
    matrix = np.zeros((n, n))
    j = 0
    for line in input_file:
        if j == 81: break
        if len(regex.split(line)) >= n:
            matrix[j, :] = regex.split(line)[2:]
            j += 1

    surface_fig = plt.figure()

    print(matrix)

    now_time = strftime("%d-%H.%M")
    # image_name = 'field_c_'+str(now_time)+'_'+variable_name+'_'+str(i)+'_'+str(var)+'.jpg'
    image_name_3d = 'field_c_'+str(now_time)+'_'+variable_name+'_'+str(i)+'_'+str(var)+'.svg'

    def draw_3Dplot(matrix):
        """
        :param matrix - matrix you want to visualize
        :returns plot
        """
        x = np.arange(np.size(matrix, axis=0))
        y = np.arange(np.size(matrix, axis=1))
        x, y = np.meshgrid(x, y)
        ax = surface_fig.gca(projection='3d')
        surf = ax.plot_surface(x, y, matrix, rstride=1, cstride=1, cmap='hot', linewidth=0, antialiased=False)
        surface_fig.colorbar(surf, shrink=0.5, aspect=5)
        # # draw contour
        # ax.contour(x, y, matrix, zdir='z', offset=0, linewidth=2)
        # ax.contour(x, y, matrix, zdir='y', offset=np.size(matrix, 0), linewidth=2)
        # ax.contour(x, y, matrix, zdir='x', offset=np.size(matrix, 1), linewidth=2)
        # ax.set_zlim(0, )
        plt.show()
        plt.savefig(image_name_3d, format = "svg")
    # --------------------------

    draw_3Dplot(matrix)
