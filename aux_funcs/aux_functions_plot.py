# -*- coding: utf-8 -*-

# import packages
import math

import numpy as np
import pandas as pd
import plotly.graph_objects as go



def create_empty_field(
    below=False, colour="green", line_colour=None, size=1, len_field=105, wid_field=68
):
    """
    Function returns a plotly figure of a soccer field.
    :param below: (bool) If true, any additional traces will overlay the field; otherwise, the field will overlay the
                         additional traces
    :param colour: (str) Colour of the field; currently only "green" and "white" are supported
    :param line_colour: (str) Colour of the line; if none it is automatically set based on the field colour
    :param size: (float) Size relative to the standard size
    :param len_field: (int) Length of soccer field in meters (needs to be between 90m and 120m)
    :param wid_field: (int) Width of soccer field in meters (needs to be between 60m and 90m)
    :return: go.Figure with a soccer field
    """

    # check the input for correctness
    assert 90 <= len_field <= 120
    assert 60 <= wid_field <= 90
    assert colour in ["green", "white"]
    assert type(below) is bool

    # size for center point and penalty points
    size_point = 0.5

    field_colour = "rgba(0,255,112,1)" if colour == "green" else "white"

    if line_colour is None:
        line_colour = "white" if colour == "green" else "black"

    # set the overall layout of the field
    layout = go.Layout(
        # make sure the field is green
        plot_bgcolor=field_colour,
        xaxis=dict(
            range=[-5, len_field + 5],
            zeroline=False,
            showgrid=False,
            showticklabels=False,
        ),
        yaxis=dict(
            range=[-5, wid_field + 5],
            zeroline=False,
            showgrid=False,
            showticklabels=False,
        ),
    )

    # create an empty figure for which only the layout is set
    fig = go.Figure(layout=layout)

    # add the halfway line
    ######################
    fig.add_shape(
        dict(
            type="line",
            x0=len_field / 2,
            y0=0,
            x1=len_field / 2,
            y1=wid_field,
            line=dict(color=line_colour, width=2),
        )
    )

    # add left penalty area
    ########################
    y_box = (wid_field - 40.32) / 2
    x_vals = [0, 16, 16, 0]
    y_vals = [wid_field - y_box, wid_field - y_box, y_box, y_box]

    for i in range(len(x_vals) - 1):
        fig.add_shape(
            # Line Vertical
            dict(
                type="line",
                x0=x_vals[i],
                y0=y_vals[i],
                x1=x_vals[i + 1],
                y1=y_vals[i + 1],
                line=dict(color=line_colour, width=2),
            )
        )

    # add left goal area
    ####################
    y_small_box = 7.32 / 2 + 5.5
    x_vals = [0, 5.5, 5.5, 0]
    y_vals = [
        wid_field / 2 - y_small_box,
        wid_field / 2 - y_small_box,
        wid_field / 2 + y_small_box,
        wid_field / 2 + y_small_box,
    ]

    for i in range(len(x_vals) - 1):
        fig.add_shape(
            # Line Vertical
            dict(
                type="line",
                x0=x_vals[i],
                y0=y_vals[i],
                x1=x_vals[i + 1],
                y1=y_vals[i + 1],
                line=dict(color=line_colour, width=2),
            )
        )

    # add right penalty area
    ########################
    x_vals = [len_field, len_field - 16, len_field - 16, len_field]
    y_vals = [wid_field - y_box, wid_field - y_box, y_box, y_box]

    for i in range(len(x_vals) - 1):
        fig.add_shape(
            # Line Vertical
            dict(
                type="line",
                x0=x_vals[i],
                y0=y_vals[i],
                x1=x_vals[i + 1],
                y1=y_vals[i + 1],
                line=dict(color=line_colour, width=2),
            )
        )

    # add right goal area
    #####################
    y_small_box = 7.32 / 2 + 5.5
    x_vals = [len_field, len_field - 5.5, len_field - 5.5, len_field]
    y_vals = [
        wid_field / 2 - y_small_box,
        wid_field / 2 - y_small_box,
        wid_field / 2 + y_small_box,
        wid_field / 2 + y_small_box,
    ]

    for i in range(len(x_vals) - 1):
        fig.add_shape(
            # Line Vertical
            dict(
                type="line",
                x0=x_vals[i],
                y0=y_vals[i],
                x1=x_vals[i + 1],
                y1=y_vals[i + 1],
                line=dict(color=line_colour, width=2),
            )
        )

    # add left penalty point
    ########################
    pen_point = (11, wid_field / 2)
    x_vals = [pen_point[0] - size_point, pen_point[0] + size_point]
    y_vals = [pen_point[1] - size_point, pen_point[1] + size_point]

    fig.add_shape(
        # unfilled circle
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=x_vals[0],
            y0=y_vals[0],
            x1=x_vals[1],
            y1=y_vals[1],
            line_color=line_colour,
            fillcolor=line_colour,
        )
    )

    # add right penalty point
    #########################
    pen_point = (len_field - 11, wid_field / 2)
    x_vals = [pen_point[0] - size_point, pen_point[0] + size_point]
    y_vals = [pen_point[1] - size_point, pen_point[1] + size_point]

    fig.add_shape(
        # unfilled circle
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=x_vals[0],
            y0=y_vals[0],
            x1=x_vals[1],
            y1=y_vals[1],
            line_color=line_colour,
            fillcolor=line_colour,
        )
    )

    # add center spot
    #################
    pen_point = (len_field / 2, wid_field / 2)
    x_vals = [pen_point[0] - size_point, pen_point[0] + size_point]
    y_vals = [pen_point[1] - size_point, pen_point[1] + size_point]

    fig.add_shape(
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=x_vals[0],
            y0=y_vals[0],
            x1=x_vals[1],
            y1=y_vals[1],
            line_color=line_colour,
            fillcolor=line_colour,
        )
    )

    # add center circle
    ###################

    # radius of the center circle (in meters)
    rad_circle = 9.15

    circle_y = wid_field / 2 - rad_circle
    circle_x = len_field / 2 - rad_circle

    fig.add_shape(
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=circle_x,
            y0=circle_y,
            x1=len_field - circle_x,
            y1=wid_field - circle_y,
            line_color=line_colour,
        )
    )

    # add outer lines
    ###################

    fig.add_shape(
        dict(
            type="line",
            x0=0,
            y0=0,
            x1=len_field,
            y1=0,
            line=dict(color=line_colour, width=2),
        )
    )

    # add the out lines
    fig.add_shape(
        dict(
            type="line",
            x0=0,
            y0=0,
            x1=0,
            y1=wid_field,
            line=dict(color=line_colour, width=2),
        )
    )

    # add the out lines
    fig.add_shape(
        dict(
            type="line",
            x0=0,
            y0=wid_field,
            x1=len_field,
            y1=wid_field,
            line=dict(color=line_colour, width=2),
        )
    )

    # add the out lines
    fig.add_shape(
        dict(
            type="line",
            x0=len_field,
            y0=0,
            x1=len_field,
            y1=wid_field,
            line=dict(color=line_colour, width=2),
        )
    )

    # add goals
    ###########

    goal_width = 7.32

    # left goal
    fig.add_shape(
        dict(
            type="line",
            x0=0,
            y0=(wid_field - goal_width) / 2,
            x1=-2,
            y1=(wid_field - goal_width) / 2,
            line=dict(color=line_colour, width=2),
        )
    )

    fig.add_shape(
        dict(
            type="line",
            x0=0,
            y0=(wid_field + goal_width) / 2,
            x1=-2,
            y1=(wid_field + goal_width) / 2,
            line=dict(color=line_colour, width=2),
        )
    )

    fig.add_shape(
        dict(
            type="line",
            x0=-2,
            y0=(wid_field - goal_width) / 2,
            x1=-2,
            y1=(wid_field + goal_width) / 2,
            line=dict(color=line_colour, width=2),
        )
    )

    # right goal
    fig.add_shape(
        dict(
            type="line",
            x0=len_field,
            y0=(wid_field - goal_width) / 2,
            x1=len_field + 2,
            y1=(wid_field - goal_width) / 2,
            line=dict(color=line_colour, width=2),
        )
    )

    fig.add_shape(
        dict(
            type="line",
            x0=len_field,
            y0=(wid_field + goal_width) / 2,
            x1=len_field + 2,
            y1=(wid_field + goal_width) / 2,
            line=dict(color=line_colour, width=2),
        )
    )

    fig.add_shape(
        dict(
            type="line",
            x0=len_field + 2,
            y0=(wid_field - goal_width) / 2,
            x1=len_field + 2,
            y1=(wid_field + goal_width) / 2,
            line=dict(color=line_colour, width=2),
        )
    )

    # configure the layout such that additional traces overlay the field
    if below:
        for shape in fig.layout["shapes"]:
            shape["layer"] = "below"

    # update the layout such that the field looks symmetrical
    fig.update_layout(
        autosize=False, width=len_field * 8 * size, height=wid_field * 9 * size
    )

    return fig


