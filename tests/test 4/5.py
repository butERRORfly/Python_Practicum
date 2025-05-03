import matplotlib.pyplot as plt


def strength(chart_type, color, **animals):
    fig, ax = plt.subplots()
    ax.set_title('Strength')
    
    if chart_type == 'bar':
        bars = ax.bar(animals.keys(), animals.values(), color=color)
    elif chart_type == 'barh':
        bars = ax.barh(list(animals.keys()), list(animals.values()), color=color)
    else:
        raise ValueError
    
    plt.savefig('result.png')
    plt.close()