"""
The quick drawing function
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

__all__ = ["quick_draw_spatial_basemap"]


def quick_draw_spatial_basemap(
    nrows: int = 1,
    ncols: int = 1,
    central_longitude: float = 0.0,
    draw_labels: str | bool | list | dict = ["bottom", "left"],
    gridlines_color: str = "grey",
    gridlines_alpha: float = 0.5,
    gridlines_linestyle: str = "--",
    coastlines_edgecolor: str = "black",
    coastlines_linewidths: float = 0.5,
):
    """
    Create geographical and spatial base map.

    Parameters
    ----------
    nrows, ncols :py:class:`int <int>`, default: 1
        Number of rows/columns of the subplot grid.
    central_longitude: :py:class:`float <float>`, default: 0.
        The central longitude for `cartopy.crs.PlateCarree` projection.
    draw_labels: :py:class:`str <str>` | :py:class:`bool <bool>` | :py:class:`list <list>` | :py:class:`dict <dict>`, default: ["bottom", "left"].
        Toggle whether to draw labels. For finer control, attributes of Gridliner may be modified individually.

        - string: `"x"` or `"y"` to only draw labels of the respective coordinate in the CRS.
        - list: Can contain the side identifiers and/or coordinate types to select which ones to draw. For all labels one would use `["x", "y", "top", "bottom", "left", "right", "geo"]`.
        - dict: The keys are the side identifiers `("top", "bottom", "left", "right")` and the values are the coordinates `("x", "y")`; this way you can precisely decide what kind of label to draw and where. For x labels on the bottom and y labels on the right you could pass in `{"bottom": "x", "left": "y"}`.

        Note that, by default, x and y labels are not drawn on left/right and top/bottom edges respectively unless explicitly requested.
    gridlines_color: :py:class:`str <str>`, default: `grey`.
        The parameter `color` for `ax.gridlines`.
    gridlines_alpha: :py:class:`float <float>`, default: `0.5`.
        The parameter `alpha` for `ax.gridlines`.
    gridlines_linestyle: :py:class:`str <str>`, default: `"--"`.
        The parameter `linestyle` for `ax.gridlines`.
    coastlines_edgecolor: :py:class:`str <str>`, default: `"black"`.
        The parameter `edgecolor` for `ax.coastlines`.
    coastlines_linewidths: :py:class:`float <float>`, default: `0.5`.
        The parameter `linewidths` for `ax.coastlines`.

    Returns
    -------
    - fig: :py:class:`Figure <matplotlib:matplotlib.figure.Figure>`
    - ax: :py:class:`Axes <matplotlib:matplotlib.axes.Axes>` or array of Axes: `ax` can be either a single :py:class:`Axes <matplotlib:matplotlib.axes.Axes>` object, or an array of Axes objects if more than one subplot was created. The dimensions of the resulting array can be controlled with the squeeze keyword.

    .. seealso::
        :py:func:`matplotlib.pyplot.subplots <matplotlib:matplotlib.pyplot.subplots>`
        :py:func:`cartopy.mpl.geoaxes.GeoAxes.gridlines <cartopy:cartopy.mpl.geoaxes.GeoAxes.gridlines>`
        :py:func:`cartopy.mpl.geoaxes.GeoAxes.coastlines <cartopy:cartopy.mpl.geoaxes.GeoAxes.coastlines>`
    """

    fig, ax = plt.subplots(
        nrows=nrows,
        ncols=ncols,
        subplot_kw={
            "projection": ccrs.PlateCarree(central_longitude=central_longitude)
        },
    )

    if nrows == 1 and ncols == 1:
        ax.gridlines(
            draw_labels=draw_labels,
            color=gridlines_color,
            alpha=gridlines_alpha,
            linestyle=gridlines_linestyle,
        )
        ax.coastlines(edgecolor=coastlines_edgecolor, linewidths=coastlines_linewidths)
    else:
        for axi in ax.flat:
            axi.gridlines(
                draw_labels=draw_labels,
                color=gridlines_color,
                alpha=gridlines_alpha,
                linestyle=gridlines_linestyle,
            )
            axi.coastlines(
                edgecolor=coastlines_edgecolor, linewidths=coastlines_linewidths
            )
    return fig, ax