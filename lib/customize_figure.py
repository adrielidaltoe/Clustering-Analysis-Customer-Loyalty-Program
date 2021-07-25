

def figure_layout(annotations=None, title_text=None, x_label=None, y_label=None, show_legend=False):

    """Customize plotly figures
       
       Parameters
       ----------
       annotations: a list of dictionaries informing the values of parameters
       				to format annotations. 
       x_label: str. Title for the xaxis.
       y_label: str. Title for the yaxis.
       show_legend: boolean. If 'True' show legend.

	"""
    layout_parameters = dict(xaxis=dict(showline=True,
                                        showgrid=False,
                                        showticklabels=True,
                                        linecolor='rgb(204, 204, 204)',
                                        linewidth=2,
                                        ticks='outside',
                                        tickfont=dict(family='Arial',
                                                      size=12,
                                                      color='rgb(82, 82, 82)')
                                       ),
                             yaxis=dict(showline=True,
                                        showgrid=False,
                                        showticklabels=True,
                                        linecolor='rgb(204, 204, 204)',
                                        linewidth=2,
                                        ticks='outside',
                                        tickfont=dict(family='Arial',
                                                      size=12,
                                                      color='rgb(82, 82, 82)')
                                       ),
                             title=dict(text=title_text,
                                        font=dict(family='Arial',
                                                  size=25,
                                                  color='rgb(37,37,37)'),
                                        ),
                             showlegend=show_legend,
                             plot_bgcolor='white',
                             autosize=False,
                             yaxis_title = y_label,
                             xaxis_title = x_label,
                             annotations = annotations
                            )
    
    return layout_parameters