def _build_hover_text(row, dict_info):
    """
    Helper function to build the hover text
    """
    text = ""
    for key in dict_info.keys():
        if "display_type" in dict_info[key]:
            text += "{}: {:^{display_type}}<br />".format(
                key,
                row[dict_info[key]["values"]],
                display_type=dict_info[key]["display_type"],
            )
        else:
            text += "{}: {}<br />".format(key, row[dict_info[key]["values"]])
    return text





def _calculate_bucket_for_position(series, nb_buckets, min_pos_val, max_pos_val):
    """
    Helper function to calculate the bucket for each position
    """
    buckets = np.arange(min_pos_val, max_pos_val + 0.001, max_pos_val / nb_buckets)

    df_buckets = pd.DataFrame()
    df_buckets["id"] = np.arange(len(buckets) - 1)
    df_buckets["minValueZone"] = list(buckets)[:-1]
    df_buckets["maxValueZone"] = list(buckets)[1:]
    df_buckets["meanValueZone"] = (
        df_buckets["minValueZone"] + df_buckets["maxValueZone"]
    ) / 2

    buckets[-1] = buckets[-1] + 0.001

    return pd.cut(series, buckets, labels=False, include_lowest=True), df_buckets


def prepare_heatmap(
    df,
    col_x,
    col_y,
    nb_buckets_x,
    nb_buckets_y,
    agg_type="count",
    agg_col=None,
    return_df=False,
    length_field=105,
    width_field=68,
    tracking_data=False,
):
    """
    Helper function to prepare a heatmap. It is most often used in combination with the function *create_heatmap*
    below.
    :param df: (pd.DataFrame) Data frame containing all the relevant data
    :param col_x: (str) Column indicating the position in x-direction
    :param col_y: (str) Column indicating the position in y-direction
    :param nb_buckets_x: (int) Split the field into *nb_buckets_x* buckets in x-direction
    :param nb_buckets_y: (int) Split the field into *nb_buckets_y* buckets in y-direction
    :param agg_type: (str) Aggregation type, e.g. mean, median etc. If None, if defaults to *count*
    :param agg_col: (str) Column name for which aggregation should be made. If None, number of appearances per grid
                     cell are computed
    :param return_df: (bool) If True, function returns *df* with additional columns indicating the grid cell
    :param length_field (int) Length of the field in meters
    :param width_field: (int) Width of the field in meters
    :param tracking_data: (bool) Whether the underlying data is tracking data or not
    :return: Returns three np.arrays for
            1. The center points of the grid cells in x-direction
            2. The center points of the grid cells in y-direction
            3. The values for each grid cell
    """

    df = df.copy()

    if tracking_data:
        df[col_y] = -1 * (df[col_y] - width_field / 2) + width_field / 2

    df[col_x + "Zone"], df_lookup_x_buckets = _calculate_bucket_for_position(
        df[col_x], nb_buckets_x, 0, length_field
    )
    df[col_y + "Zone"], df_lookup_y_buckets = _calculate_bucket_for_position(
        df[col_y], nb_buckets_y, 0, width_field
    )

    if agg_col is None:
        agg_col = col_x + "Zone"

    df_pos = (
        df.groupby([col_x + "Zone", col_y + "Zone"])
        .agg(aggVal=(agg_col, agg_type))
        .reset_index()
    )

    df_all_pos = pd.DataFrame(
        [(x, y) for x in df_lookup_x_buckets["id"] for y in df_lookup_y_buckets["id"]],
        columns=[col_x + "Zone", col_y + "Zone"],
    )

    df_lookup_x_buckets.rename(
        columns={"id": col_x + "Zone", "meanValueZone": col_x + "ZoneMean"},
        inplace=True,
    )
    df_lookup_y_buckets.rename(
        columns={"id": col_y + "Zone", "meanValueZone": col_y + "ZoneMean"},
        inplace=True,
    )

    df_all_pos = pd.merge(
        df_all_pos,
        df_lookup_x_buckets[[col_x + "Zone", col_x + "ZoneMean"]],
        how="left",
    )
    df_all_pos = pd.merge(
        df_all_pos,
        df_lookup_y_buckets[[col_y + "Zone", col_y + "ZoneMean"]],
        how="left",
    )

    df_pos = pd.merge(df_all_pos, df_pos, how="left").fillna(0)
    df_img = df_pos.pivot(col_y + "ZoneMean", col_x + "ZoneMean", "aggVal")

    x = list(df_img.columns)
    y = [width_field - x for x in df_img.index]

    img = np.array(df_img)

    if return_df:
        return img, x, y, df

    return img, x, y


