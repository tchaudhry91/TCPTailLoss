from pylab import *


fig = ''
ax = ''


def setBoxColors(bp):
    setp(bp['boxes'][1], color='green')
    setp(bp['caps'][2], color='green')
    setp(bp['caps'][3], color='green')
    setp(bp['whiskers'][2], color='green')
    setp(bp['whiskers'][3], color='green')
    setp(bp['fliers'][2], color='green')
    setp(bp['fliers'][3], color='green')
    setp(bp['medians'][1], color='green')

    setp(bp['boxes'][0], color='red')
    setp(bp['caps'][0], color='red')
    setp(bp['caps'][1], color='red')
    setp(bp['whiskers'][0], color='red')
    setp(bp['whiskers'][1], color='red')
    setp(bp['fliers'][0], color='red')
    setp(bp['fliers'][1], color='red')
    setp(bp['medians'][0], color='red')


def plotAll():
    """This Function Reads Files from ./Recordings/*
        and plots a box and whisker graph for the same
        the file name is saved as
        e.g fast_long_compl.png
            fast_long_retrans.png
    """
    initFigure()
    name_base = "Recordings/"
    TLP_status = ["TLP", "NoTLP"]
    link_speeds = ["fast", "moderate", "slow"]
    payloads = ["long", "medium", "short"]
    drop_counts = [1, 2, 4, 8]
    for link_speed in link_speeds:
        for payload in payloads:
            data_c_list = []
            data_r_list = []
            for drop_count in drop_counts:
                data_c = [[], []]
                data_r = [[], []]
                for tlp in TLP_status:
                    f_name = name_base
                    f_name += tlp + link_speed
                    f_name += "_" + payload
                    plot_name = name_base
                    plot_name += link_speed + "_"
                    plot_name += payload
                    f_name += "_" + str(drop_count)
                    f_read = open(f_name)
                    data = f_read.read()
                    f_read.close()
                    pos = 0
                    if tlp == "NoTLP":
                        pos = 0
                    else:
                        pos = 1
                    data = data.split("\n")[:-1]
                    for i in range(len(data)):
                        data[i] = data[i].split("\t")
                        data_c[pos].append(float(data[i][0]))
                        data_r[pos].append(float(data[i][1]))
                data_c_list.append(data_c)
                data_r_list.append(data_r)
            #Ready To Plot
            plotIndividual(data_c_list, "comp", plot_name)
            plotIndividual(data_r_list, "retrans", plot_name)


def initFigure():
    """(Re)Initialise the figure after each plot
    """
    global fig
    global ax
    fig = figure()
    ax = axes()
    hold(True)


def plotIndividual(data, option, f_name):
    """This function an actual box plot for the data provided.
        Two plots can be generated depending on option:
        One for Completion Time
        One for Retransmission
    """
    global ax
    ax = axes()
    ymin = 1000
    ymax = 0

    #Create a suitable Plot Range On the Axes
    for d in data:
        ymin = min((min(min(d))), ymin)
        ymax = max((max(max(d))), ymax)
    ymin = ymin - 0.05*ymin
    ymax = ymax + 0.05*ymin

    f_name += "_" + option + ".png"
    pos = 1
    for i in range(len(data)):
        bp = boxplot(data[i], positions=[pos, pos+1],
                     widths=0.6)
        setBoxColors(bp)
        pos += 3
    ylim(ymin, ymax)
    xlim(0, 12)
    ax.set_xlabel("Drop Count")
    ax.set_ylabel("Time Elapsed")
    ax.set_xticklabels(['1', '2', '4', '8'])
    ax.set_xticks([1.5, 4.5, 7.5, 10.5])

    #Plot Legend
    hB, = plot([1, 1], 'r-')
    hR, = plot([1, 1], 'g-')
    legend((hB, hR), ('NoTLP', 'TLP'))
    hB.set_visible(False)
    hR.set_visible(False)

    print("Plotting:" + f_name)
    savefig(f_name)
    fig.clear()

if __name__ == "__main__":
    plotAll()