def create_heatmap(
    x,
    y,
    z,
    dict_info,
    title_name=None,
    colour_scale=None,
    zsmooth=False,
    legend_name=None,
    size=1,
):
    """
    Function to create a coloured heatmap on top of a soccer field
    :param x: (np.array) Center points of the grid cells in x-direction, i.e. length of the field
    :param y: (np.array) Center points of the grid cells in y-direction, i.e. width of the field
    :param z: (np.array) Two-dimensional array containing the values for all grid cells
    :param dict_info: (dict) Defines what and how information should be shown when hovering over the grid cells.
                       If None, no information is displayed
    :param title_name: (str) Title to be added above the plot
    :param colour_scale: (tuple) Contains the min and max values for the colour scale
    :param zsmooth: (str or False) Smoothing parameter as used by go.Heatmap
    :param legend_name: (str) Name to be added on top of the colour legend bar
    :param size: (float) Relative size of the field
    :return: go.Figure with a heatmap plotted on top of the soccer field
    """

    if dict_info is not None:
        # Prepare the text to be shown when hovering over the heatmap
        hovertext = list()
        for idy in range(len(z)):
            hovertext.append(list())
            for idx in range(len(z[1])):
                text = ""
                for key in dict_info.keys():
                    text += "{}: {:^{display_type}}<br />".format(
                        key,
                        dict_info[key]["values"][idy][idx],
                        display_type=dict_info[key]["display_type"],
                    )
                hovertext[-1].append(text)

    # get the empty soccer field
    fig = create_empty_field(colour="white", line_colour="white", size=size)

    # overlay field with the heatmap

    # if no information should be displayed
    if dict_info is None:
        fig.add_trace(go.Heatmap(x=x, y=y, z=z, zsmooth=zsmooth, hoverinfo="none"))
    # if some information should be displayed
    else:
        fig.add_trace(
            go.Heatmap(x=x, y=y, z=z, zsmooth=zsmooth, hoverinfo="text", text=hovertext)
        )

    if colour_scale is not None:
        fig["data"][-1]["zmin"] = colour_scale[0]
        fig["data"][-1]["zmax"] = colour_scale[1]

    if title_name is not None:
        fig.update_layout(
            title={
                "text": title_name,
                "y": 0.9,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "top",
            }
        )

    if legend_name is not None:
        fig.update_layout(
            annotations=[
                dict(
                    x=1.07,
                    y=1.03,
                    align="right",
                    valign="top",
                    text=legend_name,
                    showarrow=False,
                    xref="paper",
                    yref="paper",
                    xanchor="center",
                    yanchor="top",
                )
            ]
        )

    return fig








def _hex_to_rgb(hex):
    """
    Helper function to convert hex colour into RGB vector
    """
    # Pass 16 to the integer function for change of base
    return [int(hex[i : i + 2], 16) for i in range(1, 6, 2)]


def _rgb_to_hex(rgb):
    """
    Helper function to convert RGB colour vector into hex
    """
    rgb = [int(x) for x in rgb]
    return "#" + "".join(
        ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in rgb]
    )


def colour_scale(start_hex, finish_hex, n=101):
    """
    Function returns a gradient list of *n* colors between
    the two hex colors *start_hex* and *end_hex*
    :param start_hex: (str) Six-digit color string of the start colour, e.g. #FFFFFF"
    :param finish_hex: (str) Six-digit color string of the start colour, e.g. #FFFFFF"
    :param n: (int) Number of colours to be produced
    """
    # Starting and ending colors in RGB form
    s = _hex_to_rgb(start_hex)
    f = _hex_to_rgb(finish_hex)
    # Initilize a list of the output colors with the starting color
    rgb_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)
        ]
        # Add it to our list of output colors
        rgb_list.append(curr_vector)

    return [_rgb_to_hex(RGB) for RGB in rgb_list]
